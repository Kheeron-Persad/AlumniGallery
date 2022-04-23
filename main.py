import json
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from models import db, User, Job
from forms import SignUp, LogIn, Edit

''' Begin boilerplate code '''

''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  login_manager.init_app(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)
''' End Boilerplate Code '''

# Login form
@app.route('/', methods=['GET'])
def index():
  form = LogIn()
  return render_template('login.html', form=form)

# User submits the login form
@app.route('/login', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
    data = request.form
    user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']): # check credentials
      flash('Logged in successfully.') # send message to next page
      login_user(user) # login the user
      return redirect(url_for('gallery')) # redirect to main page if login successful
  flash('Invalid credentials')
  return redirect(url_for('index'))

# Gets user data from DB and pass to gallery template
@app.route('/gallery', methods=['GET'])
@login_required
def gallery():
  card = User.query.order_by(User.firstname)
  return render_template('gallery.html', cards=card) # pass cards

# Hardcode Job data into Job model to display in job.html
@app.route('/job')
@login_required
def job():
  massy = Job(image="massy.png", company="Massy", title="Accountant", time="Full Time", salary="$7,500 per month", hours="8AM - 5PM", location="San Fernando", skill="Prepare Financial Statements", contact="massy@gmail.com")
  republic = Job(image="republic.png", company="Republic Bank", title="Manager", time="Full Time", salary="$10,000 per month", hours="8AM - 5PM", location="Port of Spain", skill="Project Management", contact="republicbank@gmail.com")
  bmobile = Job(image="bmobile.png", company="Bmobile", title="Sales Cleark", time="Part Time", salary="$5,000 per month", hours="8AM - 3PM", location="Sangre Grande", skill="Communication", contact="bmobile@gmail.com")
  job = [massy.toDict(), republic.toDict(), bmobile.toDict()]
  return render_template('job.html', jobs=job)

# Shows data in the DB, for testing 
@app.route('/users', methods=['GET'])
def get_user():
  users = User.query.all()
  return json.dumps([user.toDict() for user in users])

# Sign up form
@app.route('/signup', methods=['GET'])
def signup():
  signup = SignUp() # create form object
  return render_template('signup.html', form=signup) # pass form object to template

# User submit user form
@app.route('/signup', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username'], email=data['email'], firstname=data['firstname'], lastname=data['lastname'], year=data['year'], programme=data['programme'], faculty=data['faculty'], department=data['department'], instagram=data['instagram'], reddit=data['reddit'], twitter=data['twitter']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('gallery'))# redirect to login page
  flash('Error invalid input!')
  return redirect(url_for('signup'))

# Gets current user logged in ID, query the DB to find user with ID
# Once found, delete and redirect to login, else display error
@app.route('/delete/<id>', methods=['GET'])
@login_required
def delete_card(id):  
  card = User.query.get(id)
  if card:
    db.session.delete(card)
    db.session.commit()
    flash('Card Deleted!')
    return redirect(url_for('index'))
  flash('Unauthorized or card not found')
  return redirect(url_for('gallery')) 

# Logout user
@app.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  flash('Logged Out!')
  return redirect(url_for('index')) 

# # Edit up form
# @app.route('/edit', methods=['GET'])

# def edit():
#   edit = Edit() # create form object
#   return render_template('edit.html', form=edit) # pass form object to template

# # User submit edited form
# @app.route('/edit', methods=['POST'])

# def editAction():
#   form = Edit() # create form object
#   if form.validate_on_submit():
#     data = request.form # get data from form submission
#     id = current_user.id
#     user = User.query.get(id)
#     user = User(username=data['username'], email=data['email'], firstname=data['firstname'], lastname=data['lastname'], year=data['year'], programme=data['programme'], faculty=data['faculty'], department=data['department'], instagram=data['instagram'], reddit=data['reddit'], twitter=data['twitter']) # edit user object
#     user.set_password(data['password']) # set password
#     db.session.add(user) # save new user
#     db.session.commit()
#     flash('Account Created!')# send message
#     return redirect(url_for('gallery'))# redirect to gallery page
#   flash('Error invalid input!')
#   return redirect(url_for('gallery'))

# # Search
# @app.route('/gallery/year', methods=['GET'])
# @login_required
# def year():
#   card = User.query.order_by(User.year)
#   return render_template('gallery.html', cards=card) # pass cards

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)
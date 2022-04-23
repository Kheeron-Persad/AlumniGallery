from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  firstname = db.Column(db.String(80), unique=True, nullable=False)
  lastname = db.Column(db.String(80), unique=True, nullable=False)
  year = db.Column(db.Integer, nullable=False)
  programme = db.Column(db.String(200), nullable=False)
  faculty = db.Column(db.String(200), nullable=False)
  department = db.Column(db.String(120), nullable=False)
  instagram = db.Column(db.String(120))
  reddit = db.Column(db.String(120))
  twitter = db.Column(db.String(120))

  def toDict(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "password": self.password,
      "firstname": self.firstname,
      "lastname": self.lastname,
      "year": self.year,
      "programme": self.programme,
      "faculty": self.faculty,
      "department": self.department,
      "instagram": self.instagram,
      "reddit": self.reddit,
      "twitter": self.twitter
    }
  
  #hashes the password parameter and stores it in the object
  def set_password(self, password):
    """Create hashed password."""
    self.password = generate_password_hash(password, method='sha256')
  
  #Returns true if the parameter is equal to the object's password property
  def check_password(self, password):
    """Check hashed password."""
    return check_password_hash(self.password, password)
  
  #To String method
  def __repr__(self):
    return '<User {}>'.format(self.username)

class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image= db.Column(db.String(20), nullable=False)
  company = db.Column(db.String(120),nullable=False)
  title = db.Column(db.String(120), nullable=False)
  time= db.Column(db.String(20), nullable=False)
  salary= db.Column(db.String(200), nullable=False)
  hours = db.Column(db.String(120), nullable=False)
  location= db.Column(db.String(120), nullable=False)
  skill = db.Column(db.String(120), nullable=False)
  contact = db.Column(db.String(120), nullable=False)

  def toDict(self):
    return { 
      "id": self.id,
      "image": self.image,
      "company": self.company,
      "title": self.title,
      "time": self.time,
      "salary": self.salary,
      "hours": self.hours,
      "location": self.location,
      "skill": self.skill,
      "contact": self.contact,
    }
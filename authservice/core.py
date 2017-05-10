from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

db = SQLAlchemy()
security = Security()

from models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

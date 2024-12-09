from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from app.db_manager import fetchone
from werkzeug.security import check_password_hash
from app import db

class User(db.Model):
    
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)  # Primary key
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    def __init__(self, user_id, password, name, address, role, phone_number):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.address = address
        self.role = role
        self.phone_number = phone_number

    @staticmethod 
    def findMatchOR(keys, values):
        # Build the SQL query
        sql = "SELECT `user_id`, `password`, `name`, `address`, `role`, `phone_number` FROM Users WHERE "
        where = ' OR '.join(map(lambda k: f"`{k}` = %s", keys))
        query = sql + where
        print(f"Executing SQL: {query}")
        # Execute the query and fetch one result
        result = fetchone(query, values)
    
        # If no result is found, return None
        if not result:
            return None
        # Unpack the result into the User constructor
        return User(*result)
    
    @staticmethod
    def verify_password(stored_password, provided_password):
        # Compare the hashed password with the provided one
        return check_password_hash(stored_password, provided_password)
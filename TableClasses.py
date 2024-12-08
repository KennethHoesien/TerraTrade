from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SoilTypes(db.Model):
    __tablename__ = 'Soil_Types'
    soil_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer)
    pH_level = db.Column(db.Integer)
    type = db.Column(db.String(255))
    NPK_level = db.Column(db.Float)
    quantity = db.Column(db.Float)
    availability = db.Column(db.String(255))
    location = db.Column(db.String(255))

class Owners(db.Model):
    __tablename__ = 'Owners'
    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    email = db.Column(db.String(255))

class Users(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    role = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)

class Farms(db.Model):
    __tablename__ = 'Farms'
    farm_id = db.Column(db.String(255), primary_key=True)
    soil_id = db.Column(db.Integer, db.ForeignKey('Soil_Types.soil_id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('Owners.owner_id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('Listings.listing_id'))
    location = db.Column(db.String(255))
    size = db.Column(db.Float)

class Listings(db.Model):
    __tablename__ = 'Listings'
    listing_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    soil_id = db.Column(db.Integer, db.ForeignKey('Soil_Types.soil_id'))
    price = db.Column(db.Float)
    quantity = db.Column(db.Float)
    date = db.Column(db.Date)

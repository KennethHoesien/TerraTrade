from flask import Flask, app, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()

# classes that refer to the relations in the databse 
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

# making functions to be used by the website devs to connect to the database
def add_user(name, address, role, phone_number):
    if not name or not phone_number:
        raise ValueError("Name and phone number are required")

    new_user = Users(name=name, address=address, role=role, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def add_soil_type(provider_id, pH_level, soil_type, NPK_level, quantity, availability, location):
    new_soil = SoilTypes(
        provider_id=provider_id,
        pH_level=pH_level,
        type=soil_type,
        NPK_level=NPK_level,
        quantity=quantity,
        availability=availability,
        location=location
    )
    db.session.add(new_soil)
    db.session.commit()
    return new_soil

def add_farm(farm_id, soil_id, owner_id, listing_id, location, size):
    # Validate foreign keys
    soil = SoilTypes.query.get(soil_id)
    owner = Owners.query.get(owner_id)
    listing = Listings.query.get(listing_id)
    if not soil:
        raise ValueError(f"Soil with ID {soil_id} does not exist")
    if not owner:
        raise ValueError(f"Owner with ID {owner_id} does not exist")
    if not listing:
        raise ValueError(f"Listing with ID {listing_id} does not exist")

    # Add farm
    new_farm = Farms(
        farm_id=farm_id,
        soil_id=soil_id,
        owner_id=owner_id,
        listing_id=listing_id,
        location=location,
        size=size
    )
    db.session.add(new_farm)
    db.session.commit()
    return new_farm

def add_owner(name, phone_number, email):
    # Check if email is unique
    existing_owner = Owners.query.filter_by(email=email).first()
    if existing_owner:
        raise ValueError(f"Owner with email {email} already exists")

    # Add owner
    new_owner = Owners(name=name, phone_number=phone_number, email=email)
    db.session.add(new_owner)
    db.session.commit()
    return new_owner

def add_listing(user_id, soil_id, price, quantity, date):
    # Validate foreign keys
    user = Users.query.get(user_id)
    soil = SoilTypes.query.get(soil_id)
    if not user:
        raise ValueError(f"User with ID {user_id} does not exist")
    if not soil:
        raise ValueError(f"Soil with ID {soil_id} does not exist")

    # Add listing
    new_listing = Listings(
        user_id=user_id,
        soil_id=soil_id,
        price=price,
        quantity=quantity,
        date=date
    )
    db.session.add(new_listing)
    db.session.commit()
    return new_listing

# API endpoints for these methods
'''


@app.route('/api/add_soil_type', methods=['POST'])
def api_add_soil_type():
    data = request.json
    try:
        soil = add_soil_type(
            provider_id=data['provider_id'],
            pH_level=data['pH_level'],
            soil_type=data['type'],
            NPK_level=data['NPK_level'],
            quantity=data['quantity'],
            availability=data['availability'],
            location=data['location']
        )
        return {"success": True, "soil_id": soil.soil_id}, 200
    except Exception as e:
        return {"success": False, "error": str(e)}, 400

@app.route('/api/add_farm', methods=['POST'])
def api_add_farm():
    data = request.json
    try:
        farm = add_farm(
            farm_id=data['farm_id'],
            soil_id=data['soil_id'],
            owner_id=data['owner_id'],
            listing_id=data['listing_id'],
            location=data['location'],
            size=data['size']
        )
        return {"success": True, "farm_id": farm.farm_id}, 200
    except Exception as e:
        return {"success": False, "error": str(e)}, 400

@app.route('/api/add_owner', methods=['POST'])
def api_add_owner():
    data = request.json
    try:
        owner = add_owner(
            name=data['name'],
            phone_number=data['phone_number'],
            email=data['email']
        )
        return {"success": True, "owner_id": owner.owner_id}, 200
    except Exception as e:
        return {"success": False, "error": str(e)}, 400

@app.route('/api/add_listing', methods=['POST'])
def api_add_listing():
    data = request.json
    try:
        listing = add_listing(
            user_id=data['user_id'],
            soil_id=data['soil_id'],
            price=data['price'],
            quantity=data['quantity'],
            date=data.get('date')
        )
        return {"success": True, "listing_id": listing.listing_id}, 200
    except Exception as e:
        return {"success": False, "error": str(e)}, 400
'''
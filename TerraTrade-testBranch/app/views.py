from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.TableClasses import Users, Farms, Listings, SoilTypes, add_user, db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html")

@views.route('/listing', methods=['GET', 'POST'])
def listing():
    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = 5  # Number of listings per page

    # Default query
    query = db.session.query(Listings)

    if request.method == 'POST':
        # Retrieve filter values from the form
        min_price = request.form.get('min_price')
        max_price = request.form.get('max_price')
        min_quantity = request.form.get('min_quantity')
        max_quantity = request.form.get('max_quantity')

        # Apply filters to the query
        if min_price:
            query = query.filter(Listings.price >= float(min_price))
        if max_price:
            query = query.filter(Listings.price <= float(max_price))
        if min_quantity:
            query = query.filter(Listings.quantity >= int(min_quantity))
        if max_quantity:
            query = query.filter(Listings.quantity <= int(max_quantity))

    # Paginate the filtered query
    pagination = query.paginate(page=page, per_page=per_page)
    listings = pagination.items

    return render_template('listing.html', listings=listings, pagination=pagination)




@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/signup')
def signup_form():
    return render_template('signup.html')

@views.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    address = request.form.get('address')
    role = request.form.get('role')
    phone_number = request.form.get('phone_number')

    print(f"Received form data: Name={name}, Address={address}, Role={role}, Phone Number={phone_number}")

    if not name or not address or not role or not phone_number:
        flash('All fields are required!', 'danger')
        return redirect(url_for('views.signup'))

    try:
        add_user(name, address, role, phone_number)  # Call to add_user function
        flash('Signup successful!', 'success')
        return redirect(url_for('views.signup'))
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('views.signup'))

@views.route('/farms')
def farms():
    # Query Farms and join with Listings to get related data
    farms = db.session.query(Farms, Listings).join(Listings, Farms.listing_id == Listings.listing_id).all()
    return render_template('farms.html', farms=farms)


@views.route('/farms/filter')
def filter_farms():
    min_size = request.args.get('min_size', default=0, type=float)
    farms = db.session.query(Farms).filter(Farms.size >= min_size).all()
    return render_template('farms.html', farms=farms)


@views.route('/add-farm', methods=['GET', 'POST'])
def add_farm():
    if request.method == 'POST':
        # Retrieve form data
        farm_id = request.form.get('farm_id')
        soil_id = request.form.get('soil_id')
        owner_id = request.form.get('owner_id')
        listing_id = request.form.get('listing_id')
        location = request.form.get('location')
        size = request.form.get('size')

        # Validate required fields
        if not farm_id or not listing_id or not location or not size:
            flash('Farm ID, Listing ID, Location, and Size are required!', 'danger')
            return redirect(url_for('views.add_farm'))

        try:
            # Add the new farm to the database
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
            flash('Farm added successfully!', 'success')
            return redirect(url_for('views.farms'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('views.add_farm'))

    # Render the form
    return render_template('add_farm.html')

@views.route('/add-listing', methods=['GET', 'POST'])
def add_listing():
    if request.method == 'POST':
        # Get form data
        user_id = request.form.get('user_id')
        soil_id = request.form.get('soil_id')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        date = request.form.get('date')

        # Validate input
        if not user_id or not soil_id or not price or not quantity or not date:
            flash('All fields are required!', 'danger')
            return redirect(url_for('views.add_listing'))

        try:
            # Add the new listing to the database
            new_listing = Listings(
                user_id=user_id,
                soil_id=soil_id,
                price=price,
                quantity=quantity,
                date=date
            )
            db.session.add(new_listing)
            db.session.commit()
            flash('Listing added successfully!', 'success')
            return redirect(url_for('views.listing'))  # Update to the correct route for viewing listings
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('views.add_listing'))

    # Fetch soil types for the dropdown
    soils = db.session.query(SoilTypes).all()
    return render_template('add_listing.html', soils=soils)

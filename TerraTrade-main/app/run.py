from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# Database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",  # Replace with your actual DB username
    passwd="sharkpan",  # Replace with your actual DB password
    db="SoilMarket"
)
cursor = db.cursor()

# Function to fetch soil listings
def get_soil_listings():
    cursor.execute("SELECT id, type, quantity, price, location FROM SoilListings")
    return cursor.fetchall()

# Route for listings page
@app.route('/listings')
def listings():
    soil_data = get_soil_listings()  # Fetch data from the database
    return render_template('listing.html', soils=soil_data)

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert the contact form data into the database
        cursor.execute(
            "INSERT INTO Messages (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        db.commit()
        return "Thank you for your message!"

    # Render the contact page
    return render_template('contact.html')

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Test database connection
@app.route('/test-db')
def test_db():
    print("Test DB route is registered!")  # Debug message
    try:
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        return f"Connected to database: {db_name[0]}"
    except Exception as e:
        return f"Database connection failed: {e}"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


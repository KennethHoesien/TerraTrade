# app.py
from app import create_app

# Create an app instance using the app factory function
app = create_app()

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode in development

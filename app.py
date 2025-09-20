import os
from flask import Flask, render_template, request

# Create a Flask web app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Render the index.html template when the user visits the home page
    return render_template('index.html')

# Define the route for the greeting page, which accepts POST requests
@app.route('/greet', methods=['POST'])
def greet():
    # Get the value of the 'name' field from the submitted form
    name = request.form.get('name')
    # If the name is not provided, use a default value
    if not name:
        name = "Guest"
    # Render the greet.html template, passing the name to it
    return render_template('greet.html', name=name)

# This block ensures the app only runs when the script is executed directly
if __name__ == '__main__':
    # Set FLASK_ENV to development for debugging purposes
    os.environ['FLASK_ENV'] = 'development'
    # Run the app
    app.run()

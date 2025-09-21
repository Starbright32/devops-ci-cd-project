from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# This route now correctly handles the form submission from index.html via a POST request
@app.route("/greet", methods=['POST'])
def greet():
    # Get the value of the 'name' field from the submitted form
    name = request.form.get('name')
    # If the name is not provided, use a default value
    if not name:
        name = "Guest"
    # Render the greet.html template, passing the name to it
    return render_template("greet.html", name=name)

@app.route("/about")
def about():
    # This is the new route for the about page
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

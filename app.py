from flask import Flask # flask → library, Flask → class
from uuid import UUID  # UUID : Unique User ID

app = Flask(__name__) #Creating the Flask application

@app.route("/") # "/" represents the URL path. @app.route() called Decorator connects a URL to a Python function. Run the function associated with /.
def home():
    return "Hello Flask"


@app.route("/user/<int:id>") # Integer URL Converter, Dynamic Routing
def user(id):
    return f"User ID: {id}"

@app.route("/price/<float:amount>") # Float URL converter
def price(amount):
    return f"Price: {amount}"

@app.route("/users/<string:name>") # String URL Converter
def users(name):
    return f"Users name: {name}"

@app.route("/files/<path:file_path>") # Path converter
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>") # UUID converter
def student(user_id): #Flask expects a very specific 36-character hexadecimal format (8-4-4-4-12 digits separated by hyphens).
    return str(user_id)

# Running the application
if __name__ == "__main__":
    app.run(debug=True) # debug = True If your code has an error, Flask gives you useful debugging information. It also automatically reloads the application when you modify the code.
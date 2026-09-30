from flask import Flask # flask → library, Flask → class

app = Flask(__name__) #Creating the Flask application

@app.route("/") # "/" represents the URL path. @app.route() called Decorator connects a URL to a Python function. Run the function associated with /.
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "Welcome to about page"

@app.route("/contact")
def contact():
    return "Welcome to contact page"
    
# Running the application
if __name__ == "__main__":
    app.run(debug=True) # debug = True If your code has an error, Flask gives you useful debugging information. It also automatically reloads the application when you modify the code.
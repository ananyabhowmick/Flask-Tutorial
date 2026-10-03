from flask import Flask, request, render_template # flask → library, Flask → class

app = Flask(__name__) #Creating the Flask application

@app.route("/") # Query Parameter
def home():
    return render_template("index.html") # this is how we add html file in app.py file


# Running the application
if __name__ == "__main__":
    app.run(debug=True) # debug = True If your code has an error, Flask gives you useful debugging information. It also automatically reloads the application when you modify the code.
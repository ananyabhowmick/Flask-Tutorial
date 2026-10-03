from flask import Flask, request, render_template # flask → library, Flask → class

app = Flask(__name__) #Creating the Flask application

@app.route("/") # Query Parameter
def home():
    # Passing Data from Flask to HTML using Jinja2
    name = "Ananya"
    course = "Flask"
    city = "Kolkata"
    age : 22
    # Passing Multiple Variables
    return render_template("index.html", name=name, 
                           course=course,
                           city=city,
                           age=22) # Dynamic Data Rendering


# Running the application
if __name__ == "__main__":
    app.run(debug=True) # debug = True If your code has an error, Flask gives you useful debugging information. It also automatically reloads the application when you modify the code.
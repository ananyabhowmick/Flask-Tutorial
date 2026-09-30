from flask import Flask, request # flask → library, Flask → class

app = Flask(__name__) #Creating the Flask application

@app.route("/search") # Query Parameter
def search(): 
    #here query parameter is "name", Default Parameter is "Guest"
    # if we don't use Default Parameter then it returns "None"
    name = request.args.get("name", "Guest") # "name" > key, request.arg.get("name") > extract the value from key and store into name
    course = request.args.get("course", "Unknown")
    
    return f"{name} is learning {course}"

# Single Query parameter URL: "http://127.0.0.1:5000/search?name=Ananya"
# Multiple Query Parameter URL: "http://127.0.0.1:5000/search?name=Ananya&course=Flask"


# Running the application
if __name__ == "__main__":
    app.run(debug=True) # debug = True If your code has an error, Flask gives you useful debugging information. It also automatically reloads the application when you modify the code.
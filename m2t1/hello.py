# minimal Flask app
from flask import Flask

#print("Starting flask program from ", __name__)
app = Flask(__name__)
# Do any app specific setup here
# for instance, loading a database

@app.route("/")
def index():
    # three quotes for multiline strings
    return """
    <h3>Hello from CTS285!!!</h3>
    <p>This is a paragraph</p>
    <a href="action">Click here</a>


    """
@app.route("/action")
def action():
    return "Hello from the action route!"
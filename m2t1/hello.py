# minimal Flask app
from flask import Flask, render_template

#print("Starting flask program from ", __name__)
app = Flask(__name__)
# Do any app specific setup here
# for instance, loading a database

@app.route("/")
def index():
    # find the template in /templates
    name = "John"
    return render_template("main_page.html", name=name)



@app.route("/action")
def action():
    return "Hello from the action route!"
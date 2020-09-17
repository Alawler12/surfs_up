#import dependencies to make flask app
from flask import Flask

# We're now ready to create a new Flask app instance. "Instance" is a general term in programming to refer to a singular version of something.
app = Flask(__name__)

# create first route

# First, we need to define the starting point, also known as the root
@app.route('/')
# the forward slash denotes that we want to put our data at the root of our routes. The forward slash is commonly known as the highest level of hierarchy in any computer system.

#Whenever you make a route in Flask, you put the code you want in that specific route below @app.route(). Here's what it will look like:
@app.route('/')
def hello_world():
    return 'Hello world'
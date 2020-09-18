#import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask dependencies
from flask import Flask, jsonify

# set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#With the database reflected, we can save our references to each table.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Finally, create a session link from Python to our database with the following code:
session = Session(engine)

# Define our app for Flask
# create flask application called app
app = Flask(__name__)

# create welcome root
@app.route("/")

# The next step is to add the routing information for each of the other routes. 
# For this we'll create a function, and our return statement will have f-strings 
# as a reference to all of the other routes.

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#building the route for precipitation analysis
@app.route("/api/v1.0/precipitation")

def precipitation():
    # code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    #write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    
    #we'll create a dictionary with the date as the key and the precipitation as the value. 
    # To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file
    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)

# build the station route
@app.route("/api/v1.0/stations")

# create a query that will allow us to get all of the stations in our database
def stations():
    results = session.query(Station.station).all()

    #We want to start by unraveling our results into a one-dimensional array.
    # To do this, we want to use thefunction np.ravel(), with results as our parameter
    stations = list(np.ravel(results))

    #Then we'll jsonify the list and return it as JSON.
    return jsonify(stations=stations)

# build the temperature observations route

# build the route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    # find previous year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # filter by primary stations temp obs
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel array into a list and jsonify
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Our last route will be to report on the minimum, average, and maximum temperatures.
# However, this route is different from the previous ones in that we will have to provide 
# both a starting and ending date

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# We need to add parameters to our stats()function: a start parameter and an end parameter

def stats(start=None, end=None):
    #  create a query to select the minimum, average, and maximum temperatures from our SQLite database.
    #  We'll start by just creating a list called sel:
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
     
    # Since we need to determine the starting and ending date, add an if-not statement to our code. 
    # Then, we'll unravel the results into a one-dimensional array and convert them to a list.
    #  Finally, we will jsonify our results and return them. 
    if not end:
        results = session.query(*sel).\
                filter(Measurement.date >= start).\
             filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    # Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
    # We'll use the sel list, which is simply the data points we need to collect. Let's create our next query,
    # which will get our statistics data.

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
         filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
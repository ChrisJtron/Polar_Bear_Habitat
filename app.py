from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

# from matplotlib import style
# style.use('fivethirtyeight')
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import jsonify, render_template

engine = create_engine("sqlite:///BearsOver300Points.sqlite")

Base=automap_base()

Base.prepare(engine, reflect=True)


session=Session(engine)

@app.route("/")
def home():
    # session=Session(engine)
    # return render_template('index.html')
    return 'Welcome'


@app.route("/data")
def results_list():
    results=engine.execute('select * from limited_polar_bears').fetchall()
    # results=engine.execute('select * from limited_polar_bears').groupy_by("BearID_mcp").fetchall()
    results_list=[{'id': result[1], 'idc': result[0], 'timestamp': result[2], 'lat': result[3], 'lon': result[4]} for result in results]

    return jsonify(results_list)


if __name__ == "__main__":
    app.run(debug=True)
import pickle
import os
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('gbdt_clf_i_p.pickle','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict_api', method=['POST'])

def predict_api():
    data= request.json['data']
    print(data)
    print(np.array(list(data.values()).reshape(1,-1)))



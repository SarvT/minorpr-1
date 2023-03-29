from flask import Flask, render_template, request
import requests
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import datalist
import json
import file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def forms():
    gender = request.form['gender']
    age = request.form['age']
    sbp = request.form['sbp']
    hbp = request.form['hbp']
    spo2 = request.form['spo2']
    temp_c = int(request.form['temp'])
    temp = temp_c*9/5+32
    h_rate = request.form['h_rate']
    glc = request.form['glc']
    vitals = [age, sbp, hbp, h_rate, glc, spo2, temp_c]
    res = predict(gender,age, sbp, hbp, h_rate, glc, spo2, temp)
    if (res[0] == 1):
        result = "healthy"
        data = rec("healthy")
        
    elif(res[0] == 2):
        result = "High BP"
        data = rec("highbp")
    elif(res[0] == 3):
        result = "LOW BP"
        data = rec("lowbp")
    elif(res[0] == 4):
        result = "High Sugar"
        data = rec("highsugar")
    elif(res[0] == 5):
        result = "Low Sugar"
        data = rec("lowsugar")
    elif(res[0] == 6):
        result = "Low Oxygen"
        data = rec("lowoxy")
    elif(res[0] == 7):
        result = "High Temperature"
        data = rec("hightemp")
    elif(res[0] == 8):
        result = "Heartbeat is High"
        data = rec("highhbeat")
    elif(res[0] == 9):
        result = "Risk"
        data = rec("risk")
    # result = data.con[res[0]-1]
    return render_template('report.html', res = result, zipped_data = zip(vitals, datalist.vals), data = data)

@app.route('/forms', methods=['POST', 'GET'])
def form():
    return render_template('forms.html')

def rec(stri):
    return file.parsed[stri]

@app.route('/tips', methods=['POST', 'GET'])
def tips():
    return render_template('tips.html')

@app.route('/posts', methods=['POST', 'GET'])
def posts():
    return render_template('post.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

@app.route('/recommendations', methods=['POST', 'GET'])
def recommend():
    return render_template('recommendations.html')

@app.route('/faqs', methods=['POST', 'GET'])
def faqs():
    return render_template('faq.html')

@app.route('/login', methods=['POST', 'GET'])
def logi():
    return render_template('login.html')

def predict(g,a,s,h,hr,gl,sp,temp):
    p = np.array([[g,a,s,h,hr,gl,sp,temp]])
    pickled_model = pickle.load(open('hhcs_rfc.sav', 'rb'))

    return(pickled_model.predict(p))

if __name__ == '__main__':
    app.run(debug=True)
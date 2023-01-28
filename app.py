from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("gbdtrevise2", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():

    age = request.form["age"]

    cg = request.form["capital_gain"]

    cl = request.form["capital_loss"]

    hpw = request.form["hours_per_week"]

    if request.method == "POST":

        # workclass
        workclass=request.form['workclass']
        if(workclass =='Local_gov'):
            Local_gov = 1
            Never_worked = 0
            Private = 0
            Self_emp_inc = 0
            Self_emp_not_inc = 0
            State_gov = 0
            Without_pay = 0

        elif (workclass=='Never_worked'):
            Never_worked = 1
            Local_gov = 0
            Private = 0
            Self_emp_inc = 0
            Self_emp_not_inc = 0
            State_gov = 0
            Without_pay = 0
            
        elif (workclass=='Private'):
            Private = 1
            Never_worked = 0
            Local_gov = 0
            Self_emp_inc = 0
            Self_emp_not_inc = 0
            State_gov = 0
            Without_pay = 0

        elif (workclass=='Self_emp_inc'):
            Self_emp_inc = 1
            Private = 0
            Never_worked = 0
            Local_gov = 0
            Self_emp_not_inc = 0
            State_gov = 0
            Without_pay = 0
            
        elif (workclass=='Self_emp_not_inc'):
            Self_emp_not_inc = 1
            Self_emp_inc = 0
            Private = 0
            Never_worked = 0
            Local_gov = 0
            State_gov = 0
            Without_pay = 0

        elif (workclass=='State_gov'):
            State_gov = 1
            Self_emp_not_inc = 0
            Self_emp_inc = 0
            Private = 0
            Never_worked = 0
            Local_gov = 0
            Without_pay = 0
        
        elif (workclass=='Without_pay'):
            Without_pay = 1
            State_gov = 0
            Self_emp_not_inc = 0
            Self_emp_inc = 0
            Private = 0
            Never_worked = 0
            Local_gov = 0

        else:
            Local_gov = 0
            Never_worked = 0
            Private = 0
            Self_emp_inc = 0
            Self_emp_not_inc = 0
            State_gov = 0
            Without_pay = 0

        # Education
        education = request.form["education"]
        if (education == 'Bachelors'):
            Bachelors = 1
            College = 0
            Doctorate = 0
            Masters = 0
            school = 0

        elif (education == 'College'):
            College = 1
            Bachelors = 0
            Doctorate = 0
            Masters = 0
            school = 0

        elif (education == 'Doctorate'):
            Doctorate = 1
            College = 0
            Bachelors = 0
            Masters = 0
            school = 0

        elif (education == 'Masters'):
            Masters = 1
            Doctorate = 0
            College = 0
            Bachelors = 0
            school = 0

        elif (education == 'school'):
            school = 1
            Masters = 0
            Doctorate = 0
            College = 0
            Bachelors = 0

        else:
            Bachelors = 0
            College = 0
            Doctorate = 0
            Masters = 0
            school = 0
            
        # marital_status
        marital_status = request.form["marital_status"]
        if (marital_status == 'Married_AF_spouse'):
            Married_AF_spouse = 1
            Married_civ_spouse = 0
            Married_spouse_absent = 0
            Never_married = 0
            Separated = 0
            Widowed = 0
        
        elif (marital_status == 'Married_civ_spouse'):
            Married_civ_spouse = 1
            Married_AF_spouse = 0
            Married_spouse_absent = 0
            Never_married = 0
            Separated = 0
            Widowed = 0

        elif (marital_status == 'Married_spouse_absent'):
            Married_spouse_absent = 1
            Married_civ_spouse = 0
            Married_AF_spouse = 0
            Never_married = 0
            Separated = 0
            Widowed = 0

        elif (marital_status == 'Never_married'):
            Never_married = 1
            Married_spouse_absent = 0
            Married_civ_spouse = 0
            Married_AF_spouse = 0
            Separated = 0
            Widowed = 0

        elif (marital_status == 'Separated'):
            Separated = 1
            Never_married = 0
            Married_spouse_absent = 0
            Married_civ_spouse = 0
            Married_AF_spouse = 0
            Widowed = 0
        
        elif (marital_status == 'Widowed'):
            Widowed = 1
            Separated = 0
            Never_married = 0
            Married_spouse_absent = 0
            Married_civ_spouse = 0
            Married_AF_spouse = 0

        else:
            Married_AF_spouse = 0
            Married_civ_spouse = 0
            Married_spouse_absent = 0
            Never_married = 0
            Separated = 0
            Widowed = 0

        # occupation
        occupation = request.form["occupation"]
        if (occupation == 'Craft_repair'):
            Craft_repair = 1
            Exec_managerial = 0
            Farming_fishing = 0
            Handlers_cleaners = 0
            Machine_op_inspct = 0
            Other_service = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0
        
        elif (occupation == 'Exec_managerial'):
            Exec_managerial = 1
            Craft_repair = 0
            Farming_fishing = 0
            Handlers_cleaners = 0
            Machine_op_inspct = 0
            Other_service = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Farming_fishing'):
            Farming_fishing = 1
            Exec_managerial = 0
            Craft_repair = 0
            Handlers_cleaners = 0
            Machine_op_inspct = 0
            Other_service = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Handlers_cleaners'):
            Handlers_cleaners = 1
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Machine_op_inspct = 0
            Other_service = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Machine_op_inspct'):
            Machine_op_inspct = 1
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Other_service = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Other_service'):
            Other_service = 1
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Others_occupation'):
            Others_occupation = 1
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Priv_house_serv'):
            Priv_house_serv = 1
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0
        
        elif (occupation == 'Prof_specialty'):
            Prof_specialty = 1
            Priv_house_serv = 0
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0
        
        elif (occupation == 'Protective_serv'):
            Protective_serv = 1
            Prof_specialty = 0
            Priv_house_serv = 0
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Sales'):
            Sales = 1
            Protective_serv = 0
            Prof_specialty = 0
            Priv_house_serv = 0
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Tech_support'):
            Tech_support = 1
            Sales = 0
            Protective_serv = 0
            Prof_specialty = 0
            Priv_house_serv = 0
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Transport_moving = 0
            Armed_Forces = 0

        elif (occupation == 'Transport_moving'):
            Transport_moving = 1
            Tech_support = 0
            Sales = 0
            Protective_serv = 0
            Prof_specialty = 0
            Priv_house_serv = 0
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
            Armed_Forces = 0

        elif (occupation == 'Armed_Forces'):
            Armed_Forces = 1
            Transport_moving = 0
            Tech_support = 0
            Sales = 0
            Protective_serv = 0
            Prof_specialty = 0
            Priv_house_serv = 0
            Others_occupation = 0
            Other_service = 0
            Machine_op_inspct = 0
            Handlers_cleaners = 0
            Farming_fishing = 0
            Exec_managerial = 0
            Craft_repair = 0
        
        else:
            Craft_repair = 0
            Exec_managerial = 0
            Farming_fishing = 0
            Handlers_cleaners = 0
            Machine_op_inspct = 0
            Other_service = 0
            Others_occupation = 0
            Priv_house_serv = 0
            Prof_specialty = 0
            Protective_serv = 0
            Sales = 0
            Tech_support = 0
            Transport_moving = 0
            Armed_Forces = 0

        # relationship
        relationship = request.form["relationship"]
        if (relationship == 'Not_in_family'):
            Not_in_family = 1
            Other_relative = 0
            Own_child = 0
            Unmarried = 0
            Wife = 0
        
        elif (relationship == 'Other_relative'):
            Other_relative = 1
            Not_in_family = 0
            Own_child = 0
            Unmarried = 0
            Wife = 0

        elif (relationship == 'Own_child'):
            Own_child = 1
            Other_relative = 0
            Not_in_family = 0
            Unmarried = 0
            Wife = 0

        elif (relationship == 'Unmarried'):
            Unmarried = 1
            Own_child = 0
            Other_relative = 0
            Not_in_family = 0
            Wife = 0
        
        elif (relationship == 'Wife'):
            Wife = 1
            Unmarried = 0
            Own_child = 0
            Other_relative = 0
            Not_in_family = 0
        
        else:
            Not_in_family = 0
            Other_relative = 0
            Own_child = 0
            Unmarried = 0
            Wife = 0
            
        
    # race
        race = request.form["race"]
        if (race == 'Asian_Pac_Islander'):
            Asian_Pac_Islander = 1
            Black = 0
            Other = 0
            White = 0
        
        elif (race == 'Black'):
            Black = 1
            Asian_Pac_Islander = 0
            Other = 0
            White = 0

        elif (race == 'Other'):
            Other = 1
            Black = 0
            Asian_Pac_Islander = 0
            White = 0

        elif (race == 'White'):
            White = 1
            Other = 0
            Black = 0
            Asian_Pac_Islander = 0
            
        else:
            Asian_Pac_Islander = 0
            Black = 0
            Other = 0
            White = 0

    # sex
        sex = request.form["sex"]
        if (sex == 'Male'):
            Male = 1
        else:
            Male = 0

    # country
        country = request.form["country"]
        if (country == 'United_States'):
            United_States = 1
            Cuba = 0
            Jamaica = 0
            India = 0
            Others_country = 0
            Mexico = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0
      
        elif (country == 'Cuba'):
            Cuba = 1
            United_States = 0
            Jamaica = 0
            India = 0
            Others_country = 0
            Mexico = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Jamaica'):
            Jamaica = 1
            Cuba = 0
            United_States = 0
            India = 0
            Others_country = 0
            Mexico = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'India'):
            India = 1
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Others_country = 0
            Mexico = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Others_country'):
            Others_country = 1
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Mexico = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0
        
        elif (country == 'Mexico'):
            Mexico = 1
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'South'):
            South = 1
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Puerto_Rico'):
            Puerto_Rico = 1
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Honduras'):
            Honduras = 1
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'England'):
            England = 1
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Canada'):
            Canada = 1
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Germany'):
            Germany = 1
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Iran'):
            Iran = 1
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Philippines'):
            Philippines = 1
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Italy'):
            Italy = 1
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Poland'):
            Poland = 1
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Columbia'):
            Columbia = 1
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

    

        elif (country == 'Thailand'):
            Thailand = 1
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Ecuador'):
            Ecuador = 1
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Laos'):
            Laos = 1
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Taiwan'):
            Taiwan = 1
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Haiti'):
            Haiti = 1
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0
        
        elif (country == 'Portugal'):
            Portugal = 1
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Dominican_Republic'):
            Dominican_Republic = 1
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'El_Salvador'):
            El_Salvador = 1
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'France'):
            France = 1
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Guatemala'):
            Guatemala = 1
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'China'):
            China = 1
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Japan'):
            Japan = 1
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Yugoslavia'):
            Yugoslavia = 1
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Peru'):
            Peru = 1
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Outlying_US_Guam_USVI_etc'):
            Outlying_US_Guam_USVI_etc = 1 
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Scotland '):
            Scotland = 1
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Trinadad_Tobago'):
            Trinadad_Tobago = 1
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Greece'):
            Greece = 1
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Nicaragua'):
            Nicaragua = 1
            Greece = 0
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Vietnam'):
            Vietnam = 1
            Nicaragua = 0
            Greece = 0
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Hong'):
            Hong = 1
            Vietnam = 0
            Nicaragua = 0
            Greece = 0
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Ireland'):
            Ireland = 1
            Hong = 0
            Vietnam = 0
            Nicaragua = 0
            Greece = 0
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Hungary = 0
            Holand_Netherlands = 0

        elif (country == 'Hungary'):
            Hungary = 1
            Ireland = 0
            Hong = 0
            Vietnam = 0
            Nicaragua = 0
            Greece = 0
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            Holand_Netherlands = 0

        elif (country == 'Holand_Netherlands'):
            Holand_Netherlands = 1
            Hungary = 0
            Ireland = 0
            Hong = 0
            Vietnam = 0
            Nicaragua = 0
            Greece = 0
            Trinadad_Tobago = 0
            Scotland = 0
            Outlying_US_Guam_USVI_etc = 0
            Peru = 0
            Yugoslavia = 0
            Japan = 0
            China = 0
            Guatemala = 0
            France = 0
            El_Salvador = 0
            Dominican_Republic = 0
            Portugal = 0
            Haiti = 0
            Taiwan = 0
            Laos = 0
            Ecuador = 0
            Thailand = 0
            Columbia = 0
            Poland = 0
            Italy = 0
            Philippines = 0
            Iran = 0
            Germany = 0
            Canada = 0
            England = 0
            Honduras = 0
            Puerto_Rico = 0
            South = 0
            Mexico = 0
            Others_country = 0
            India = 0
            Jamaica = 0
            Cuba = 0
            United_States = 0
            
        else:
            United_States = 0
            Cuba = 0
            Jamaica = 0
            India = 0
            Others_country = 0
            Mexico = 0
            South = 0
            Puerto_Rico = 0
            Honduras = 0
            England = 0
            Canada = 0
            Germany = 0
            Iran = 0
            Philippines = 0
            Italy = 0
            Poland = 0
            Columbia = 0
            Thailand = 0
            Ecuador = 0
            Laos = 0
            Taiwan = 0
            Haiti = 0
            Portugal = 0
            Dominican_Republic = 0
            El_Salvador = 0
            France = 0
            Guatemala = 0
            China = 0
            Japan = 0
            Yugoslavia = 0
            Peru = 0
            Outlying_US_Guam_USVI_etc = 0
            Scotland = 0
            Trinadad_Tobago = 0
            Greece = 0
            Nicaragua = 0
            Vietnam = 0
            Hong = 0
            Ireland = 0
            Hungary = 0
            Holand_Netherlands = 0

        
        prediction=model.predict([[
            age,
            cg,
            cl,
            hpw,
            Local_gov,
            Never_worked,
            Private,
            Self_emp_inc,
            Self_emp_not_inc,
            State_gov,
            Without_pay,
            Bachelors,
            College,
            Doctorate,
            Masters,
            school,
            Married_AF_spouse,
            Married_civ_spouse,
            Married_spouse_absent,
            Never_married,
            Separated,
            Widowed,
            Craft_repair,
            Exec_managerial,
            Farming_fishing,
            Handlers_cleaners,
            Machine_op_inspct,
            Other_service,
            Others_occupation,
            Priv_house_serv,
            Prof_specialty,
            Protective_serv,
            Sales,
            Tech_support,
            Transport_moving,
            Armed_Forces,
            Not_in_family,
            Other_relative,
            Own_child,
            Unmarried,
            Wife,
            Asian_Pac_Islander,
            Black,
            Other,
            White,
            Male,
            United_States,
            Cuba,
            Jamaica,
            India,
            Others_country,
            Mexico,
            South,
            Puerto_Rico,
            Honduras,
            England,
            Canada,
            Germany,
            Iran,
            Philippines,
            Italy,
            Poland,
            Columbia,
            Thailand,
            Ecuador,
            Laos,
            Taiwan,
            Haiti,
            Portugal,
            Dominican_Republic,
            El_Salvador,
            France,
            Guatemala,
            China,
            Japan,
            Yugoslavia,
            Peru,
            Outlying_US_Guam_USVI_etc,
            Scotland,
            Trinadad_Tobago,
            Greece,
            Nicaragua,
            Vietnam,
            Hong,
            Ireland,
            Hungary,
            Holand_Netherlands
        ]])

        if prediction == 1:
            output = ">50K"
    
        else:
            output = "<=50K"

        return render_template('home.html',prediction_text="Salary of an employee is {}".format(output))


    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
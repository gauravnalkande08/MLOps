
import pickle
import json
import pandas as pd 
import numpy as np
import config 

class Diabetis():
    def __init__(self,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Pregnancies=Pregnancies
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age

        

    def load_model(self):
        with open(config.Model_file_path,"rb") as f:
            self.model=pickle.load(f)

        with open(config.Json_file_path,"r") as f:
            self.json_data=json.load(f)

    def predict_diabetis(self):
        self.load_model()

        len(self.json_data["columns"])

        array = np.zeros(len(self.json_data["columns"]))
        array[0] = self.Pregnancies
        array[1] = self.Glucose
        array[2] = self.BloodPressure
        array[3] = self.SkinThickness
        array[4] = self.Insulin
        array[5] = self.BMI
        array[6] = self.DiabetesPedigreeFunction
        array[7] = self.Age

        print("test array ---",array)
        predict_patient =self.model.predict([array])[0]
        if predict_patient == 1 :
                print("You are Diabetis patient,Take proper treatment and get recover soon")
        else:
                print("You dont have diabetis ...Enjoy your life")
        
if __name__ == "__main__":
    Pregnancies=7.000
    Glucose=142.000
    BloodPressure=60.000
    SkinThickness=33.000
    Insulin=190.000
    BMI=28.800
    DiabetesPedigreeFunction=0.687
    Age=61.000


    dia = Diabetis(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    predict_patient=dia.predict_diabetis()
    if predict_patient == 1 :
                print("You are Diabetis patient,Take proper treatment and get recover soon")
    else:
                print("You dont have diabetis ...Enjoy your life")
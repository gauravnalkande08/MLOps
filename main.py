
from flask import Flask, jsonify, render_template, request
from model.utils import Diabetis
from distutils.command.config import config
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("********  Your Health  Our Responsibility  *********")
    return render_template("index.html")

@app.route('/predict_diabetes', methods = ["POST", "GET"])
def predict_diabetis():

    if request.method == "GET":
        print("We are using GET Method")
       
        
        Pregnancies = eval(request.args.get("Pregnancies"))
        Glucose = eval(request.args.get("Glucose"))
        BloodPressure = eval(request.args.get("BloodPressure"))
        SkinThickness = eval(request.args.get("SkinThickness"))
        Insulin = eval(request.args.get("Insulin"))
        BMI = eval(request.args.get("BMI"))
        DiabetesPedigreeFunction = eval(request.args.get("DiabetesPedigreeFunction"))
        Age = eval(request.args.get("Age"))
        


        dia = Diabetis(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        predict_patient=dia.predict_diabetis()
        # if predict_patient == 1 :
        #         print("You are Diabetis patient,Take proper treatment and get recover soon")
        # else:
        #         print("You dont have diabetis ...Enjoy your life"
        

        # return render_template("index.html", prediction = predict_patient)
        if predict_patient == 1:
                return render_template("index.html", prediction = "You are Diabetis patient,Take proper treatment and get recover soon")
        else:
                return render_template("index.html", prediction = "You dont have diabetis ...Enjoy your life...")

    else:
        print("We are using POST Method")

        Pregnancies = eval(request.form.get("Pregnancies"))
        Glucose = eval(request.form.get("Glucose"))
        BloodPressure = eval(request.form.get("BloodPressure"))
        SkinThickness = eval(request.form.get("SkinThickness"))
        Insulin = eval(request.form.get("Insulin"))
        BMI = eval(request.args.get("BMI"))
        DiabetesPedigreeFunction = eval(request.form.get("DiabetesPedigreeFunction"))
        Age = eval(request.form.get("Age"))


        dia = Diabetis(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        predict_patient=dia.predict_diabetis()

        # return render_template("index.html", prediction = predict_patient)
        if predict_patient == 1:
                return render_template("index.html", prediction = "You are Diabetis patient,Take proper treatment and get recover soon")
        else:
                return render_template("index.html", prediction = "You dont have diabetis ...Enjoy your life...")

    


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= 7555, debug=True)
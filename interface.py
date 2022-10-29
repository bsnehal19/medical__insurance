from flask import Flask,jsonify,render_template,request,json
from project_app.utils import MedicalInsurance
import config


app=Flask(__name__)

@app.route('/')
def hello_flask():
    print('welcome to flask')
    return render_template("home.html")
#####################################################
@app.route('/predict_charges')
def get_insurance_charges():
    data=request.form   #to get data from user
    print('DATA is :',data)
    age=eval(data['age'])
    sex=data['sex']
    bmi=eval(data['bmi'])
    children= eval(data['children'])
    smoker=data['smoker']
    region=data['region']
    med_ins=MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges=med_ins.get_predicted_charges() 

    return jsonify({"MSG":f"predicted Medical Insurance Charge is {charges}"}) 
        


    







if __name__ == "__main__":

   app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)




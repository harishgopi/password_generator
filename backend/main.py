from flask import request, Flask
from password.generator import generator

app = Flask(__name__)

@app.route('/',methods=['get'])
def start():
    #server heath check or welcome api
    return "welcome to password generator"


@app.route('/get_password',methods=['POST'])
def get_password():
    #getting all the details from the API and filling the missing form elements with default value
    min_length=int(request.form.get('min_length') or 15)
    spl_char_length=int(request.form.get('spl_char_length') or 5)
    numbers_length=int(request.form.get('numbers_length') or 5)
    number_of_passwords=int(request.form.get('number_of_passwords') or 10)
    
    #message variable for more verbose error messages
    message = "success"
    
    #wenabling system restrictions
    # number of passwords should not be greater than 1000  
    if(number_of_passwords > 1000):
        message = "sorry the system is limited to 1000 number of passwords per API hit"
        return {"message": message, "data":[]}, 400
    
    #password length , special character length and numbers length should not exceed 2000 
    if (min_length > 2000): 
        message = "sorry the system is limited to a maximum of 2000 in minimum password length"
        return {"message": message, "data":[]}, 400
    
    if (spl_char_length > 2000):
        message = "sorry the system is limited to maximum 2000 in password length and special character length is exceeding 2000"
        return {"message": message, "data":[]}, 400
    
    if (numbers_length > 2000):
        message = "sorry the system is limited to maximum 2000 in password length and numbers length is exceeding 2000"
        return {"message": message, "data":[]}, 400

    #minimum length is used as the actual password length
    #if length of special character and numbers_length exceeds the minimum length 
    #following code adds a additional length for the alphabets
    if (spl_char_length + numbers_length) > 2000:
        message = "sorry the system is limited to maximum 2000 in password length and total special character length and numbers length is exceeding 2000"
        return {"message": message, "data":[]}, 400
    else:
        if (min_length < (spl_char_length + numbers_length)):
            min_length = spl_char_length + numbers_length + 5
    
    return {"message": message, "data": generator(min_length,spl_char_length,numbers_length,number_of_passwords)}, 200


	
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
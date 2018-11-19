from models import User
import re
from werkzeug.security import check_password_hash

def reg_validate(username, password1, password2=None,email=None):
    user = User.query.filter(User.username == username).first()
    user_email = User.query.filter(User.email == email).first()
    print(user)
    if user:
        return 'Username already existed'
    else:
        if len(username) < 4:
            return 'Username cannot shorter than 4'
        elif len(username) > 20:
            return 'Username cannot longer than 20'
        elif len(email) < 7 or re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
            return 'Invalid Email Format'
        elif password2 is None or password1 is None:
            return 'Password cannot be none'
        elif password1 != password2:
            return 'Comfirmed password is different to password'
        elif len(password1) < 6:
            return 'password cannnot shorter than 6'
        elif user_email:
            return 'The Email already has been registered'
        else:
            return 'Register successfully, please Login'

def log_validate(username, password1):
    user = User.query.filter(User.username == username).first()
    print(user)
    if user:
        if username is None:
            return 'Username cannot be empty'
        elif check_password_hash(user.password, password1):
            return 'Login successfully'
        else:
            return 'Wrong Password'
    else:
        return 'Username is not exist'

def reset_validate(username,password,password1,password2):
    user = User.query.filter(User.username == username).first()
    if check_password_hash(user.password, password):
        if password1 == password2:
            if len(password1)<6:
                return 'password cannnot shorter than 6'
            elif len(password1) > 20:
                return 'password cannot longer than 20'
            else:
                return 'Successfully Reset Password'
        else:
            return 'Comfirmed password is different to password'

    else:
        return 'Wrong Password'

def profile_validate(first_name,last_name,email,phone):

    # if len(first_name) is None or len(last_name) is None:
    #     return 'Wrong First Name or Last Name'
    if first_name.isdigit() or last_name.isdigit():
        return 'Wrong First Name or Last Name'

    elif len(email) < 7 or re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
        return 'Invalid Email Format'

    elif phone.isdigit():
        if len(phone) == 10:
            pass
        else:
            return "please enter correct phone number！"
    else:
        return "please enter correct phone number！"

    return 'Successfully modify profile'
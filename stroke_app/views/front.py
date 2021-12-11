from flask import Blueprint
from . import pred
front= Blueprint('front', __name__)
user=[]


@front.route('/gender')
def gender():
    return """남자일 경우 127.0.0.1:5000/gender/Male
여자일 경우 127.0.0.1:5000/gender/Female
이동해주세요"""

@front.route('/gender/gen', defaults={ 'gen' : None })
@front.route('/gender/<gen>')
def get_gender(gen):
    if gen=='Male':
        user.append(gen)
        return "127.0.0.1:5000/age 로 이동하시오"
    elif gen=='Female':
        user.append(gen)
        return "127.0.0.1:5000/age 로 이동하시오"
    else:
        return "잘못된 접근입니다"

@front.route('/age')
def age():
    return "몇살 입니까? 127.0.0.1:5000/age/숫자"
@front.route(f'/age/num', defaults={ 'num' : None })
@front.route(f'/age/<num>')
def get_age(num):
    try:
        int(num)
        user.append(num)
        ans='127.0.0.1:5000/bmi 로 이동하시오'
    except ValueError:
        ans='잘못된 접근입니다'
    return f'{ans}'

@front.route('/bmi')
def bmi(): 
    return "bmi계산 방법는 자신의 몸무게(kg)를 키의 제곱(m)으로 나눈 값입니다 bmi를 입력해주세요 127.0.0.1:5000/bmi/숫자"

@front.route(f'/bmi/num1', defaults={ 'num1' : None })
@front.route(f'/bmi/<num1>')
def get_bmi(num1):
    try:
        float(num1)
        user.append(num1)
        ans='127.0.0.1:5000/result 로 이동하시오'
    except ValueError:
        ans='잘못된 접근입니다'
    return f'{ans}'

@front.route('/result')
def result():
    try:
        ans=pred.Predict(user)
        if int(ans)==1:
            re='위험'
        else:
            re='상대적 덜 위험'
    except ValueError:
        re='다시 처음부터 진행해 주십시오'
    return f"{re}"
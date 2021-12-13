from flask import Blueprint, render_template,request
from . import pred

main = Blueprint('main', __name__)

@main.route('/',methods=['POST', 'GET'])
def index():
    return render_template('index.html'), 200

@main.route('/result')
def index():
    req=request.form
    data=list(req.values())
    try:
        ans=pred.Predict(data)
        if int(ans)==1:
            re='위험합니다'
        else:
            re='좋습니다 건강 유지해주세요 ^^'
    except ValueError:
            re='다시 처음부터 진행해 주십시오'
    return render_template("result.html",ans=re), 200
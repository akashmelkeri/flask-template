from flask import jsonify, request
from . import auth_bp
from models import User

@auth_bp.route('/')
def default():
    users = User.find_all()
    return {"ok":True,"message":"test auth","data":users}
    # return {"ok":True,"message":"default auth"}

# @auth_bp.route('/test')
# def test():
#     users = User.find_all()
#     return {"ok":True,"message":"test auth","data":users}


from flask_restful import Resource
from flask import request
from db import db
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from marshmallow import ValidationError
from models.user import UserModel
from schemas.schemas import UserSchema
from blocklist import BLOCKLIST
user_schema = UserSchema()
class UserRegister(Resource):
    @classmethod
    def post(cls):
        print('ICH BIN HIER')
        user_json=request.get_json()
        
        # validatorPassword = validate.And(validate.Length(min=3, max=30, error="The length of the password must be between 3 and 30 characters"))
        # validatorUsername = validate.And(validate.Length(min=3, max=30, error="The length of the username must be between 3 and 30 characters"))
        try:
            user =user_schema.load(user_json)
            
            
        except ValidationError as err:
            return {"errors": err.messages}, 422
            
        
        
        
        if UserModel.find_by_username(user.username):
            return {"errors":{"username":[ f"User '{user.username}' already in our database!"]}}, 400
        user.save_to_db()
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        user.password=None
        return {"access_token": access_token, "refresh_token": refresh_token, "user":user_schema.dump(user)}, 201
    
    
class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_data=request.get_json()
        print(user_data["email"])
        # user_data=user_schema.load(user_json)
        user=UserModel.find_by_email(user_data["email"])
        if user and safe_str_cmp(user.password, user_data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            user.password=None
            return {"access_token": access_token, "refresh_token": refresh_token, "user":user_schema.dump(user)}, 200

        return {"message": "Invalid credentials"}, 401
    

class UserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
      
        jti = get_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        
        BLOCKLIST.add(jti)
        return {"message": "Logged out"}, 200

    
class TokenRefresh(Resource):
    @classmethod
    @jwt_required(refresh=True)
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
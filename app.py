from flask import Flask, jsonify
import datetime
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from os import environ
from db import db
from ma import ma
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

from libs.image_helper import IMAGE_SET
from resources.user import UserRegister, UserLogin,UserLogout
from resources.portfolio import Portfolio,PutPortfolio,GetPortfolio, DeletePortfolio, PortfolioList
from resources.comment import Comment
from resources.like import LikeOrUnlike
from resources.dislike import DislikeOrUnlike
from libs.image_helper import IMAGE_SET
from resources.skillcard import SkillCard
from resources.email import Email
app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
CORS(app)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/mysite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=10)

flask_uploads.configure_uploads(app, IMAGE_SET)
api = Api(app)
jwt = JWTManager(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    print(err)
    return jsonify(err.messages), 400

api.add_resource(UserRegister, "/api/register")
api.add_resource(UserLogin, "/api/login")
api.add_resource(Portfolio, "/api/portfolios")
api.add_resource(UserLogout, "/api/logout")

api.add_resource(PortfolioList, "/api/portfolios")
api.add_resource(LikeOrUnlike, "/api/portfolios/<int:id>/like")
api.add_resource(DislikeOrUnlike, "/api/portfolios/<int:id>/dislike")
api.add_resource(GetPortfolio, "/api/portfolios/<string:id>")
api.add_resource(PutPortfolio, "/api/portfolios/<int:id>")


api.add_resource(DeletePortfolio, "/api/portfolios/<int:id>")



api.add_resource(Comment, "/api/portfolios/<int:id>/comments")

api.add_resource(SkillCard, "/api/skillcards")
api.add_resource(Email, "/api/email")






app.config['SECRET_KEY']= environ.get("SECRET_KEY")
db.init_app(app)
@app.before_first_request

def create_tables():

    db.create_all()
    
    
if __name__ == '__main__':
  
    ma.init_app(app)
    app.run(port=5000, debug=True)

from sqlalchemy.orm import session
from flask_restful import Resource
from flask import request
from sqlalchemy import select
from db import db
from schemas.schemas import PortfolioSchema, LikeSchema, DislikeSchema
from models.portfolio import PortfolioModel

from models.like import LikeModel 
from models.dislike import DislikeModel
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
post_schema=PortfolioSchema()

like_list=PortfolioSchema(many=True)

class LikeOrUnlike(Resource):
    @classmethod
    @jwt_required()
    def post(cls, id):
 
        user_who_liked= get_jwt_identity()
        portfolio= PortfolioModel.find_by_id(id)
        like=db.session.query(LikeModel).filter_by(user_id=get_jwt_identity(), portfolio_id=id).first()
        dislike=db.session.query(DislikeModel).filter_by(user_id=get_jwt_identity(), portfolio_id=id).first()
        if like:
            if dislike:
                dislike.delete_from_db()
            like.delete_from_db()
            post=PortfolioModel.find_by_id(id)
            return {"post": post_schema.dump(post)}, 200
        else:
            if dislike:
                dislike.delete_from_db()
            like=LikeModel(portfolio_id=id, user_id=user_who_liked)
            portfolio.likes.append(like)
            portfolio.save_to_db()
            portfolio=PortfolioModel.find_by_id(id)
            return {"post": post_schema.dump(portfolio)}, 201
        
        
        

        

        
        
        
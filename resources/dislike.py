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
dislike_schema=DislikeSchema()
portfolio_schema=PortfolioSchema()
like_list=PortfolioSchema(many=True)
class DislikeOrUnlike(Resource):
    @classmethod
    @jwt_required()
    def post(cls, id):
        print('YESSS')
        print('WARUM')
        user_who_disliked= get_jwt_identity()
        portfolio= PortfolioModel.find_by_id(id)
        dislike=db.session.query(DislikeModel).filter_by(user_id=get_jwt_identity(), portfolio_id=id).first()
        like=db.session.query(LikeModel).filter_by(user_id=get_jwt_identity(), portfolio_id=id).first()
        
        if dislike:
            post=dislike.portfolio
            dislike.delete_from_db()
            if like:
                like.delete_from_db()
            return {"post": portfolio_schema.dump(post)}, 200
        else:
            if like:
                like.delete_from_db()
            dislike=DislikeModel(portfolio_id=id, user_id=user_who_disliked)
            portfolio.dislikes.append(dislike)
            portfolio.save_to_db()
            portfolio=PortfolioModel.find_by_id(id)
            return {"post": portfolio_schema.dump(portfolio)}, 201
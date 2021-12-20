
from typing import List
from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from schemas.schemas import CommentSchema



from models.comment import CommentModel
from flask_jwt_extended import (
    jwt_required,
)

comment_schema=CommentSchema()
comment_list=CommentSchema(many=True)

class Comment(Resource):
    @classmethod
    @jwt_required()
    def post(cls, id:int)->"CommentModel":
        comment_json=request.get_json()
        comment_json["portfolio_id"]=id
        comment_json["user_id"]=get_jwt_identity()
        comment= comment_schema.load(comment_json)
      
        comment.save_to_db()
        return {"comment": comment_schema.dump(comment)}, 201
    
    def get(cls, id:int)->List["CommentModel"]:
        
        return {"comments": comment_list.dump(CommentModel.query.filter_by(portfolio_id=id))}, 200
    
    
    @jwt_required()
    def delete(cls, id:int)->"None":
       
        comment=CommentModel.find(id=id)
      
        
        comment.delete_from_db()
        return {"message":"deleted"}, 200
    
    
    
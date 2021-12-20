from sqlalchemy.orm import lazyload
from db import db
from typing import List
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)



class PortfolioModel(db.Model):
    __tablename__="portfolios"
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80), nullable=False)
    description= db.Column(db.String(1000), nullable=False)
    likes=db.relationship("LikeModel", lazy=True)
    dislikes=db.relationship("DislikeModel", lazy=True)
    comments=db.relationship("CommentModel", lazy=True)
    background_image1= db.Column(db.String(500), nullable=False)
    tech_stack_logos1= db.Column(db.String(500), nullable=False)
    tech_stack_logos2= db.Column(db.String(500), nullable=False)
    tech_stack_logos3= db.Column(db.String(500), nullable=False)
    
    
    
    @classmethod
    def find_by_title(cls, title: str) -> "PortfolioModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "PortfolioModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_all(cls) -> List["PortfolioModel"]:
        return cls.query.all()
    

     

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    
    
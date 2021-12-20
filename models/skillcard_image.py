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

from models.skillcard import SkillCardModel

class SkillCardImage(db.Model):
    __tablename__="skillcard_images"
    id=db.Column(db.Integer, primary_key=True)

 
    
    
    
    
    @classmethod
    def find_by_title(cls, title: str) -> "SkillCardModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "SkillCardModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_all(cls) -> List["SkillCardModel"]:
        return cls.query.all()
    

     

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    
    
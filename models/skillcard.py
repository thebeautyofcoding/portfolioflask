from sqlalchemy.orm import lazyload
from db import db
from typing import List




class SkillCardModel(db.Model):
    __tablename__="skillcards"
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(150), nullable=False)
    small_description=db.Column(db.String(150), nullable=False)
    description= db.Column(db.String(1000), nullable=False)
    background_image1=db.Column(db.String(500), nullable=True)
    
    tech_stack_logos1=db.Column(db.String(500), nullable=True)
    tech_stack_logos2=db.Column(db.String(500), nullable=True)
    tech_stack_logos3=db.Column(db.String(500), nullable=True)
    
    
 
    
    
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
    
    
    
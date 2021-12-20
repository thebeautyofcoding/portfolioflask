from db import db
from typing import List

class UserModel(db.Model):
    __tablename__="users"
    
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), nullable=True, unique=True)
    password=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(80), nullable=False)
    likes=db.relationship("LikeModel",  lazy=True)
    comments=db.relationship("CommentModel", back_populates="user", lazy=True)
    dislikes=db.relationship("DislikeModel",  lazy=True)
    is_admin=db.Column(db.Boolean, default=False)
    
    
    def __init__(self, username, password, email):
        self.username=username
        self.password=password
        self.email=email
        
    
    @classmethod
    def find_by_email(cls, email:str)->"UserModel":
      
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_username(cls, username) -> "UserModel":
        return cls.query.filter_by(username=username).first()
    
    def save_to_db(self)->None:
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self)->None:
        db.session.delete()
        db.session.commit()
    
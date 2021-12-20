from db import db
from typing import List

class CommentModel(db.Model):
    __tablename__="comments"
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(1000), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    user=db.relationship("UserModel",lazy=True)
    portfolio_id=db.Column(db.Integer, db.ForeignKey('portfolios.id'))

    
    
    # @classmethod
    # def find_by_user_id(cls, title: str) -> "CommentModel":
    #     return cls.query.filter_by(title=title).first()

    @classmethod
    def find(cls, id:int) -> "CommentModel":
        
        
        return cls.query.filter_by(id=id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_all(cls,user_id:int) -> List["CommentModel"]:
        return cls.query.filter_by(user_id=user_id)
    
    
   
    
    
    
    
        

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
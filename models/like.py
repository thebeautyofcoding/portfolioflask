from db import db
from typing import List

class LikeModel(db.Model):
    __tablename__="likes"
    
    id=db.Column(db.Integer, primary_key=True)
    portfolio_id=db.Column(db.Integer, db.ForeignKey('portfolios.id'), unique=False)
    
    portfolio=db.relationship("PortfolioModel", back_populates="likes",lazy=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), unique=False)
    user=db.relationship("UserModel", back_populates="likes",lazy=True)
    portfolio=db.relationship("PortfolioModel", back_populates="likes", lazy=True)
    
    
    
    @classmethod
    def find_by_user_id(cls, title: str) -> "LikeModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_username(cls, _id: int) -> "LikeModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_all(cls) -> List["LikeModel"]:
        return cls.query.all()
    
    
    
    
        

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
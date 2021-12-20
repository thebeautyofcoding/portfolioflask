from ma import ma
from marshmallow import Schema, fields, validate, post_load
from  models.portfolio import PortfolioModel
from models.user import UserModel
from models.comment import CommentModel
from models.like  import LikeModel
from werkzeug.datastructures import FileStorage

from models.dislike import DislikeModel
from models.skillcard import SkillCardModel

class PortfolioSchema(ma.SQLAlchemyAutoSchema):
    likes=ma.Nested("LikeSchema", many=True)
    dislikes=ma.Nested("DislikeSchema", many=True)
    comments=ma.Nested("CommentSchema", many=True)
    class Meta:
        model = PortfolioModel
        load_instance = True
        dump_only=("id", "user_id", "portfolio_id")
        include_fk = True
        
class UserSchema(Schema):
    # likes=fields.Nested("LikeSchema", many=True)
    # dislikes=fields.Nested("DislikeSchema", many=True)
    username=fields.String(validate=validate.Length(min=3, max=30, error="The username must be between 3 and 30 characters"))
    email=fields.String(validate=validate.Email())
    password=fields.String(validate=validate.Length(min=3, max=30, error="The email must be between 3 and 30 characters"))
    
    @post_load
    def create_person(self, data, **kwargs):
        return UserModel(**data)

    
        
class LikeSchema(ma.SQLAlchemyAutoSchema):
    # portfolio=ma.Nested("PortfolioSchema", many=False)
    # user=ma.Nested("UserSchema", many=False)
    class Meta:
        model = LikeModel
        load_instance = True
        include_fk = True
        

class DislikeSchema(ma.SQLAlchemyAutoSchema):
    # portfolio=ma.Nested("PortfolioSchema", many=False)
    # user=ma.Nested("UserSchema", many=False)
    class Meta:
        model = DislikeModel
        load_instance = True
        include_fk = True
        
class CommentSchema(ma.SQLAlchemyAutoSchema):
    user=ma.Nested("UserSchema", many=False)
    portfolio=ma.Nested("PortfolioSchema", many=False)
    class Meta:
        model = CommentModel
        load_instance = True
  
        include_fk = True
        
        
class SkillCardSchema(ma.SQLAlchemyAutoSchema):
    # skillcard_images=ma.Nested("SkillCardSchema", many=True)
    # title=fields.String(validate=validate.Length(required=True))
    # description=fields.String(validate=validate.Length(required=True))
    class Meta:
        model = SkillCardModel
        load_instance = True
  
        include_fk = True
     
class FileStorageField(fields.Field):
    default_error_messages={
        "invalid":"Not a valid image."
    }
    def _deserialize(self, value, attr, data, **kwargs)->FileStorage:
        if value is None:
            return None
        if not isinstance(value, FileStorage):
            print('KEIN FOTO')
            
        return value
            
        
class ImageSchema(ma.SQLAlchemyAutoSchema):
    portfolio=ma.Nested("PortfolioSchema", many=False)
    tech_stack_logos1=FileStorageField(required=False)
    tech_stack_logos2=FileStorageField(required=False)
    tech_stack_logos3=FileStorageField(required=False)
    tech_stack_logos4=FileStorageField(required=False)
    background_image1=FileStorageField(required=False)
    

class SkillCardImageSchema(ma.SQLAlchemyAutoSchema):
    portfolio=ma.Nested("SkillCardSchema", many=False)
    background_image1=FileStorageField(required=False)

    tech_stack_logos1=FileStorageField(required=False)
    tech_stack_logos2=FileStorageField(required=False)
    tech_stack_logos3=FileStorageField(required=False)
  
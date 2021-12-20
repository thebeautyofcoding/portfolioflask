from pathlib import Path
from typing import Dict
from flask.sessions import NullSession
from flask_restful import Resource
from flask import json, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)



from models.skillcard import SkillCardModel

from schemas.schemas import SkillCardSchema


skillcard_schema= SkillCardSchema()
skill_list=SkillCardSchema(many=True)
class SkillCard(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
     
        form_data=request.form
        
        title=form_data["title"]
        description=form_data["description"]
        
        small_description=form_data["small_description"]
        data= dict()
       
        data["title"]=title
        data["description"]=description
        data['small_description']=small_description
        print(request.files)
        try:
            import libs.image_helper
            
           
           
            folder_background1= f"skillcard_{data['title'].replace(' ', '_')}"+"_background1"
            folder_background2= f"skillcard_{data['title'].replace(' ', '_')}"+"_background2"
            folder_logos1= f"skillcard_{data['title'].replace(' ', '_')}"+"_logos1"
            folder_logos2= f"skillcard_{data['title'].replace(' ', '_')}"+"_logos2"
            folder_logos3= f"skillcard_{data['title'].replace(' ', '_')}"+"_logos3"
            folder_logos4= f"skillcard_{data['title'].replace(' ', '_')}"+"_logos4"
            folder_logos5= f"skillcard_{data['title'].replace(' ', '_')}"+"_logos5"
            
            # folder_list.extend([folder_background1, folder_background2, folder_logos1, folder_logos2, folder_logos3, folder_logos4, folder_logos5])
      
            
            if   request.files["background_image1"]:
                background1=libs.image_helper.save_image(request.files["background_image1"], folder=folder_background1)
                path= '\\static\\images\\'+background1
                data["background_image1"]=path

      
                
            if   request.files["tech_stack_logos1"]:
                logos1=libs.image_helper.save_image(request.files["tech_stack_logos1"], folder=folder_logos1)
                path= '\\static\\images\\'+logos1
                data["tech_stack_logos1"]=path
            
                
            if   request.files["tech_stack_logos2"]:
                logos2=libs.image_helper.save_image(request.files["tech_stack_logos2"], folder=folder_logos2)
                path= '\\static\\images\\'+logos2
                data["tech_stack_logos2"]=path

            
            if   request.files["tech_stack_logos3"]:
                
                logos3=libs.image_helper.save_image(request.files["tech_stack_logos3"], folder=folder_logos3)
                path= '\\static\\images\\'+logos3
                data["tech_stack_logos3"]=path
            
       
            
           
            
           
            
           
            
            skillcard= skillcard_schema.load(data)
            print(skillcard)
            
            portfolio_db= SkillCardModel.find_by_title(skillcard.title)
            if(portfolio_db):
                return {"message":"skillcard entry with same title already existent"}, 400
           
            
            print('HIERNOCH')
            skillcard.save_to_db()
            return {"message":f"Images saved"}, 201
            
        except Exception as e:
            print(e)
            return {"message": "Image was not uploaded"}, 400

    def get(cls):
        return {"skills": skill_list.dump(SkillCardModel.find_all())}, 200          
        
        
        
        
    
    
    
    
    
    
        
# class GetPortfolio(Resource):  
#     @classmethod
#     def get(cls, id):
#         skillcard= PortfolioModel.find_by_id(id)
     
#         if skillcard:
#             return {"skillcard": skillcard_schema.dump(skillcard)}, 200
        
#         return {"message": "not found"}, 404
        
        
# class PutPortfolio(Resource):
#     @jwt_required()
#     def put(cls, id):
        
#         skillcard=PortfolioModel.find_by_id(id)
#         portfolio_json=request.get_json()
#         print(portfolio_json)
#         if skillcard:
           
#             skillcard.title=portfolio_json['title']
#             skillcard.description=portfolio_json['description']
            
#             skillcard.save_to_db()
#             return {"updated_portfolio": skillcard_schema.dump(skillcard)}, 200
#         portfolio_to_update=skillcard_schema.load(portfolio_json)
#         portfolio_to_update.save_to_db()

#         return {"message":f"new skillcard with title {portfolio_to_update.title} created"}
    
    
# class DeletePortfolio(Resource):
    
#     def delete(cls, id):
#         skillcard=PortfolioModel.find_by_id(id)
#         if skillcard:
#             skillcard.delete_from_db()
#             return {"message":f"skillcard with id {skillcard.id}  deleted"}
#         return {"message":f"skillcard with id {id} not found, nothing to delete"}
 
 
# class PortfolioList(Resource):
        
    
    
    
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

from schemas.schemas import PortfolioSchema
from models.portfolio import PortfolioModel
from flask_jwt_extended import (
    jwt_required,
)

from schemas.schemas import ImageSchema

portfolio_schema=PortfolioSchema()
portfolio_list=PortfolioSchema(many=True)
image_schema= ImageSchema()
class Portfolio(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        form_data=request.form
     
        title=form_data["title"]
        description=form_data["description"]
        
        data= dict()
        data["title"]=title
        data["description"]=description
     
       
        try:
            import libs.image_helper
            
           
            
            folder_background1= f"portfolio_{data['title'].replace(' ', '_')}"+"_background1"
            folder_background2= f"portfolio_{data['title'].replace(' ', '_')}"+"_background2"
            folder_logos1= f"portfolio_{data['title'].replace(' ', '_')}"+"_logos1"
            folder_logos2= f"portfolio_{data['title'].replace(' ', '_')}"+"_logos2"
            folder_logos3= f"portfolio_{data['title'].replace(' ', '_')}"+"_logos3"
            folder_logos4= f"portfolio_{data['title'].replace(' ', '_')}"+"_logos4"
            folder_logos5= f"portfolio_{data['title'].replace(' ', '_')}"+"_logos5"
            
            # folder_list.extend([folder_background1, folder_background2, folder_logos1, folder_logos2, folder_logos3, folder_logos4, folder_logos5])
            
            
            if   request.files["background_image1"]:
                
                background1=libs.image_helper.save_image(request.files["background_image1"], folder=folder_background1)
                print(background1)
                path= '\\static\\images\\'+background1
                data["background_image1"]=path
                print('HIERR')
            # if   request.files["background_image2"]:
            #     background2=libs.image_helper.save_image(request.files["background_image2"], folder=folder_background2)
            #     path= '\\static\\images\\'+background2
            #     data["background_image2"]=path
               
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
            
          
            
           
            
           
            
           
            
            portfolio= portfolio_schema.load(data)
            print(portfolio)
          
            portfolio_db= PortfolioModel.find_by_title(portfolio.title)
            if(portfolio_db):
                return {"message":"skillcard entry with same title already existent"}, 400
           
            
            print('HIERNOCH')
            portfolio.save_to_db()
            return {"message":f"Images saved"}, 201
            
        except Exception as e:
            print(e)
            return {"message": "Image was not uploaded"}, 400

    def get(cls):
        return {"portfolios": portfolio_list.dump(PortfolioModel.find_all())}, 200          
        
        
        
        
        
        
    
    
    
    
    
    
        
class GetPortfolio(Resource):  
    @classmethod
    def get(cls, id):
        portfolio= PortfolioModel.find_by_id(id)
     
        if portfolio:
            return {"portfolio": portfolio_schema.dump(portfolio)}, 200
        
        return {"message": "not found"}, 404
        
        
class PutPortfolio(Resource):
    @jwt_required()
    def put(cls, id):
        
        portfolio=PortfolioModel.find_by_id(id)
        portfolio_json=request.get_json()
        print(portfolio_json)
        if portfolio:
           
            portfolio.title=portfolio_json['title']
            portfolio.description=portfolio_json['description']
            
            portfolio.save_to_db()
            return {"updated_portfolio": portfolio_schema.dump(portfolio)}, 200
        portfolio_to_update=portfolio_schema.load(portfolio_json)
        portfolio_to_update.save_to_db()

        return {"message":f"new portfolio with title {portfolio_to_update.title} created"}
    
    
class DeletePortfolio(Resource):
    
    def delete(cls, id):
        portfolio=PortfolioModel.find_by_id(id)
        if portfolio:
            portfolio.delete_from_db()
            return {"message":f"portfolio with id {portfolio.id}  deleted"}
        return {"message":f"portfolio with id {id} not found, nothing to delete"}
 
 
class PortfolioList(Resource):
    def get(cls):
        return {"portfolios": portfolio_list.dump(PortfolioModel.find_all())}, 200       
    
    
    
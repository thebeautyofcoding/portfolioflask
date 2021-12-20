from sqlalchemy.orm import session
from flask_restful import Resource
from flask import request
from sqlalchemy import select
from db import db
import smtplib 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class Email(Resource):
    @classmethod

    def post(cls):
        message = MIMEMultipart()
        data=request.get_json()
     
        message['From'] = data['email']
        message['To'] = "bloatloard69@gmail.com"
        message['Subject']=data['subject']
       
        message_content=f"The email has been sent FROM: {data['email']};  \n MESSAGE: {data['message']} "
        message.attach(MIMEText(message_content, 'plain'))
        text = message.as_string()
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        
        server.login("bloatloard69@gmail.com", "Gopro123")
        server.sendmail(data['email'], 'bloatloard69@gmail.com',text )
        del data
        server.quit()
        return {"message":'Sent'}, 200
        
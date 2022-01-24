from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Mail:
    def __init__( self , data ):
        self.id = data['id']
        self.mail = data['mail']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO mails ( mail , created_at, updated_at ) VALUES ( %(mail)s , NOW() , NOW() );"
        return connectToMySQL('mail_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mails;"
        results = connectToMySQL('mail_schema').query_db(query)
        mails = []
        for mail in results:
            mails.append( cls(mail) )
        return mails

    @staticmethod
    def validate_mail(mail):
      is_valid = True 
      if not EMAIL_REGEX.match(mail['mail']):
        flash("Invalid email address!")
        is_valid = False
      return is_valid

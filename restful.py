from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from create_tables import create_sqlite_db
from db import db

# from item import Item, ItemList
from resources.item_db import Item, ItemList

from security_sql import authenticate, identity

app = Flask(__name__)
app.config['PROPOGATE_EXCEPTIONS'] = True # To allow flask propogating exception even if debug is set to false on app
api = Api(app)
app.secret_key = 'jose'


jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

def app_run():
    create_sqlite_db()
    app.run(port=5050, debug=True)
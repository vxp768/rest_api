from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'
items = []

jwt = JWT(app, authenticate, identity)

class Item(Resource):
    @jwt_required()
    def get(self, name):
        #for item in items:
        #    if item['name'] == name:
        #        return item
        #return {'item': None}, 404  ## http code for obj not found = 404
        item = next(filter(lambda x: x['name'] == name, items), None)
        #return {'item': item}, 201 if item is not None else 404
        return {'item': item}, 201 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201 ## 201 return http code for create success


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

def app_run():
    app.run(port=5050, debug=True)
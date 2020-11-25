from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity

class Item(Resource):
    parser = reqparse.RequestParser()  ## to parse incoming req and make sure only required field is there
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank"
                        )

    @jwt_required()  ## can be put in front of all HTTP verbs
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

        #data = request.get_json()
        data = Item.parser.parse_args()

        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201 ## 201 return http code for create success

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items)) #update items list
        return {'message':'Item deleted'}

    def put(self, name):
        #data = request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}
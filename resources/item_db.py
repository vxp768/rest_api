from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()  ## to parse incoming req and make sure only required field is there
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank"
                        )

    @jwt_required()  ## can be put in front of all HTTP verbs
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with '{}' already exists.".format(name)}, 400 # something wrong with request
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.insert()
        except:
            return {"message": "An error occurred inseting the item"}, 500 # internal server error

        return item.json(), 201 ## 201 return http code for create success

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message':'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error occurred updating the item"}, 500
        return updated_item.json()

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


stores = [  # list of stores
    {      # dict for each store
        'name':'my store',
        'items': [ # list of items
            {     # dict for each item
                'name': 'my item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

#POST from server perspective is to receive data
#POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#POST /store/store_name/item  {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# GET /store/
@app.route('/store/')  #by default method is GET for any browser
def get_stores():
    return jsonify({'stores': stores}) #jsonify takes dict not list,
                                     #hence convert stores into dict with single entry

# GET /store/store_name
@app.route('/store/<string:name>')
def get_store(name):  #http://<IP:port>/store/some_name
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

# GET /store/store_name/item
@app.route('/store/<string:name>/item') # by default meethod is GET for any browser
def get_item_in_store(name):  #http://<IP:port>/store/some_name
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'item not found'})


def app_run():
    app.run(port=5050)
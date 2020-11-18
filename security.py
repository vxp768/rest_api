from user import User
from werkzeug.security import safe_str_cmp
# in-mem data base
'''
users  = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]
'''
#use objects insetad of dict
users = [
    User(1,'bob','asdf')
]
# index on user name
'''
username_mapping = { 'bob' :
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}
'''
username_mapping = {u.username: u for u in users}
username_id      = {u.id: u for u in users}
# index on user id
userid_mapping = { 1: {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

def authenticate(username, password):
    user = username_mapping.get(username, None) #use get instead of [] so as to give default value
    #if user and user.password == password
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload): ## payload is content of JWT token
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

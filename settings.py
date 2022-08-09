import json

file = open('config.json')
config = json.load(file)

# database
database = config['database'][0]

DATABASE_USER = database['user']
DATABASE_PASSWORD = database['password']
DATABASE_HOST = database['host']
DATABASE_PORT = database['port']
DATABASE_NAME = database['name']

# JWT
jwt = config['jwt']
JWT_PREFIX = jwt['jwt_prefix']
SECRET_KEY = jwt['secret_key']
ALGORITHM = jwt['algorithm']
ACCESS_TOKEN_EXPIRE_MINUTES = jwt['expired']

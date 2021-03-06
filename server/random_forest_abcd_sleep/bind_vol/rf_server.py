import rf_model.rf_inference as rfinf
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
import requests
import json

## Using code from https://github.com/narenaryan/Salary-API as starting template

app = Flask(__name__)
api = Api(app)

CORS(app, origins="*")

img_server='http://localhost:5050'
'''
# Test Classes: Use these to ensure server is working
class Hello_World(Resource):
    def get(self):
        # Return string Hello World
        return {'Hello':  'world!',
        'also': tmod.hello_world_mod()}

class Hello_World_internal(Resource):
    def get(self):
        # Return string Hello World
        r = requests.get(img_server + "/helloworld_private")
        print(r.text)
        json_res = r.json()
        return json_res

# Image-Only Classes
class cxr_only(Resource):
    def post(self):
        content = request.get_json(force=True)
        r = requests.post(img_server + "/json_image",json=content)
        print(r.text)
        json_res = r.json()
        return json_res
'''

class zero_rf_test(Resource):
    def get(self):
        zero_result = rfinf.zero_test()
        print('zero_result: ', zero_result)
        #zero_result = 12345
        #return 0
        return int(zero_result)

@app.route('/')
def index():
    return "Welcome to my Python Server" 

#api.add_resource(Hello_World, '/helloworld')
#api.add_resource(Hello_World_internal, '/helloworld_internal')
#api.add_resource(cxr_only, '/cxr')
api.add_resource(zero_rf_test, '/zero_rf_test')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='5002')


#print('Hello World')

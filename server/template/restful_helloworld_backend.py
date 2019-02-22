from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
import requests
import json
import user_def_utils.test_mod as tmod
import user_def_utils.image_utils as image_utils

## Using code from https://github.com/narenaryan/Salary-API as starting template

app = Flask(__name__)
api = Api(app)

#app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
#app.config['CORS_HEADERS'] = 'Content-Type

CORS(app, origins="*")

class Hello_World(Resource):
    def get(self):
        # Return string Hello World
        return {'Hello':  'world!',
        'also': tmod.hello_world_mod()}

class Hello_World_internal(Resource):
    def get(self):
        # Return string Hello World
        r = requests.get("http://localhost:5050/helloworld_private")
        print(r.text)
        json_res = r.json()
        return json_res

class Hey_You(Resource):
    def get(self, user_name):
        # Return string Hello World
        return {'Hello':  user_name}

class postJsonHandler_image(Resource):
    def post(self):
        print (request.is_json)
        #print (request.get_data())
        #print (request.get_json(force=True))
        content = request.get_json(force=True)
        #print (content['image'])
        im_obj = image_utils.base64_to_img(content['image'])
        im_obj_rot90 = image_utils.img_rot_90deg(im_obj)
        print(image_utils.img_to_disk(im_obj_rot90,'test'))
        im_base64_rot90 = image_utils.img_to_base64(im_obj_rot90)
        return {'message':'JSON posted',
        'original_image':content['image'],
        'return_image':im_base64_rot90}

class postJsonHandler(Resource):
    def post(self):
        '''
        Json used for testing==
        { 
            "device":"TemperatureSensor", 
            "value":"20", 
            "timestamp":"25/01/2017 10:10:05" 
        }
        '''
        print (request.is_json)
        print (request.get_data())
        print (request.get_json(force=True))
        #content = request.get_json()
        #print (content['device'])
        return 'JSON posted'

@app.route('/')
def index():
    return "Welcome to my Python Server" 

api.add_resource(Hello_World, '/helloworld')
api.add_resource(Hello_World_internal, '/helloworld_internal')
api.add_resource(postJsonHandler, '/json')
api.add_resource(postJsonHandler_image, '/json_image')
api.add_resource(Hey_You, '/hey/<string:user_name>')

if __name__ == '__main__':
     app.run(port='5002')

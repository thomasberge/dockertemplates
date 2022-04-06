from glob import glob
from flask import Flask, request, redirect, render_template, make_response, jsonify
from flask_restful import Resource, Api, reqparse
import uuid
import json
import os

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = False
app.secret_key = os.getenv('APP_SECRET_KEY')
api = Api(app)

class Root(Resource):
    def get(self):
        return "Up and running", 200

api.add_resource(Root, '/')
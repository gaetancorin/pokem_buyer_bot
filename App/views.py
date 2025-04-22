from flask import *
from flask_cors import CORS
import logging
# from App.utils import *
import App.utils as utils
import App.specific_functions as specific_functions

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
CORS(app)


@app.route('/test', methods=["GET"])
def test():
    return {'message': 'this is a test'}

@app.route('/test2', methods=["GET"])
def test2():
    name = specific_functions.get_full_name()
    return {'message': name}

@app.route('/test3', methods=["GET"])
def test3():
    name = "Pierre"
    name_uppercase = utils.change_uppercase(name)
    return {'message': name_uppercase}

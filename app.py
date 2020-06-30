import flask
from flask import jsonify
import accounts as Accounts

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello!'

@app.route('/accounts/<id>', methods=['GET'])
def getAccount(id):
    return jsonify(Accounts.getAccount(id))

app.run()

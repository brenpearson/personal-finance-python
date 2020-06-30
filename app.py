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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

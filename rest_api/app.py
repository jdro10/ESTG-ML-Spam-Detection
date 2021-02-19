from flask import Flask
from flask import request
from rest_api.controllers.controller import *

app = Flask(__name__)


@app.route('/')
def index():
    return index_test()


@app.route('/evaluateSpam', methods=['POST'])
def spam_or_not():
    data = request.data
    string_decoded = data.decode('UTF-8')

    return spam_or_not_spam(string_decoded)


if __name__ == "__main__":
    app.run(debug=True)

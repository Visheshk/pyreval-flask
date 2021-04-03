from flask import Flask
from flask import request
from test import testfn

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=['POST', 'GET'])
def test():
    error = None
    if request.method == 'POST':
        try:
            rf = dict(request.form)
            print(testfn(rf["answer"]))
            return "post return"
        except:
            return "failed post return"
    else:
        return "other queries return"

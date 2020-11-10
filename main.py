from flask import Flask
from resources.user import Users

app = Flask(__name__)

@app.route('/<int:userid>')
def hello_world(userid):
    return 'Hello, World id = {}',format(userid)

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/test')
def test():
    return 'Test Page'



if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='127.0.0.1', port=8000)
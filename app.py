from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! My name is Malvika. I am going to add Karan to this project'

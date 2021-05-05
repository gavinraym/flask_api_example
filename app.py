from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    name = request.args['name']
    return f"Your name is {name}"


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return f'{user}, you just posted!'
   else:
      return f'You just getted!'

app.run(host='localhost', port=8080, debug=True)
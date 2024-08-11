from flask import Flask, render_template

app=Flask(__name__)

 

@app.route('/home')

def home2():

    return "hello python"

@app.route('/greet/<name>')  

def greet(name):

    return f"Hello, {name}!"

@app.route('/add/<a>/<b>') 
def add(a,b):
     value = int(a)+int(b)
     return int(value)

 

 

if __name__=='__main__':

    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])

@app.route("/")
def hello():
    return "Hello, Flask API!"

@app.route("/add", methods=["GET"])
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(operation="add", result=a+b)

@app.route("/divide", methods=["GET"])
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    if b== 0:
        return jsonify(error="cannot devide by zero"), 400
    return jsonify(operation="divide", result=a/b)

@app.route("/calculate", methods = ["POST"])
def calculate():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    op = data.get("operation")
    
    if None in (a, b, op):
        return jsonify(error="missing input"), 400
    
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        return jsonify(error="invalid number"), 400
    
    if op =="substract":
       result = a-b
    elif op =="multiply":
       result = a*b
    else:
       return jsonify(error="invalid operation"), 400
   
    return jsonify(operation=op, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
from backend.server.app import app
from flask import jsonify, request
from backend.server.app.services import GPTService

@app.route('/')
def home():
    data = 'Hello World'
    return jsonify(data), 200

@app.route("/message", methods=["POST"])
def message():
    response = { "gptResponse" : "message received"} 
    
    return jsonify(response), 201

@app.route("/ask", methods=["POST"])
def ask():
    payload = request.get_json()
    responseMessage = GPTService.ReceiveResponse(payload["question"])

    response = { "gptResponse" : [responseMessage]} 
    return jsonify(response), 201
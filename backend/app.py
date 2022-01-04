"""
Project Name: YouTube Transcript Summarizer
YouTube Transcript Summarizer API
"""


from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/', methods=['GET'])
def respond():


    body = {}

    # Build Response
    data = {}
    data['message'] = "Success"
    data['id'] = "0"
    data['response'] = "Predicted Disease - X"

    body["data"] = data

    # Return the response in json format
    return buildResponse(body)


# Welcome message to our server
@app.route('/')
def index():

    body = {}
    body['message'] = "Success"
    body['data'] = "Welcome to Skin-Disease Prediction API."

    return buildResponse(body)


def buildResponse(body):

    # from flask import json, Response
    # res = Response(response=json.dumps(body), status=statusCode, mimetype="application/json")
    # res.headers["Content-Type"] = "application/json; charset=utf-8"
    # return res

    response = jsonify(body)
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)

# Deployment to Heroku Cloud.

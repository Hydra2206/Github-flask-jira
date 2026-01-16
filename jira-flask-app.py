#This flask app is used when someone comment /jira on github issues, using api call a jira ticket will be created for that issue
from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json


#creating flask app instance
app = Flask(__name__)         # mandatory to start writing flask app


@app.route("/CreateJIRA", methods = ['POST'])               #decorator used here before app to authenticate
def createJIRA():

    url = "https://mittu270318.atlassian.net/rest/api/3/issue"
    API_TOKEN = ""

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
    
        "issuetype": {
        "id": "10047"
        },
        "project": {
        "key": "GPH"
        },
        "summary": "My First Jira Ticket",
    },
    "update": {}
    } )

    #importing payload sending by github webhook about issue comments
    data = request.json

    comment_body = data["comment"]["body"]
    
    # Check if '/jira' exists anywhere in the comment (case-insensitive)
    if "/jira" not in comment_body.lower():
        return jsonify({"message": "To create a JIRA ticket, comment /jira"}), 200

    # Only runs if '/jira' is present
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return jsonify(response.json()), response.status_code

app.run('0.0.0.0')
from flask import Flask,request
import requests
from requests.auth import HTTPBasicAuth
import json

##creating a flask application instance
app = Flask("__name__")

@app.route("/createJIRA" , methods=['POST']) 
def create_jira():
    data = request.json


    login_value = data["issue"]["user"]["login"]
    content = data['comment']['body']
    comparevalue="/jira"
    summaryvalue = login_value + "Issue Settled."
    body_text = "The issue regarding "+ data["issue"]["body"] + " is solved."
    

    if content==comparevalue:


    
        url = ""

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
                    "text": body_text,
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "project": {
            "key": "RATU"
            },
            "issuetype": {
            "id": "10006"
            },
            "summary": summaryvalue ,
        },
        "update": {}
        } )

        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    

app.run('0.0.0.0')
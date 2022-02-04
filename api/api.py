import json
import requests
import os

es_auth = (os.environ['ES_USER'], os.environ['ES_PASSWORD'])
es_host = os.environ['ES_HOST']
es_index = os.environ['ES_INDEX']
es_type = os.environ['ES_TYPE']
url = es_host + '/' + es_index + '/' + es_type + '/_search'

def lambda_handler(event, context):
    query = {
        "query": {
            "simple_query_string" : {
                "query": event['queryStringParameters']['q'],
                "fields": ["title^5", "keywords^3", "description^3", "text"]
            }
        },
        "fields": ["title", "description"],
        "_source": False
    }

    headers = { "Content-Type": "application/json" }
    r = requests.post(url, auth=es_auth, headers=headers, data=json.dumps(query))

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False
    }
    response['body'] = r.text

    return response

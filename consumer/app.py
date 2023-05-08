import base64
import json

def lambda_handler(event, context):
    for record in event:
        data = json.loads(base64.b64decode(record['data']))
        print(record)
        print(data)

import json

def hello(event, context):
    name = event.get("queryStringParameters", {}).get("name", "Guest")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": f"Hola profe}!"})
    }

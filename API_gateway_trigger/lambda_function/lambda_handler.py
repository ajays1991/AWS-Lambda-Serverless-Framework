import config
import json
import requests

def handler(event, context):

    event_object = json.loads(event['body'])
    city = event_object["city"]

    response = requests.get(url = config.WEATHER_API_URL, params = {"q": city, "APPID": config.WEATHER_API_KEY})
    response_data = response.json()
    print(response_data)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
                    "report": response_data
        })
    }

if __name__ == "__main__":
    event = {
        "city": "london",
        "days": "4"
    }
    handler(event,{})

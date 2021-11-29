import config
import json
import pymysql

def get_mysql_connection():
    return pymysql.connect(
        host=config.RDS_HOST,
        user=config.RDS_USER,
        password=config.RDS_PASSWORD,
        db=config.RDS_DATABASE,
        charset=config.RDS_CHARSET,
        cursorclass=pymysql.cursors.DictCursor
    )

def handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    message_id = event['Records'][0]['Sns']['MessageId']
    event_object = json.loads(message.strip())
    
    sensor_data = {}
    sensor_data['tractor_id'] = event_object["tractor_id"]
    sensor_data['temprature'] = event_object["temprature"]
    sensor_data['humidity'] = event_object["humidity"]
    sensor_data['longitude'] = event_object["longitude"]
    sensor_data['latitude'] = event_object["latitude"]
    sensor_data['pressure'] = event_object["pressure"]
    sensor_data['torque'] = event_object["torque"]
    sensor_data['message_id'] = message_id
    
    if not sensor_data['tractor_id'] or not sensor_data['temprature'] or not sensor_data['humidity'] or not sensor_data['longitude'] or not sensor_data['latitude'] or not sensor_data['pressure'] or not sensor_data['torque']:
        return True

    mysql_connection = get_mysql_connection()

    with mysql_connection.cursor() as cursor:
        cursor.execute(
                "insert into sensor_data(tractor_id, temprature, humidity, longitude, latitude, pressure, torque,"
                " message_id) values (%(tractor_id)s, %(temprature)s, %(humidity)s,"
                " %(longitude)s, %(latitude)s, %(pressure)s, %(torque)s, %(message_id)s)",
                sensor_data)
        mysql_connection.commit()
        mysql_connection.close()
    return True
    

if __name__ == "__main__":
    event = {
        "Records": [{
            "Sns": {
                "Message": "{\"tractor_id\":1,\"temprature\":34,\"humidity\":100,\"longitude\":24.5,\"latitude\":34.6,\"pressure\":100,\"torque\":94}",
                "MessageId": "febcb5c3-dbcf-5284-9422-ec28d94992dc"
            }
        }]
    }
    lambda_function(event,{})

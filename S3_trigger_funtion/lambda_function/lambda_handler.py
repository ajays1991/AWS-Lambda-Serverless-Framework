import config
import boto3
from urllib.parse import unquote_plus
from PIL import Image
from io import BytesIO

def handler(event, context):
	if event:
		file_object = event["Records"][0]
		bucket_name = str(file_object["s3"]["bucket"]["name"])
		file_name = str(file_object["s3"]["object"]["key"])
		file_name = unquote_plus(file_name)
		resize_image(bucket_name, file_name)


def resize_image(bucket_name, file_name):
	size = 100, 100
	client = boto3.client('s3')
	resized_in_memory_file = BytesIO()

	file_byte_string = client.get_object(Bucket=bucket_name, Key=file_name)["Body"].read()
	image = Image.open(BytesIO(file_byte_string))
	image.thumbnail(size, Image.ANTIALIAS)
	image.save(resized_in_memory_file, format=image.format)
	resized_in_memory_file.seek(0)

	s3_upload_response = client.put_object(
		Body=resized_in_memory_file,
		Bucket=config.DESTINATION_BUCKET,
		Key="resized_" + file_name
	)
	print(s3_upload_response)

if __name__ == "__main__":
    event = {
        "Records": [{
            "s3": {
                "bucket": {
                	"name": "unmodified-images-bucket"
                },
                "object": {
                	"key": "test.png"
                }
            }
        }]
    }
    handler(event,{})

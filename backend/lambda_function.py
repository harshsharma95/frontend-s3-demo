import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = "s3-deploy-static-website"

def lambda_handler(event, context):
    try:
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event

        name = body.get('name')
        email = body.get('email')
        contact = body.get('contact')

        data = {
            "name": name,
            "email": email,
            "contact": contact,
            "timestamp": str(datetime.now())
        }

        # Unique file name
        file_name = f"contacts/{name}_{datetime.now().timestamp()}.json"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data),
            ContentType='application/json'
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Data stored successfully in S3 ✅"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

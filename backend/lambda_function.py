import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = "s3-deploy-static-website"

def lambda_handler(event, context):
    try:
        # Get data from API Gateway
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event

        name = body.get("name")
        email = body.get("email")
        contact = body.get("contact")

        # Prepare data
        data = {
            "name": name,
            "email": email,
            "contact": contact,
            "time": str(datetime.now())
        }

        # File name in S3
        file_name = f"contacts/{name}_{datetime.now().timestamp()}.json"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data),
            ContentType='application/json'
        )

        # ✅ Only return clean message
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Thanks for submitting"
            })
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error occurred"
            })
        }

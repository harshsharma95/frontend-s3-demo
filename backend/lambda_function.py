import json
import boto3

ses = boto3.client('ses', region_name='ap-south-1')

def lambda_handler(event, context):
    try:
        # Parse request
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event

        name = body.get('name', 'User')
        email = body.get('email', 'No Email')
        contact = body.get('contact', 'No Contact')

        # 🔥 Email details
        sender_email = "harshsharma952887@gmail.com"
        receiver_email = "harshsharma952887@gmail.com"

        subject = "New Contact Form Submission"

        message = f"""
You received a new contact form submission:

Name: {name}
Email: {email}
Contact: {contact}
"""

        # 🔥 Send Email via SES
        ses.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [receiver_email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': message
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                'message': f"Thanks {name}, your details submitted successfully!"
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({'error': str(e)})
        }

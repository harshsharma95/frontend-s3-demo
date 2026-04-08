import json

def lambda_handler(event, context):
    try:
        # Handle both API Gateway and direct test
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event

        name = body.get('name', 'User')
        email = body.get('email', 'No Email')
        contact = body.get('contact', 'No Contact')

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                'message': f"Thanks {name}, we will reach you at {email} or call {contact}"
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

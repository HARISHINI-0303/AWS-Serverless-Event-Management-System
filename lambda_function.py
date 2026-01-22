import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Events')

def lambda_handler(event, context):
    body = event.get('body')

    if body:
        if isinstance(body, str):
            body = json.loads(body)
    else:
        body = event

    event_name = body.get('event_name')

    event_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'event_id': event_id,
            'event_name': event_name
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'Event created successfully',
            'event_id': event_id
        })
    }

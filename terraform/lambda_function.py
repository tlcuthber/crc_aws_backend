import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('counter')

def lambda_handler(event, context):
    # Get visitor counter data from DyanmoDb database
    response = table.get_item(
        Key={
            'counterName': 'resumeVisitorCounter'
        })
        
    # Create counterValue variable and set to value of visitorCounter
    counterValue=response['Item']['visitorCounter']
    
    # Increment counterValue by 1
    counterValue += 1
    
    # Update DynamoDB database with new value
    response = table.update_item(
            Key={
                'counterName': 'resumeVisitorCounter'
            },
            UpdateExpression="set visitorCounter = :updatedCount",
            ExpressionAttributeValues={
                ':updatedCount': counterValue
            }
        )
    
    return counterValue 
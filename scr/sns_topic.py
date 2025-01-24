import json
import boto3

sns_client = boto3.client("sns")
SNS_TOPIC_ARN = "arn:aws:sns:your-region:your-account-id:EC2StateChangeTopic"

def lambda_handler(event, context):
    message = f"EC2 Instance State Change: {json.dumps(event, indent=2)}"
    
    # Send SNS notification
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="EC2 Instance State Change Alert"
    )
    
    print("SNS Notification Sent:", response)
    
    return {
        "statusCode": 200,
        "body": "Event processed and SNS notification sent!"
    }

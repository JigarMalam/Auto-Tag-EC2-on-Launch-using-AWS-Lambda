import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Extract instance ID from CloudTrail event
    try:
        instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
    except Exception as e:
        print("Error getting instance ID:", e)
        return

    
    date_tag = datetime.utcnow().strftime('%Y-%m-%d')

    try:
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'LaunchDate', 'Value': date_tag},
                {'Key': 'Project', 'Value': 'JigarAutoTag'},
                {'Key': 'Auto', 'Value': 'ThisTagISbyJigar'}, 
            ]
        )
        print(f"Successfully tagged instance {instance_id}")
    except Exception as e:
        print("Failed to tag instance:", e)

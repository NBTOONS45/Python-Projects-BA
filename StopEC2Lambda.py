
import boto3

region ='us-east-1'

instances = ['i-0325521c39870a409', 'i-0926d9b632814d3cb', 'i-04991f674eedc55af']

def lambda_handler(event,context):
    
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print( 'stopped your instances: ' +str(instances))
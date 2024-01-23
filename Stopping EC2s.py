# Import the Boto3 library, which provides an interface to AWS services.

import boto3 

# Initialize an EC2 client using the Boto3 libarary.
ec2 = boto3.client('ec2')

# Use 'stop_instances' method of the EC2 client to stop specified instances. 
response = ec2.stop_instances(
    InstanceIds=['i-0325521c39870a409', 'i-0926d9b632814d3cb', 'i-04991f674eedc55af'],)

# Print the response recieved after attempting to stop the instances. 
print(response)


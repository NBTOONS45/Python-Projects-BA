# Import the Boto3 library, which provides an interface to AWS services
import boto3 

# Define a function to retrieve and print VPC information based on filters
def get_vpc_information(client, filter=[]):
    # Use the describe_vpcs method of the provided client with the specified filters
    response = client.describe_vpcs(Filters=filter)
    
    # Iterate through the VPCs in the response and print relevant information
    for vpc in response["Vpcs"]:
        # Print VPC ID, CIDR block, and check if it's the default VPC
        print(vpc['VpcId'], vpc["CidrBlock"], vpc.get("IsDefault", "N/A"))

# Define a function to retrieve and print VPC names based on filters
def get_vpc_name(client, filter=[]):
    # Use the describe_vpcs method of the provided client with the specified filters
    response = client.describe_vpcs(Filters=filter)
    
    # Iterate through the VPCs in the response
    for vpc in response["Vpcs"]:
        # Check if the VPC has Tags
        if "Tags" in vpc:
            # Iterate through the tags of the VPC
            for tag in vpc["Tags"]:
                # Check if the tag key is "Name" and print its value
                if tag['Key'] == 'Name':
                    print(tag["Value"])

# Initialize an EC2 client using the Boto3 library
ec2 = boto3.client('ec2') 

# Call the defined functions with the EC2 client to retrieve and print VPC information
get_vpc_information(ec2)
get_vpc_name(ec2)


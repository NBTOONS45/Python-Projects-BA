# Import the Boto3 library, which provides an interface to AWS services
import boto3

# Initialize an S3 client using the Boto3 library
s3 = boto3.client('s3')

# Generate a pre-signed URL for the 'get_object' operation
# Params:
#   - 'Bucket': The name of the S3 bucket from which you want to get the object
#   - 'Key': The key (path) of the object you want to access within the bucket
#   - 'ExpiresIn': The expiration time for the pre-signed URL in seconds (600 seconds or 10 minutes in this case)
response = s3.generate_presigned_url('get_object', Params={'Bucket': "ba-boto3-bucket", 'Key': "boto3.html"}, ExpiresIn=600)

# Print the generated pre-signed URL to the console
print(response)

#BA
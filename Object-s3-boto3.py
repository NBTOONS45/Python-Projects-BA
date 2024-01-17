import boto3

# Initialize the S3 client

s3 = boto3.client('s3')

# Specify your bucket name and file key

bucket_name = 'ba-boto3-bucket'
file_key = 'boto3.html'

# Open the file to be uploaded

with open("boto3.html", 'rb' ) as f:
    
# Upload the file to S3
    s3.put_object(Bucket="ba-boto3-bucket", Key="boto3.html", Body=f)
   
import boto3

s3 = boto3.client('s3')


response = s3.create_bucket(
  Bucket = 'ba-boto3-bucket'
)
print('response')
print('Bucket')

# created a bucket using boto3 python.
#BA
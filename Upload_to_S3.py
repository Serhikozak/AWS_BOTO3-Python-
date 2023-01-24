import boto3

# session = boto3.Session(
#     aws_access_key_id='AWS_ACCESS_KEY_ID',
#     aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
# )
s3 = boto3.resource('s3')
# Filename - File to upload
# Bucket - Bucket to upload to (the top level directory under AWS S3)
# Key - S3 object name (can contain subdirectories). If not specified then file_name is used
s3.meta.client.upload_file(Filename='/Users/army/Military/users.csv', Bucket='skozakov', Key='users.csv')

  

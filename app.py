import boto3

s3 = boto3.client("s3")

bucket_name = "amrit-demo-bucket-123456"

try:
    s3.create_bucket(Bucket=bucket_name)

    print("Bucket Created")

except Exception as e:
    print(e)
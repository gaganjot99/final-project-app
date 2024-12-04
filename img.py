import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import logging

def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"downloads/bg.jpg"
    s3.Bucket(bucket).download_file(file_name, output)

    return output
    
download_file(os.environ.get('IMAGE_NAME'), "imagestemps")
import os

from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = os.getenv('AWS_BUCKET_NAME')
    location = 'media'
    file_overwrite = True

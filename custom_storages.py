"""
Custom storage backends for AWS S3
"""
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """
    Custom storage for media files (uploaded images)
    Stores files in 'media/' folder within S3 bucket
    """
    location = 'media'
    file_overwrite = False


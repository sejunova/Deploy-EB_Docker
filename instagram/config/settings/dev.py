from .base import *

config_secret_dev = json.loads(open(CONFIG_SECRET_DEV).read())

DATABASES = config_secret_dev['django']['databases']



AWS_ACCESS_KEY_ID = config_secret_common['aws']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret_common['aws']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config_secret_common['aws']['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME_= 'ap-northeast-2'

# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

#S3 static directory customize
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
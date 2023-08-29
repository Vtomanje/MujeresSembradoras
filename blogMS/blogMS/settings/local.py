from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1689937619067",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "--------------------/*"
        }
    ]
}

AWS_ACCESS_KEY_ID = get_secret('KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'msembradoras'
AWS_S3_REGION_NAME = 'us-east-1' # Por ejemplo, 'us-east-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False

# Configuración para almacenar archivos estáticos y multimedia
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, 'static')
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, 'media')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




# ckeditor settings
CKEDITOR_UPLOAD_PATH = '/uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS ={
    'default': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['NumberedList','BulletedList'],
            ['Indent','Outdent'],
            ['Maximize'],
        ],
        'extraPlugins': 'justify,liststyle,indent',
    }
}


# SMTP configuarcion
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.office365.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = get_secret('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
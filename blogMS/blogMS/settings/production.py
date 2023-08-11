from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["mujeressembradoras-b38489007cc4.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'ec2-3-234-204-26.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


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
"""EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.office365.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = get_secret('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')"""
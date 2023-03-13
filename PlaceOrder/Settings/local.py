from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'PlaceOrder' ,
        'CLIENT' :  {
            'host': 'mongodb+srv://majimenezh:4ZdwP8dn7uShM0af@microservicio-pagos.w8bjvui.mongodb.net/?retryWrites=true&w=majority'
        }
    }
}


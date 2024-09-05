# Registration

This is a Django application which start the customization of the User model of Django. 

## Installation

First at all, it must be added to the INSTALLED_APP in the file named 'settings.py' of the project. It must be the placed 
before 'django.contrib.auth' and 'django.contrib.admin' because the migrations this app have to be done before those of 'django.contrib.auth'.

```
INSTALLED_APPS = [
    ...
    'registrations',
    'django.contrib.admin',
    'django.contrib.auth',
    ...
] 
```

Always in settings.py, you must indicate the model utilized like user model.

```
AUTH_USER_MODEL = "registrations.CustomUser"
```








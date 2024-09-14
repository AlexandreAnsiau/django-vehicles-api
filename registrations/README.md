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

The host used must be indicated in the settings whith the HOST variable. For example:

```
HOST = "127.0.0.1"
```

The project name used must be indicated in the settings whith the PROJECT_NAME variable. It will be use for the subjects of the mails. For example:

```
PROJECT_NAME = "Project Name"
```

The lifetime of the reset password tokens spectify in the settings with the RESET_PASSWORD_TOKEN_VALIDITY variable. Its value must be a datetime.timedelta object. (Indicate the default value)


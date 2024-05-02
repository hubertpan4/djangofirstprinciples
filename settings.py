from pathlib import Path

"""
Migrating settings configuration from primary blogmaker_lite.py into this file

Helps to replace the following code:
```python
settings.configure(
    ROOT_URLCONF = __name__, # tells django where to find the urls it should listen to, in this case it is this file
    DEBUG=True, # tells django to show debugging info if something goes wrong 
    SECRET_KEY="my-secret-key",
    TEMPLATES = [ # adding config for django templates
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [Path(__file__).parent / "templates"]
        }
    ]
)
```

Apparently running `python manage.py migrate` is impt whenever database related changes occur.

"""

ROOT_URLCONF="blogmaker_lite" # instead of __name__ we now point to the main blogmaker_lite.py file

DEBUG=True 

SECRET_KEY="my-secret-key"

TEMPLATES=[
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(__file__).parent / "templates"],
        # adding stuff for admin stuff
        "APP_DIRS": True, # tells django to also look for templates in the app specific 'templates' directories as well.
        'OPTIONS': {
            'context_processors': [ # processors are required to allow for auth on admin pages
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

# Tells Django which "apps" have been isntalled to this project
# each app corresponds to a folder, which also tells Django to where to look for each app's stuff
INSTALLED_APPS = [
    "blogs",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles"
    ]

# Middleware allows you to process requests at different points in the request-response cycle.
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Django database configuration
# in this case we tell Django to use SQLite by default backed with a single db.sqlite3 file
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).parent / 'db.sqlite3'
    }
}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
STATIC_URL = "static/"
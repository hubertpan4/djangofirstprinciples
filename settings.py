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

"""

ROOT_URLCONF="blogmaker_lite" # instead of __name__ we now point to the main blogmaker_lite.py file

DEBUG=True 

SECRET_KEY="my-secret-key"

TEMPLATES=[
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(__file__).parent / "templates"],
    }
]

# Tells Django which "apps" ahve been isntalled to this project
# each app corresponds to a folder, which also tells Django to where to look for each app's stuff
INSTALLED_APPS = ["blogs"]

# Django database configuration
# in this case we tell Django to use SQLite by default backed with a single db.sqlite3 file
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).parent / 'db.sqlite3'
    }
}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
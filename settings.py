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
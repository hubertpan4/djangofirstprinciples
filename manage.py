import os 
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    # load settings from external settings.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    #django.setup() # no longer required b/c execute_from_command_line() is run before other setup code and handles the same stuff
    execute_from_command_line()
    # run this file with the command `python manage.py runserver`
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from pathlib import Path
import os 
import django 
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.shortcuts import render

# load settings from external settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

def index(request):
    """
    switch the index page over to using the template setup
    """
    return render(request=request, template_name="index.html")

def bob(request):
    title = "Blog title"
    desc = "Blog seed!"
    page_text = f"<h1>{title}</h1>"
    page_text += f"<p>{desc}</p>"
    return HttpResponse(page_text)

urlpatterns = [
    path("", index),
    path("bob", bob)
]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()
    # run this file with the command `python blogmaker_lite.py runserver`
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line

settings.configure(
    ROOT_URLCONF = __name__, # tells django where to find the urls it should listen to, in this case it is this file
    DEBUG=True, # tells django to show debugging info if something goes wrong 
    SECRET_KEY="my-secret-key"
)

def index(request):
    return HttpResponse("BlogMaker Lite")

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
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.shortcuts import render
# import admin console code and Blog model 
from django.contrib import admin 
from blogs.models import Blog

# tells the admin console to manage the Blog model by registering it
admin.site.register(Blog)


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
    path("admin2/", admin.site.urls), # add the admin urls to the admin/ prefix path
    path("", index),
    path("bob", bob)
]

application = WSGIHandler()
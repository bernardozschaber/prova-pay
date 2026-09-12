from django.http import HttpResponse
from django.urls import path

app_name = "applicators"
urlpatterns = [path("", lambda r: HttpResponse("TODO"), name="list")]

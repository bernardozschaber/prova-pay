from django.http import HttpResponse
from django.urls import path

app_name = "catalog"
urlpatterns = [path("", lambda r: HttpResponse("TODO"), name="settings")]

from django.urls import path
from .views import listEvents

urlpatterns = [
    path("list/", listEvents, name="events"),
]

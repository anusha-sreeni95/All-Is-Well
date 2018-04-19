from django.conf.urls import url, include
from .views import CreateEventView

urlpatterns = [
  url("^$", CreateEventView.as_view(), name="createeventview")
]

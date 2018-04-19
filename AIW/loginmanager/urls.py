from django.conf.urls import url, include
from .views import LoginView

urlpatterns = [
  url("^$", LoginView.as_view(), name="loginview"),

]

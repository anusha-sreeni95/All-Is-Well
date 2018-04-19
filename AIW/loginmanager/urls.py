from django.conf.urls import url, include
from .views import LoginView
from .utils import remove_session

urlpatterns = [
  url("^$", LoginView.as_view(), name="loginview"),
  url("^logout$", remove_session, name="logoutview")
]

from django.conf.urls import url, include
from .views import SignUpView

urlpatterns = [
  url("^$", SignUpView.as_view(), name="signupview")
]

from django.conf.urls import url, include
from .views import HomePageView

urlpatterns = [
  url("^homapage$", HomePageView.as_view(), name="homepageview")
]

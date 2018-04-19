from django.conf.urls import url, include
from .views import ProfilePage

urlpatterns = [
  url("^(?P<token>.+)$", ProfilePage.as_view(), name="profilepage")
]

from django.conf.urls import url, include
from .views import DonationView

urlpatterns = [
  url("^$", DonationView.as_view(), name="donateview")
]

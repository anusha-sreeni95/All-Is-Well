from django.conf.urls import url
from .views import UpcomingEvents

urlpatterns = [
    url(r'^$', UpcomingEvents.as_view(), name='upcomingevents'),
]
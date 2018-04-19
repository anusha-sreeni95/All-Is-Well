from django.conf.urls import url, include
from .views import ScoreBoardView

urlpatterns = [
  url("^$", ScoreBoardView.as_view(), name="scoreboardview")
]

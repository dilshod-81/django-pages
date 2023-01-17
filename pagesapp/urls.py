from django.urls import path
from .views import HomePageView, AboutPageView, IndexPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("index/", IndexPageView.as_view(), name="index"),
]

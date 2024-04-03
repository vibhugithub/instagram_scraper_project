from django.urls import path, include
from instagram_scraper import views

app_name = "instagram_scraper"

urlpatterns = [
    path("get_insta/", views.get_insta, name="get_insta"),
]

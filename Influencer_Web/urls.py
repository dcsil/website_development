from django.urls import re_path
from Influencer_Web import views


urlpatterns = [
    re_path(r'^influencer$', views.influencerInfoApi),
    re_path(r'^influencer/([0-9]+)$', views.influencerInfoApi)
]
from django.urls import re_path
from app import views

urlpatterns = [
    re_path(r'^api/bill$', views.billApi),
    re_path(r'^api/bill/([0-9]+)$', views.billApi),

]
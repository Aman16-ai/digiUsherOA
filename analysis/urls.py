from django.contrib import admin
from django.urls import path,include
from .views import ReportAPIView
urlpatterns = [
    path('report',view=ReportAPIView.as_view())
]
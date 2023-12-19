from django.contrib import admin
from django.urls import path,include
from .routers import metricsRouter
urlpatterns = [
    path('metrics',include(metricsRouter.urls))
]
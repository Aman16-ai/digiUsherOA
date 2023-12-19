from rest_framework.routers import SimpleRouter
from .views import MetricViewSet
metricsRouter = SimpleRouter()
metricsRouter.register('',MetricViewSet)
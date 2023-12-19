from ..models import Metric
from rest_framework.exceptions import NotFound
from django.db.models import Q,Avg
class MetricsService:

    def create(self,data):
        try:
            metricObj = Metric(**data)
            metricObj.save()
            return metricObj
        except Exception as e:
            return APIException(detail=str(e))
        
    
    def get_average_mertics(self,startDate,endDate):
        metric = Metric.objects.filter(Q(timestamp__gte=startDate) & Q(timestamp__lte=endDate))
        if metric.exists():
            avg_ram = metric.aggregate(Avg('ram_consumed'))['ram_consumed__avg']
            avg_cpu = metric.aggregate(Avg('cpu'))['cpu__avg']
            avg_disk = metric.aggregate(Avg('disk_usage_percent'))['disk_usage_percent__avg']
            return {
                'ram_consumed':avg_ram,
                'cpu' : avg_cpu,
                'disk_usage_percent': avg_disk
            }
        else:
            raise NotFound(detail=("Not found"))

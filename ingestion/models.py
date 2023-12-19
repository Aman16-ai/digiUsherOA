from django.db import models

class Metric(models.Model):
    ram_consumed = models.IntegerField()
    cpu = models.IntegerField()
    disk_usage_percent = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

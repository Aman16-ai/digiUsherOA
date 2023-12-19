from ingestion.services.MetricsService import MetricsService
from django.utils import timezone
import datetime

class ReportService:

    def __init__(self) -> None:
        self.metricsService = MetricsService()
        self.present_date = timezone.now()
        self.start_date_day = self.present_date - datetime.timedelta(days=1)
        self.start_date_month = self.present_date - datetime.timedelta(days=30)

    
    def generate(self):
        day_avg_metrics = self.metricsService.get_average_mertics(startDate=self.start_date_day,endDate=self.present_date)

        month_avg_metrics = day_avg_metrics = self.metricsService.get_average_mertics(startDate=self.start_date_month,endDate=self.present_date)
        return {'day':day_avg_metrics,'month':month_avg_metrics}
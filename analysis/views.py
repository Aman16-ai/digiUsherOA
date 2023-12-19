from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.ReportService import ReportService
# Create your views here.

class ReportAPIView(APIView):

    def get(self,request):
        try:
            rs = ReportService()
            report = rs.generate()
            return Response(status=status.HTTP_200_OK,data={'status':status.HTTP_200_OK,'Response':report})
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'Error':"Internal server error"})

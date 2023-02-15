from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InfoSerializer
from rest_framework import status

# Create your views here.
class TestAPIView(APIView):
    def get(self, request):
        return Response('oke')

    def post(self, request):
        da = InfoSerializer(data = request.data)
        if not da.is_valid():
            return Response('bad request', status= status.HTTP_400_BAD_REQUEST)
        
        print(da.data['name'])
        
        return Response('Success', status= status.HTTP_200_OK)
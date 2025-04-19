from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer

@api_view(['POST'])
def shorten_url(request):
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Getting original URL
@api_view(['GET'])
def redirect_url(request, short_url):
    url_obj = ShortURL.objects.filter(short_url=short_url).first()
    if not url_obj:
        return Response({"error": "Short URL is required."},status=status.HTTP_400_BAD_REQUEST)
        
    url_obj.hit_count += 1
    url_obj.save()
    serializer = ShortURLSerializer(url_obj)
    serializer.pop('hit_count', None)
    serializer.pop('id', None)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


#Updating the URL
@api_view(['PUT'])
def update_url(request, short_url):
    url_obj = ShortURL.objects.filter(short_url=short_url).first()
    if not url_obj:
        return Response({"error": "Short URL is required."},status=status.HTTP_400_BAD_REQUEST)
        
    serializer = ShortURLSerializer(short_url, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_url(request, short_url):
    url_obj = ShortURL.objects.filter(short_url=short_url).first()
    if not url_obj:
        return Response({"error": "Short URL is required."},status=status.HTTP_400_BAD_REQUEST)
        
    url_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


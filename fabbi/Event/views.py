from django.http.response import Http404
from django.shortcuts import render
from rest_framework import pagination,viewsets,generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from User.models import User

from .models import Event
from .serializer import EventSerializer
from .paginator import EventPagination

# Create your views here.
class EventViewSet(viewsets.ViewSet, generics.ListAPIView,generics.CreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    # query_set = Event.objects.filter(is_archived = 0)
    serializer_class = EventSerializer
    pagination_class = EventPagination 
    # permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        events = Event.objects.filter(is_archived = 0)
        keyword = self.request.query_params.get('keyword')
        type_get = self.request.query_params.get('is_private')
        

        if keyword is not None :
            events = events.filter(title__icontains=keyword)

        if type_get is not None:
            if type_get=='1' or type_get=='2' :
                events=events.filter(type = type_get)
            elif type_get=='':
                events=events.filter(title__in=['1','2'])    
   
        return events



class EventAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated,]

    def get(self,request):     
        events = Event.objects.filter(is_archived=1)
        keyword = self.request.query_params.get('keyword')

        if keyword is not None :
            events = events.filter(title__icontains=keyword)

        type_get = self.request.query_params.get('type')
        

        if type_get is not None:
                
            if (type_get == '1' or type_get == '2' ):
                events = events.filter(type=type_get)
            elif (type_get == '') :
                events = events.filter(type__in=['1','2']) 

        serializer = EventSerializer(events, many=True)    
        return Response(data=serializer.data, status=status.HTTP_200_OK)    

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class DetailEvent(APIView):
    # permission_classes = [permissions.IsAuthenticated,]

    def get_object(self, pk) :
        try :
            return Event.objects.get(event_id=pk)
        except Event.DoesNotExist : #tên model
            raise Http404

    def get(self,request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)        

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


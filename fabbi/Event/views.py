from django.shortcuts import render
from rest_framework import pagination,viewsets,generics

from .models import Events
from .serializer import EventSerializer
from .paginator import EventPagination

# Create your views here.
class EventViewSet(viewsets.ViewSet,generics.ListAPIView) :
    # queryset = Events.objects.filter(is_archived = 0)
    serializer_class = EventSerializer
    pagination_class = EventPagination

    def get_queryset(self):
        events = Events.objects.filter(is_archived=0)

        keyword = self.request.query_params.get('keyword')
        if keyword is not None :
            events = events.filter(title__icontains=keyword)

        type = self.request.query_params.get('type')
        if (type == '1' or type == '2' ):
            events = events.filter(type=type)
        elif (type == '') :
            events = events.filter(type__in=['1','2'])    



        return events
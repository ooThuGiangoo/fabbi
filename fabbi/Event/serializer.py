from django.db import models
from django.db.models import fields
from rest_framework import relations, serializers
from rest_framework.utils import representation
from .models import Event
from User.models import Image_path


class EventSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Event
        fields = ['event_id','type','title']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try :
            img = Image_path.objects.filter(event_id = instance.event_id) 
            representation['image_url'] = img.values('image_url')

        except Image_path.DoesNotExist :
            img = None   
            representation['image_url'] = ''
        
        return representation
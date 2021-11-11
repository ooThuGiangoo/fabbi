from django.contrib import admin

from Livestream.models import Live_stream, Live_stream_viewer

# Register your models here.

admin.site.register(Live_stream)
admin.site.register(Live_stream_viewer)
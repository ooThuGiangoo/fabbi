from django.contrib import admin
from .models import Host_user_link, Image_paths, Mgmt_portal_user, User_additional_profile, User_stamp, Users,Clients,Prefectures
# Register your models here.


admin.site.register(Users)
admin.site.register(Clients)
admin.site.register(Prefectures)
admin.site.register(Image_paths)
admin.site.register(User_stamp)
admin.site.register(Host_user_link)
admin.site.register(User_additional_profile)
admin.site.register(Mgmt_portal_user)
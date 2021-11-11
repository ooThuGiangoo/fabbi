from django.contrib import admin
from .models import Host_user_link, Image_path, Mgmt_portal_user, User_additional_profile, User, Client
# Register your models here.


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Image_path)
admin.site.register(Host_user_link)
admin.site.register(User_additional_profile)
admin.site.register(Mgmt_portal_user)
from django.contrib import admin
from MasterData.models import Additional_profile_item, Device_token, Email_auth, Password_reset, Push_notification, Push_notification_master_content, Push_notification_trans_content,Refresh_token, Related_link, Sent_relation, Stamp_receipt_history, Stamp_spending_history
from MasterData.models import Email_notification, Email_notification_master_content, Email_notification_trans_content
from MasterData.models import Box_notification, Box_notification_master_content, Box_notification_trans_content
from MasterData.models import Prefectures

# Register your models here.
admin.site.register(Stamp_receipt_history)
admin.site.register(Stamp_spending_history)
admin.site.register(Additional_profile_item)
admin.site.register(Push_notification_master_content)
admin.site.register(Push_notification_trans_content)
admin.site.register(Push_notification)
admin.site.register(Sent_relation)
admin.site.register(Email_auth)
admin.site.register(Password_reset)
admin.site.register(Refresh_token)
admin.site.register(Device_token)
admin.site.register(Related_link)
admin.site.register(Email_notification)
admin.site.register(Email_notification_master_content)
admin.site.register(Email_notification_trans_content)
admin.site.register(Box_notification)
admin.site.register(Box_notification_master_content)
admin.site.register(Box_notification_trans_content)
admin.site.register(Prefectures)

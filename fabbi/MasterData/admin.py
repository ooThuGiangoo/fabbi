from django.contrib import admin
from Event.models import Email_notification, Email_notification_master_content, Email_notification_trans_content

from MasterData.models import Additional_profile_item, Device_token, Drawing, Email_auth, Follow, Password_reset, Push_notification, Push_notification_master_content, Push_notification_trans_content, Ranking_summary, Refresh_token, Related_link, Sent_relation, Stamp_receipt_history, Stamp_spending_history

# Register your models here.
admin.site.register(Drawing)
admin.site.register(Follow)
admin.site.register(Stamp_receipt_history)
admin.site.register(Stamp_spending_history)
admin.site.register(Ranking_summary)
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
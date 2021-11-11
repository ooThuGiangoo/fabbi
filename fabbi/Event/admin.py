from django.contrib import admin

from Event.models import Box_notification, Box_notification_master_content, Box_notification_trans_content, Events, Gift, Gift_purchase_history, Gift_tipping_history, Performance, Ranking, Stamps_code, Ticket, Ticket_purchase_history, Ticket_purchase_revervation, User_gift, User_point, User_ticket
from Event.models import Event_authorized_user

# Register your models here.
admin.site.register(Events)
admin.site.register(Event_authorized_user)
admin.site.register(Performance)
admin.site.register(Ticket)
admin.site.register(Ticket_purchase_revervation)
admin.site.register(Ticket_purchase_history)
admin.site.register(User_ticket)
admin.site.register(Gift)
admin.site.register(Gift_purchase_history)
admin.site.register(Gift_tipping_history)
admin.site.register(User_gift)
admin.site.register(User_point)
admin.site.register(Box_notification_master_content)
admin.site.register(Box_notification_trans_content)
admin.site.register(Box_notification)
admin.site.register(Stamps_code)
admin.site.register(Ranking)

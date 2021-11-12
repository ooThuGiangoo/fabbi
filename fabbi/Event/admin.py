from django.contrib import admin

from Event.models import Event,Performance,Ticket, Ticket_purchase_history, Ticket_purchase_revervation,  User_ticket
from Event.models import Event_authorized_user
from Event.models import Drawing

# Register your models here.
admin.site.register(Event)
admin.site.register(Event_authorized_user)
admin.site.register(Performance)
admin.site.register(Ticket)
admin.site.register(Ticket_purchase_revervation)
admin.site.register(Ticket_purchase_history)
admin.site.register(User_ticket)
admin.site.register(Drawing)


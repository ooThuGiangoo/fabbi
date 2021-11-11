from django.db import models
from django.db.models.base import Model
from django.db.models.fields import SmallIntegerField
# from User.models import Clients
# from User.models import Users

# Create your models here.
class Events(models.Model) : 
    choice_type = (
        (1 , 'Live stream event'),
        (2 , 'Office event'))
    choice_private = (
        (0 , 'Not private'),
        (1 , 'Private')   )
    choice_archive = (
        (0 , 'Not archived'),
        (1 , 'Archived'))
    event_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    type = models.IntegerField(choices = choice_type)
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_private = models.IntegerField(choices = choice_private, default =1)
    private_key = models.CharField(max_length=255, null=True)
    is_archived = models.IntegerField(choices = choice_archive)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Event_authorized_user(models.Model):
    event_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User.Users", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    


class Performance(models.Model) :
    choice_ticket = (
        (0, 'Not available'),
        (1, 'Available')
    )
    performance_id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    streaming_method = models.SmallIntegerField(null = True)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(auto_now_add=True)
    capacity =models.IntegerField(null = True)
    ticket_available_flag = models.SmallIntegerField(choices= choice_ticket, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Ticket(models.Model) :
    choice_draw = (
        (0, 'No drawing'),
        (1, 'By drawing')
    )
    choice_status = (
        (0, 'Drawing preiod'),
        (1, ' Purchase method')
    )
    choice_flag = (
        (0, 'Not available'),
        (1, 'Available')
    )
    choice_seat = (
        (0, 'Not assigned'),
        (1, 'Assigned')
    )
    ticket_id = models.IntegerField(primary_key=True)
    performance_id = models.ForeignKey(Performance, on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    points_required = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    expiration_datetime = models.DateTimeField(auto_now_add=True)
    drawing_flag = models.SmallIntegerField(choices= choice_draw, default=1)
    drawing_application_deadline = models.DateTimeField(null=True, auto_now_add=True)
    drawing_status = models.SmallIntegerField(choices=choice_status, default=1)
    stamp_available_flag = models.SmallIntegerField(choices= choice_flag, default=1)
    max_number_of_ticket = models.IntegerField()
    number_of_issued_tickets = models.IntegerField()
    is_seat_id_assigned = models.SmallIntegerField(choices=choice_seat, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Ticket_purchase_revervation (models.Model) :
    choice_purchase = (
        (0 , 'Not purchased'),
        (1, 'Purchased')
    )
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User.Users", on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255, null=True)
    number_of_tickets = models.IntegerField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    is_purchased = models.SmallIntegerField(choices=choice_purchase, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.order_id

class User_ticket(models.Model) :
    choice_settle = (
        (0 , 'Unsettled'),
        (1 , 'Settled'))
    choice_status = (
        (0 , 'Unused'),
        (1 , 'Used'))
    user_ticket_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    ticket_id = models.IntegerField()
    is_settled = models.IntegerField(choices=choice_settle, default=1)
    seat_id = models.CharField(max_length=255, null=True)
    expire_in = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=choice_status, default =1 )
    used_at = models.DateTimeField(null=True, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    def __str__(self):
        return self.seat_id

class Ticket_purchase_history(models.Model) :
    choice_type = (
        ('card', 'Credit card'),
        ('cvs', 'Convenience store payment')
    )
    id = models.IntegerField(primary_key=True)
    user_ticket_id = models.ForeignKey(User_ticket, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    point_amount = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    order_id = models.CharField(max_length=100, null=True)
    payment_type = models.CharField(choices=choice_type, null=True, max_length=25)
    purchased_at = models.DateTimeField(auto_now_add=True)
    settle_at = models.DateTimeField(null=True, auto_now_add=True)
    receipt_number = models.CharField(max_length=32, null=True)
    haraikomi_url = models.CharField(max_length=256)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    def __str__(self):
        return self.order_id

class Gift(models.Model) :
    gift_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    points_spent = models.DecimalField(max_digits=15, decimal_places=0)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

class User_gift(models.Model):
    choice_status= (
        (0 , 'Unused'),
        (1 , 'Used'))
    user_gift_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User.Users", on_delete=models.CASCADE)
    gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
    status = models.IntegerField(choices= choice_status, default = 1)
    used_at = models.DateTimeField(null=True, auto_now_add=True)        
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)


class User_point(models.Model) :
    choice_type = (
        (1 , 'Deposit'),
        (2 , 'Withdrawal'))
    choice_withdrawal = (
        (1 , 'Exchange for a gift'),
        (2 , 'Exchange for a ticket'))
    choice_deposit = (
        (1 , 'Purchase'),)
    user_point_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User.Users", on_delete=models.CASCADE)
    type = models.IntegerField(choices=choice_type, default = 1)
    deposit_reason = models.IntegerField(null = True, choices=choice_deposit)        
    withdrawal_reason = models.IntegerField(null = True, choices=choice_withdrawal)        
    points = models.DecimalField(max_digits=15, decimal_places=0)
    transacted_at = models.DateTimeField(auto_now_add=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

class Box_notification_trans_content(models.Model) :
    choice_type = (
       (1,'Host user'), 
        (2, 'Client user (Mgmt portal user)'),
        (3, 'System admin user( Mgmt portal user)'))
    choice_deliver = (
        (0 , 'Not delivered'),
        (1 , 'Delivered') )
    box_notification_trans_content_id = models.IntegerField(primary_key= True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    from_type = models.IntegerField(choices=choice_type, default=1)
    from_user_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add=True) 
    is_delivered = models.IntegerField(choices=choice_deliver)
    delivered_at = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title

class Box_notification_master_content (models.Model):
    box_notification_master_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    memo = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title


class Box_notification(models.Model):
    choice_read =(
        (0, 'Not read'),
        (1, 'Read')
    )
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User.Users", on_delete=models.CASCADE) 
    box_notification_master_content_id = models.ForeignKey(Box_notification_master_content, on_delete=models.SET_NULL, null=True) 
    box_notification_trans_content_id = models.ForeignKey(Box_notification_trans_content, on_delete=models.SET_NULL, null=True) 
    is_read = models.SmallIntegerField(choices=choice_read, default=1)
    read_at = models.DateTimeField(auto_now_add = True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Gift_purchase_history (models.Model):
    id = models.IntegerField(primary_key=True)
    user_gift_id = models.ForeignKey(User_gift, on_delete=models.CASCADE)
    user_point_id = models.ForeignKey(User_point, on_delete=models.CASCADE)
    points_spent = models.DecimalField(max_digits=15, decimal_places=0)
    purchased_at = models.DateTimeField(null=False, auto_now_add = True)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)    

class Gift_tipping_history(models.Model) :
    id = models.IntegerField(primary_key=True)
    user_gift_id = models.ForeignKey(User_gift, on_delete=models.CASCADE)
    to_user_id = models.ForeignKey(Box_notification_trans_content, on_delete=models.CASCADE)
    points_equivalent = models.DecimalField(max_digits=15, decimal_places=0)
    tipped_at = models.DateTimeField(null=False, auto_now_add = True)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)    

class Stamps_code(models.Model):
    stamp_code_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    stamps_granted = models.DecimalField(max_digits=15, decimal_places=0)
    number_of_applicable_user = models.IntegerField(null=True)
    number_of_applied_user = models.IntegerField()
    expires_in = models.DateTimeField(null=False, auto_now_add = True)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True) 

    def __str__(self):
        return self.name

class Ranking(models.Model):
    choice_type = (
        (1, 'Tipping'),
        (2, 'Tipped')
    )
    ranking_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=choice_type, default=1)  
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True) 

    

class Email_notification_master_content(models.Model):
    choice_timing = (
        (1, 'When a drawing winner is determined'),
        (2, 'When tickets purchase is complete'),
        (99, 'Any timing (Templates for mgmt portal)')
    )
    email_notification_master_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    timing_type = SmallIntegerField(choices=choice_timing, default=1)
    title = models.CharField(max_length=255)
    body = models.TextField()
    memo = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    def __str__(self):
        return self.title


class Email_notification_trans_content(models.Model):
    choice_deliver = (
        (0, 'Not delivered'),
        (1, 'Delivered')
    )
    email_notification_trans_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add = True)
    is_delivered = models.SmallIntegerField(choices=choice_deliver, default=1)
    delivered_at = models.DateTimeField(null=True, auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Email_notification(models.Model) :
    choice_status = (
        (0, 'Not sent'),
        (1, 'Sent'),
        (2, 'Error')
    )
    id = models.BigIntegerField(primary_key=True)
    to_email = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    body = models.TextField()
    scheduled_at = models.DateTimeField(auto_now_add = True)
    status = models.SmallIntegerField(choices=choice_status, default=1)
    sent_at = models.DateTimeField(null=True, auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title



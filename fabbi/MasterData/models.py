from django.db import models
from django.db.models.fields import IntegerField
from User.models import Users, User_stamps
from Event.models import Ranking
from fabbi.Event.models import Email_notification_trans_contents
from fabbi.User.models import Clients

# Create your models here.
class Drawing (models.Model):
    choice_elect = (
        (0,'Not elected'),
        (1, 'Elected')
    )
    choice_purchase = (
        (0, 'Not purchased'),
        (1, 'Purchased')
    )
    ticket_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_elected = models.SmallIntegerField(choices=choice_elect, default=1)
    is_purchased = models.SmallIntegerField(choices=choice_purchase, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Follow(models.Model):
    from_user_id = models.IntegerField()  
    to_user_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Stamp_receipt_history(models.Model):
    id = models.IntegerField(primary_key=True)
    user_stamp_id = models.ForeignKey(User_stamps, on_delete=models.CASCADE)
    live_stream_id = models.IntegerField(null=True)    
    stamp_code_id = models.IntegerField(null=True)
    received_at = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Stamp_spending_history(models.Model):
    choice_spend = (
        (1, 'Ticket'),
    )
    id = models.IntegerField(primary_key=True)
    user_stamp_id = models.ForeignKey(User_stamps, on_delete=models.CASCADE)
    spent_for = models.SmallIntegerField(choices=choice_spend, default=1)
    stamp_code_id = models.IntegerField(null=True)
    spent_at = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Ranking_summary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ranking_id = models.ForeignKey(Ranking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=0)
    target_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Additional_profile_item(models.Model):
    Additional_profile_item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Push_notification_master_content (models.Model):
    push_notification_master_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField()
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    internal_url = models.CharField(max_length=255, null=True)
    memo = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title

class Push_notification_trans_content(models.Model) :
    choice_deliver = (
        (0 , 'Not delivered'),
        (1 , 'Delivered') )
    push_notification_trans_content_id = models.IntegerField(primary_key= True)
    client_id = models.ForeignKey("User.Clients", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    internal_url = models.CharField(max_length=255, null=True)
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add=True) 
    is_delivered = models.IntegerField(choices=choice_deliver)
    delivered_at = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.body

class Push_notification(models.Model):
    choice_platform = (
        (1,'IOS'),
        (2,'Android')
    )
    choice_status =(
        (0, 'Not sent'),
        (1, 'Sent')
    )
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User.Users", on_delete=models.CASCADE) 
    to_platform = models.SmallIntegerField(choices=choice_platform, default=1)
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    internal_url = models.CharField(max_length=255, null=True)
    scheduled_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(choices=choice_status, default=1)
    sent_at = models.DateTimeField(auto_now_add = True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)       

class Sent_relation(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models,IntegerField(null=True)
    live_stream_id = models.IntegerField(null=True)
    email_notification_trans_content_id  = models.IntegerField(null=True)
    push_notification_trans_content_id  = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 

class Email_auth(models.Model):
    choice_type = (
        (1,'General user'),
        (2,'Host user'),
        (3,'Mgmt portal user')
    )
    id = models.IntegerField(primary_key=True)
    user_type = models.SmallIntegerField(choices=choice_type, default=1)
    email = models.CharField(max_length=254)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 


class Password_reset(models.Model):
    choice_type = (
        (1,'General user'),
        (2,'Host user'),
        (3,'Mgmt portal user')
    )
    id = models.IntegerField(primary_key=True)
    user_type = models.SmallIntegerField(choices=choice_type, default=1)
    email = models.CharField(max_length=254)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 


class Refresh_token(models.Model):
    choice = (
        (0,'Not blacklisted'),
        (2,'Blacklisted')
    )
    refresh_token_id = models.BigIntegerField(primary_key=True)
    user_id = models.IntegerField(null=True)
    mgmt_portal_user_id = models.IntegerField(null=True)
    encrypted_refresh_token = models.CharField(max_length=255)
    expires_in = models.DateTimeField(auto_now_add = True)
    is_blacklisted = models.SmallIntegerField(choices=choice, default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)     


class Device_token(models.Model):
    choice_platform = (
        (1,'IOS'),
        (2,'Android')
    )
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField() 
    platform = models.SmallIntegerField(choices=choice_platform, default=1)
    title = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=255)
    invalidated_at = models.DateTimeField(auto_now_add = True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)       

    def __str__(self):
        return self.title

class Related_link(models.Model) :
    id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    dir_path = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)       

    def __str__(self):
        return self.title


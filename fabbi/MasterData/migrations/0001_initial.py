# Generated by Django 3.2.9 on 2021-11-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additional_profile_item',
            fields=[
                ('additional_profile_item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device_token',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('platform', models.SmallIntegerField(choices=[(1, 'IOS'), (2, 'Android')], default=1)),
                ('title', models.CharField(max_length=255, null=True)),
                ('token', models.CharField(max_length=255)),
                ('invalidated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_elected', models.SmallIntegerField(choices=[(0, 'Not elected'), (1, 'Elected')], default=1)),
                ('is_purchased', models.SmallIntegerField(choices=[(0, 'Not purchased'), (1, 'Purchased')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email_auth',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField(choices=[(1, 'General user'), (2, 'Host user'), (3, 'Mgmt portal user')], default=1)),
                ('email', models.CharField(max_length=254)),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('from_user_id', models.IntegerField()),
                ('to_user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Password_reset',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField(choices=[(1, 'General user'), (2, 'Host user'), (3, 'Mgmt portal user')], default=1)),
                ('email', models.CharField(max_length=254)),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Push_notification',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('to_platform', models.SmallIntegerField(choices=[(1, 'IOS'), (2, 'Android')], default=1)),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.TextField()),
                ('internal_url', models.CharField(max_length=255, null=True)),
                ('scheduled_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Not sent'), (1, 'Sent')], default=1)),
                ('sent_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Push_notification_master_content',
            fields=[
                ('push_notification_master_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('timing_type', models.SmallIntegerField()),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.TextField()),
                ('internal_url', models.CharField(max_length=255, null=True)),
                ('memo', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Push_notification_trans_content',
            fields=[
                ('push_notification_trans_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.TextField()),
                ('internal_url', models.CharField(max_length=255, null=True)),
                ('to_user_ids', models.TextField(null=True)),
                ('scheduled_at', models.DateTimeField(auto_now_add=True)),
                ('is_delivered', models.IntegerField(choices=[(0, 'Not delivered'), (1, 'Delivered')])),
                ('delivered_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking_summary',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=15)),
                ('target_date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Refresh_token',
            fields=[
                ('refresh_token_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('mgmt_portal_user_id', models.IntegerField(null=True)),
                ('encrypted_refresh_token', models.CharField(max_length=255)),
                ('expires_in', models.DateTimeField(auto_now_add=True)),
                ('is_blacklisted', models.SmallIntegerField(choices=[(0, 'Not blacklisted'), (2, 'Blacklisted')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Related_link',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('link_url', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('dir_path', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sent_relation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('live_stream_id', models.IntegerField(null=True)),
                ('email_notification_trans_content_id', models.IntegerField(null=True)),
                ('push_notification_trans_content_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stamp_receipt_history',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('live_stream_id', models.IntegerField(null=True)),
                ('stamp_code_id', models.IntegerField(null=True)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stamp_spending_history',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('spent_for', models.SmallIntegerField(choices=[(1, 'Ticket')], default=1)),
                ('stamp_code_id', models.IntegerField(null=True)),
                ('spent_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
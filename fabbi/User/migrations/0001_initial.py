# Generated by Django 3.2.9 on 2021-11-11 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MasterData', '0001_initial'),
        ('Livestream', '0001_initial'),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('seconds_delivered_per_month', models.DecimalField(decimal_places=0, max_digits=15)),
                ('is_archived', models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('prefecture_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('display_order', models.SmallIntegerField()),
                ('is_default', models.SmallIntegerField(choices=[(0, 'Not default'), (1, 'Default')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField(choices=[(1, 'General user'), (2, 'Host user')], default=0)),
                ('login_type', models.CharField(choices=[('email', 'EMAIL'), ('insta', 'INSTAGRAM'), ('facebook', 'FACEBOOK'), ('twitter', 'TWITTER')], default='email', max_length=45)),
                ('email', models.CharField(max_length=254, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('remember_token', models.CharField(max_length=255, null=True)),
                ('facebook_id', models.CharField(max_length=255, null=True)),
                ('twitter_id', models.CharField(max_length=255, null=True)),
                ('apple_id', models.CharField(max_length=255, null=True)),
                ('last_name_kanji', models.CharField(max_length=255)),
                ('first_name_kanji', models.CharField(max_length=255)),
                ('last_name_kana', models.CharField(max_length=255)),
                ('first_name_kana', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('sex', models.SmallIntegerField(choices=[(0, 'Not known'), (1, 'Male'), (2, 'Female'), (9, 'Not applicable')], default=1)),
                ('is_sex_public', models.SmallIntegerField(choices=[(0, 'Private'), (1, 'Public')], default=1)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('is_date_of_birth_public', models.SmallIntegerField(choices=[(0, 'Private'), (1, 'Public')], default=1)),
                ('phone', models.CharField(max_length=45, null=True)),
                ('zip_code', models.CharField(max_length=8, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('subsequent_address', models.CharField(max_length=255, null=True)),
                ('biography', models.TextField(null=True)),
                ('points_balance', models.DecimalField(decimal_places=0, max_digits=15)),
                ('points_reveived', models.DecimalField(decimal_places=0, max_digits=15)),
                ('stamps_balance', models.DecimalField(decimal_places=0, max_digits=15)),
                ('econtext_cus_id', models.CharField(max_length=255, null=True)),
                ('delux_membership', models.CharField(max_length=255, null=True)),
                ('host_user_type', models.SmallIntegerField(choices=[(1, 'Individual'), (2, 'Group')], default=1, null=True)),
                ('is_authenticated', models.SmallIntegerField(choices=[(0, 'Not authenticated'), (1, 'Authenticated'), (2, 'No authenticated required')], default=1)),
                ('is_archived', models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.clients')),
                ('prefecture_id', models.ForeignKey(max_length=11, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.prefectures')),
            ],
        ),
        migrations.CreateModel(
            name='User_stamp',
            fields=[
                ('user_stamp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal')], default=1)),
                ('deposit_reason', models.IntegerField(choices=[(1, 'Participation in a performance'), (2, 'Application of a stamp code')], null=True)),
                ('withdrawal_reason', models.IntegerField(choices=[(1, 'Exchange for a ticket')], null=True)),
                ('stamps', models.DecimalField(decimal_places=0, max_digits=15)),
                ('transacted_at', models.DateTimeField(auto_now_add=True)),
                ('stamps_balance', models.DecimalField(decimal_places=0, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.users')),
            ],
        ),
        migrations.CreateModel(
            name='User_additional_profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('additional_profile_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterData.additional_profile_item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.users')),
            ],
        ),
        migrations.CreateModel(
            name='Mgmt_portal_user',
            fields=[
                ('mgmt_portal_user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.IntegerField(choices=[(1, 'System admin user'), (2, 'Client user'), (3, 'Host user')], default=1)),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('remember_token', models.CharField(max_length=255, null=True)),
                ('is_archived', models.IntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.clients')),
            ],
        ),
        migrations.CreateModel(
            name='Image_paths',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('dir_path', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('box_notification_trans_content_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Event.box_notification_trans_content')),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.clients')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.users')),
            ],
        ),
        migrations.CreateModel(
            name='Host_user_link',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('host_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Livestream.live_stream')),
            ],
        ),
    ]

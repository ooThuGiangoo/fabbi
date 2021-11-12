# Generated by Django 3.2.9 on 2021-11-12 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('MasterData', '0001_initial'),
        ('Point', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stamp_spending_history',
            name='user_stamp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Point.user_stamp'),
        ),
        migrations.AddField(
            model_name='stamp_receipt_history',
            name='user_stamp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Point.user_stamp'),
        ),
        migrations.AddField(
            model_name='related_link',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='push_notification_trans_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='push_notification_master_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='push_notification',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
        migrations.AddField(
            model_name='email_notification_trans_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='email_notification_master_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='box_notification_trans_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='box_notification_master_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='box_notification',
            name='box_notification_master_content_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterData.box_notification_master_content'),
        ),
        migrations.AddField(
            model_name='box_notification',
            name='box_notification_trans_content_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterData.box_notification_trans_content'),
        ),
        migrations.AddField(
            model_name='box_notification',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
    ]

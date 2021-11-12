# Generated by Django 3.2.9 on 2021-11-12 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Event', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_purchase_revervation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
        migrations.AddField(
            model_name='ticket_purchase_history',
            name='user_ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.user_ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='performance_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.performance'),
        ),
        migrations.AddField(
            model_name='performance',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event'),
        ),
        migrations.AddField(
            model_name='event_authorized_user',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
        migrations.AddField(
            model_name='event',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.client'),
        ),
        migrations.AddField(
            model_name='drawing',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
    ]

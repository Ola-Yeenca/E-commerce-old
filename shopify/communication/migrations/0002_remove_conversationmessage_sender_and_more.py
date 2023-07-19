# Generated by Django 4.2.3 on 2023-07-19 16:01

import communication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationmessage',
            name='sender',
        ),
        migrations.AddField(
            model_name='conversationmessage',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_as_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='member',
            field=models.ManyToManyField(related_name='conversations_as_member', to=settings.AUTH_USER_MODEL),
        ),
    ]

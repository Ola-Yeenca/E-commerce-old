# Generated by Django 4.2.3 on 2023-07-19 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0010_alter_item_created_by'),
    ]

    operations = [
        # ...
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None),
        ),
        # ...
    ]
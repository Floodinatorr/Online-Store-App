# Generated by Django 4.1.2 on 2022-10-23 14:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_storecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='store_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
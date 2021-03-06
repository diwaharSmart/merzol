# Generated by Django 3.2 on 2022-07-30 00:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0002_auto_20220729_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_id',
            field=models.CharField(default=uuid.UUID('0e1244c4-03e0-40fe-ad33-fe5fef01fa04'), max_length=255, unique=True),
        ),
    ]

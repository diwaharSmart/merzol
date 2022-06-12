# Generated by Django 3.2.8 on 2022-06-12 09:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_user_last_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='google_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_google_auth',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]
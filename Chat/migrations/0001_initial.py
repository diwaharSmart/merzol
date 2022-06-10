# Generated by Django 3.2.8 on 2022-06-06 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0003_alter_user_last_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='message/file/')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(blank=True, max_length=255, null=True)),
                ('media_attached', models.URLField(blank=True, null=True)),
                ('text', models.BooleanField(default=False)),
                ('media', models.BooleanField(default=False)),
                ('timestamp', models.CharField(blank=True, max_length=255, null=True)),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.user')),
            ],
        ),
    ]
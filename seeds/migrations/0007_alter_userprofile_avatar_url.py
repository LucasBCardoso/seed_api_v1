# Generated by Django 5.1.1 on 2024-10-05 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0006_usercargo_rename_name_client_fantasy_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='URL do Avatar'),
        ),
    ]

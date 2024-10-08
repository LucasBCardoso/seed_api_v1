# Generated by Django 5.1.1 on 2024-10-05 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0004_alter_client_field_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='field_area',
            field=models.IntegerField(blank=True, null=True, verbose_name='Área de Campo (Ha)'),
        ),
        migrations.AlterField(
            model_name='clientaddress',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seeds.client', verbose_name='Cliente'),
        ),
    ]

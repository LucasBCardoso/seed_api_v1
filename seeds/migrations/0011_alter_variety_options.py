# Generated by Django 5.1.1 on 2024-10-05 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0010_alter_clientnegotiation_id_alter_orderitems_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variety',
            options={'verbose_name': 'Variedade / Cultivar', 'verbose_name_plural': 'Variedades / Cultivares'},
        ),
    ]

# Generated by Django 3.1.2 on 2021-04-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_slots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryslot',
            name='active',
        ),
        migrations.AddField(
            model_name='deliveryslot',
            name='special_item',
            field=models.BooleanField(default=True),
        ),
    ]

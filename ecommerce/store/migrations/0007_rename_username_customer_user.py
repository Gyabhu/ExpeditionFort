# Generated by Django 4.1.3 on 2023-05-15 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_customer_user_customer_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='user',
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-20 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0009_customer_password_alter_customer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
    ]

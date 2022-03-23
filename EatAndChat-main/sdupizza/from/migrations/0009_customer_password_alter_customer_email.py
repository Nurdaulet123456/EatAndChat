# Generated by Django 4.0.2 on 2022-03-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0008_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0002_form_delete_formmodals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('img_name', models.CharField(max_length=400)),
                ('img_subtitle', models.TextField(max_length=10000)),
                ('img_price', models.DecimalField(decimal_places=5, max_digits=1000)),
            ],
        ),
    ]

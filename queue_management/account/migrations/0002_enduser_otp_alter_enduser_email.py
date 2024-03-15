# Generated by Django 5.0.2 on 2024-03-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

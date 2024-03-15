# Generated by Django 5.0.2 on 2024-03-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_enduser_user_is_enduser_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='information',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_enduser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='services',
        ),
    ]

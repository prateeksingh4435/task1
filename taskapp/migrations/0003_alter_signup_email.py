# Generated by Django 4.1.7 on 2024-07-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_remove_signup_user_alter_signup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]

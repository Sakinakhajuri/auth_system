# Generated by Django 3.2.3 on 2021-10-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_register_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='confirm_password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
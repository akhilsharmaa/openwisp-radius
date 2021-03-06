# Generated by Django 3.1.6 on 2021-02-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_users', '0003_update_user_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.TextField(
                blank=True, help_text='notes for internal usage', verbose_name='notes'
            ),
        ),
    ]
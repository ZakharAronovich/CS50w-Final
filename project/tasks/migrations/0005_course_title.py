# Generated by Django 5.0.6 on 2024-07-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]

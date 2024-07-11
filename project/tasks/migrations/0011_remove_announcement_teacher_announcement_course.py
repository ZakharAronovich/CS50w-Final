# Generated by Django 5.0.6 on 2024-07-11 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_announcement_recipients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='teacher',
        ),
        migrations.AddField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='announcements_by_course', to='tasks.course'),
        ),
    ]
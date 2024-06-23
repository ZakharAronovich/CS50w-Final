# Generated by Django 5.0.6 on 2024-06-23 13:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('TC', 'Teacher'), ('ST', 'Student')], default=None, max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='students',
            field=models.ManyToManyField(related_name='assigned_tasks', to='tasks.student'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='tasks.teacher'),
        ),
        migrations.AddField(
            model_name='task',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to='tasks.teacher'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ALG', 'Algebra'), ('ART', 'Art'), ('BIO', 'Biology'), ('CHE', 'Chemistry'), ('ENG', 'English'), ('GEO', 'Geography'), ('HIS', 'History'), ('PE', 'PE')], max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(related_name='courses_by_tag', to='tasks.tag'),
        ),
    ]

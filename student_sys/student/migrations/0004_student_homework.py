# Generated by Django 2.2.3 on 2019-09-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='homework',
            field=models.CharField(default='尚未有公布的作业', max_length=128, verbose_name='作业公告栏'),
        ),
    ]

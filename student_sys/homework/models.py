from django.db import models


class Homework(models.Model):
    hw = models.TextField(default="尚未有公布的作业", verbose_name='作业公告栏')

    def __str__(self):
        return '<Homework: {}>'.format(self.hw)

    class Meta:
        verbose_name = verbose_name_plural = "HomeworkInf"

    @classmethod
    def get_all(cls):
        return cls.objects.all()
# Create your models here.

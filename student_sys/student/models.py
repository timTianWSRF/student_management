from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, 'male'),
        (2, 'female'),
        (0, 'unknown'),
    ]
    STATUS_ITEMS = [
        (0, 'applying'),
        (1, 'passed'),
        (2, 'refused'),
    ]
    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='学号')
    email = models.EmailField(verbose_name='电子邮箱')
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='手机号码')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    score = models.CharField(max_length=128, default="尚未批改", verbose_name='成绩')

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "StudentInf"

    @classmethod
    def get_all(cls):
        return cls.objects.all()




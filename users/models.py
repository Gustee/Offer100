from django.contrib.auth.models import User
from django.db import models
from resume.models import Resume
from company.models import Company
from datetime import datetime

# Create your models here.


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=10, verbose_name='姓名')
    age = models.CharField(max_length=10, verbose_name='年龄')
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    city = models.CharField(max_length=20, verbose_name='城市')
    education = models.CharField(max_length=10, choices=(('bachelor', '本科'), ('master', '硕士'), ('doctor', '博士')), default='bachelor')
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)
    resume = models.OneToOneField(Resume, on_delete=models.PROTECT, null=True,blank=True)

    class Meta:
        verbose_name = "候选人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, verbose_name='姓名')
    phone = models.CharField(max_length=15, verbose_name='电话')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True,blank=True),
    position = models.CharField(max_length=20, default='',verbose_name='职位')

    class Meta:
        verbose_name = "HR信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register", "注册"), ("forget", "找回密码")), max_length=10)
    send_time = models.DateField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
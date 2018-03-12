
from resume.models import *
from company.models import *
from users.models import *
from django.db import models
# Create your models here.


class Job(models.Model):
    # company = models.ForeignKey(Company, null=True, on_delete=models.PROTECT, verbose_name="公司"),
    # HR = models.ForeignKey(HR, null=True, on_delete=models.PROTECT, verbose_name="HR"),
    tpye = models.OneToOneField(Careers, on_delete=models.PROTECT, verbose_name='岗位类型')
    name = models.CharField(max_length=20, verbose_name="岗位名称")
    work_city = models.CharField(max_length=20, verbose_name="工作城市")
    addrees = models.CharField(max_length=100, verbose_name="具体地址")
    # wage_tpye = models.CharField(max_length=10, choices=(('m', '月薪'), ('y', '年薪')), verbose_name="月薪或年薪"),
    wage = models.FloatField(default=0.0, verbose_name="工资")
    exp_time = models.IntegerField(verbose_name="工作经验")
    job_description = models.TextField(default="", max_length=500, verbose_name="岗位描述")
    job_requirements = models.TextField(default="", max_length=500, verbose_name="岗位要求")
    key_words = models.CharField(default="", max_length=50, verbose_name="岗位关键字")
    is_verify = models.BooleanField(default=False, verbose_name="审核状态")
    edu = models.CharField(max_length=10, choices=(('0', '无限制'), ('1', '专科'), ('2', '本科'), ('3', '硕士'), ('4', '博士')), verbose_name="最低学历要求")
    school = models.CharField(max_length=10, choices=(('0', '无限制'), ('1', '一本'), ('2', '211'), ('3', '985'), ('4', '清北')), verbose_name="院校要求")
    HR = models.ForeignKey(HR, on_delete=models.PROTECT, null=True, verbose_name="HR")

    class Meta:
        verbose_name = "职位信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.


## 技术 数据 产品 设计 大职业方向
class Careers(models.Model):
    name = models.CharField(max_length=20)

# 具体技能
class Skills(models.Model):
    name = models.CharField(max_length=20)
    belong_careers = models.ForeignKey(Careers, on_delete=models.PROTECT)


class Resume(models.Model):
    # 个人描述
    description = models.TextField()
    # 社交网站
    zhihu = models.CharField(max_length=100)
    blog = models.CharField(max_length=100)
    personal_site = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    # 工作经验
    work_experience = models.TextField(max_length=1000)
    # 教育经理
    edu_experience = models.TextField(max_length=1000)
    # 职业方向
    career = models.ForeignKey(Careers, on_delete=models.PROTECT)
    # 在该职业方向上工作的时间
    career_work_year = models.IntegerField()
    # 具体方向
    skill = models.ForeignKey(Skills, on_delete=models.PROTECT)
    # 技能关键字
    skill_keywords = models.CharField(max_length=50)


# class WorkExperience(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
#     company_name = models.CharField(max_length=100)
#     position = models.CharField(max_length=50)
#     start_date = models.DateField(null=True)
#     end_date = models.DateField(null=True)
#     description = models.CharField(max_length=1000)
#
#
# class ProjectExperience(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
#     project_name = models.CharField(max_length=100)
#     project_role = models.CharField(max_length=50)
#     start_date = models.DateField(null=True)
#     end_date = models.DateField(null=True)
#     description = models.CharField(max_length=1000)
#
#
# class EducationExperience(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
#     school_name = models.CharField(max_length=20)
#     education = models.CharField(max_length=10, choices=(('bachelor', '本科'), ('master', '硕士'), ('doctor', '博士')))
#     start_date = models.DateField(null=True)
#     end_date = models.DateField(null=True)
#     specialty = models.CharField(max_length=20)



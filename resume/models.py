from django.db import models

# Create your models here.


## 技术 数据 产品
class Careers(models.Model):
    name = models.CharField(max_length=20)


class Skills(models.Model):
    name = models.CharField(max_length=20)
    belong_careers = models.ForeignKey(Careers, on_delete=models.PROTECT)


class Resume(models.Model):
    description = models.TextField()
    zhihu = models.CharField(max_length=100)
    blog = models.CharField(max_length=100)
    personal_site = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    career = models.ForeignKey(Careers, on_delete=models.PROTECT)
    career_work_year = models.IntegerField()
    skill = models.ForeignKey(Skills, on_delete=models.PROTECT)
    skill_keywords = models.CharField(max_length=50)


class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=1000)


class ProjectExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
    project_name = models.CharField(max_length=100)
    project_role = models.CharField(max_length=50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=1000)


class EducationExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
    school_name = models.CharField(max_length=20)
    education = models.CharField(max_length=10, choices=(('bachelor', '本科'), ('master', '硕士'), ('doctor', '博士')))
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    specialty = models.CharField(max_length=20)



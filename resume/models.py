from django.db import models

# Create your models here.


## 技术 数据 产品 设计 大职业方向
class Careers(models.Model):
    name = models.CharField(max_length=20, verbose_name='职业方向')


    class Meta:
        verbose_name = "职业方向"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

# 具体技能
class Skills(models.Model):
    name = models.CharField(max_length=20, verbose_name='具体职业')
    belong_careers = models.ForeignKey(Careers, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "具体职业"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Resume(models.Model):
    # 个人描述
    description = models.TextField(verbose_name='个人描述')
    # 社交网站
    zhihu = models.CharField(max_length=100, verbose_name='知乎')
    blog = models.CharField(max_length=100, verbose_name='博客')
    personal_site = models.CharField(max_length=100, verbose_name='个人网站')
    github = models.CharField(max_length=100, verbose_name='github')
    # 工作经验
    work_experience = models.TextField(max_length=1000, default="", verbose_name='工作经验')
    # 教育经理
    edu_experience = models.TextField(max_length=1000, default="", verbose_name='教育')
    # 职业方向
    career = models.ForeignKey(Careers, on_delete=models.PROTECT, verbose_name='职业方向')
    # 在该职业方向上工作的时间
    career_work_year = models.IntegerField(verbose_name='从业时间')
    # 具体方向
    skill = models.ForeignKey(Skills, on_delete=models.PROTECT, verbose_name='具体职业')
    # 技能关键字
    skill_keywords = models.CharField(max_length=50, verbose_name='技能关键字')


    class Meta:
        verbose_name = "简历"
        verbose_name_plural = verbose_name



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



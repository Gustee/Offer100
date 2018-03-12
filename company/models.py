from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='公司全称')
    logo = models.FileField(upload_to="", default='default.png', verbose_name='公司Logo')
    site = models.CharField(max_length=100, verbose_name='公司网站')
    keywords = models.CharField(max_length=100, verbose_name='公司关键词')
    city = models.CharField(max_length=20, verbose_name='所在城市')
    address = models.CharField(max_length=50, verbose_name='具体地址')
    field = models.CharField(max_length=20, verbose_name='所在领域')
    scale = models.CharField(max_length=20, choices=(('s', '15以下'), ('m', '15-50人'),
                                      ('l', '50-150人'), ('xl', '150-500人'), ('xxl', '500人以上')), verbose_name='公司规模')
    establish_date = models.DateField(verbose_name='成立时间')
    slogan = models.CharField(max_length=100, verbose_name='公司标语')
    company_profile = models.TextField(max_length=1000, verbose_name='公司详情')
    product_profile = models.TextField(max_length=1000, verbose_name='产品信息')
    welfare = models.CharField(max_length=50, verbose_name='公司福利')

    class Meta:
        verbose_name = "公司信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

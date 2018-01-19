from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='公司全称')
    logo = models.FileField(upload_to="", default='default.png')
    site = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    field = models.CharField(max_length=20)
    scale = models.CharField(max_length=20, choices=(('s', '15以下'), ('m', '15-50人'),
                                      ('l', '50-150人'), ('xl', '150-500人'), ('xxl', '500人以上')))
    establish_date = models.DateField()
    slogan = models.CharField(max_length=100)
    company_profile = models.TextField(max_length=1000)
    product_profile = models.TextField(max_length=1000)
    welfare = models.CharField(max_length=50)

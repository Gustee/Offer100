from django.db import models
from users.models import *
from job.models import *

# Create your models here.

class Like(models.Model):
    Candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, null=True, blank=True, verbose_name="候选人")
    Job = models.ForeignKey(Job, on_delete=models.PROTECT, null=True, blank=True, verbose_name="职位")

    class Meta:
        verbose_name = "用户收藏职位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Candidate.name


class Apply(models.Model):
    Candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, null=True, blank=True, verbose_name="候选人")
    Job = models.ForeignKey(Job, on_delete=models.PROTECT, null=True, blank=True, verbose_name="职位")

    class Meta:
        verbose_name = "用户申请职位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Candidate.name
# Generated by Django 2.0.1 on 2018-03-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr',
            name='company',
        ),
        migrations.AddField(
            model_name='hr',
            name='position',
            field=models.CharField(default='', max_length=20, verbose_name='职位'),
        ),
    ]

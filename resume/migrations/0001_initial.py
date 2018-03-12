# Generated by Django 2.0.1 on 2018-03-12 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='职业方向')),
            ],
            options={
                'verbose_name': '职业方向',
                'verbose_name_plural': '职业方向',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='个人描述')),
                ('zhihu', models.CharField(max_length=100, verbose_name='知乎')),
                ('blog', models.CharField(max_length=100, verbose_name='博客')),
                ('personal_site', models.CharField(max_length=100, verbose_name='个人网站')),
                ('github', models.CharField(max_length=100, verbose_name='github')),
                ('work_experience', models.TextField(default='', max_length=1000, verbose_name='工作经验')),
                ('edu_experience', models.TextField(default='', max_length=1000, verbose_name='教育')),
                ('career_work_year', models.IntegerField(verbose_name='从业时间')),
                ('skill_keywords', models.CharField(max_length=50, verbose_name='技能关键字')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.Careers', verbose_name='职业方向')),
            ],
            options={
                'verbose_name': '简历',
                'verbose_name_plural': '简历',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='具体职业')),
                ('belong_careers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.Careers')),
            ],
            options={
                'verbose_name': '具体职业',
                'verbose_name_plural': '具体职业',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.Skills', verbose_name='具体职业'),
        ),
    ]

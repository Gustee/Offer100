# Generated by Django 2.0.1 on 2018-03-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='HR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.HR', verbose_name='HR'),
        ),
    ]

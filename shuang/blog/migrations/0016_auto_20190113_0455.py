# Generated by Django 2.1.5 on 2019-01-12 20:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190113_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criticism',
            name='content',
            field=models.TextField(max_length=600, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='评语'),
        ),
        migrations.AlterField(
            model_name='criticism',
            name='critic',
            field=models.CharField(max_length=50, verbose_name='署名'),
        ),
    ]

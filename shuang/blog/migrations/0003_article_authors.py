# Generated by Django 2.1.5 on 2019-01-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190108_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.CharField(default='yiwowa', max_length=50, verbose_name='博客作者'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='博客标题')),
                ('category', models.CharField(blank=True, max_length=50, verbose_name='博客标签')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]

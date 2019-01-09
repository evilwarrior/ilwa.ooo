#coding:utf8
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField

class Article(models.Model):
    # 博客标题
    title = models.CharField(u"博客标题", max_length=100)
    # 博客作者
    authors = models.CharField(u"博客作者（留空默认为添加者名称）", max_length=50, blank=True)
    # 博客分类
    category = models.CharField(u"博客分类（默认值为日记）", max_length=50, blank=True, default='日记')
    # 博客标签
    tags = models.CharField(u"博客标签（逗号分隔）", max_length=200, blank=True)
    # 博客发布日期
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    # 博客文章正文
    content = UEditorField(width=600, height=300, toolbars="besttome", imagePath="images/", filePath="files/", upload_settings={"imageMaxSize":1204000}, settings={}, verbose_name='内容')

    def __unicode__(self):
        return self.title

    class Meta:     #按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"

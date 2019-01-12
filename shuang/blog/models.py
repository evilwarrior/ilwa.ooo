#coding:utf8
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from django.conf import settings
from django.core.validators import MinLengthValidator
from DjangoUeditor.models import UEditorField
# python其他模块
import os
import uuid
from datetime import datetime as datime

# 博客文章类
class Article(models.Model):
    title = models.CharField("标题", max_length=100)
    authors = models.CharField("作者（留空默认为添加者名称）", max_length=50, blank=True)
    category = models.CharField("分类（默认值为日记）", max_length=50, blank=True, default='日记')
    tags = models.CharField("标签（逗号分隔）", max_length=200, blank=True)
    pub_date = models.DateTimeField("发布日期", auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    content = UEditorField(width=600, height=300, toolbars="besttome", imagePath="images/", filePath="files/", upload_settings={"imageMaxSize":1204000}, settings={}, verbose_name='')

    # 作为外键时显示id 标题 作者
    def __str__(self):
        tpl = r'{aid}. {title}, {authors}'
        return tpl.format(title=self.title, authors=self.authors, aid=self.id)

    def __unicode__(self):
        return self.title

    #按时间下降排序
    class Meta:
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"

# 博客评论::定义上传头像的路径
def portrait_path(instance, filename):
    whole = filename.split('.')
    time_string = datime.strftime(datime.now(), '%Y%m%d%H%M%S')
    uid_sample = uuid.uuid4().hex[:3]
    filename = '{}_{}_{}.{}'.format(whole[:-1], time_string, uid_sample, whole[-1])
    return os.path.join("portraits", filename)

# 博客评论类
class Criticism(models.Model):
    validate_content = MinLengthValidator(5)
    article = models.ForeignKey(Article, verbose_name="关联文章", on_delete=models.CASCADE, default=1)
    critic = models.CharField("署名", max_length=50)
    portrait = models.ImageField("头像", upload_to=portrait_path, blank=True)
    content = models.TextField("评语", max_length=600, validators=[validate_content])
    pub_date = models.DateTimeField("发布日期", auto_now_add=True, editable=True)

    # 头像字段使用图片代替路径显示
    def portrait_form(self):
        return format_html(
                '<a target="_blank" href="{0}"><img src="{0}" style="max-width:70px;max-hight:70px" /></a>',
                self.portrait.url,
        )
    portrait_form.short_description = '正在使用的头像'

    # 若评语长度超过15字时缩略
    def abbr_content(self):
        if len(str(self.content)) > 15:
            return '{}...'.format(str(self.content[0:15]))
        else:
            return str(self.content)
    abbr_content.allow_tags = True
    abbr_content.short_description = '內容'

    def __str__(self):
        tpl = r'{cid}. at {title}, {critic}'
        return tpl.format(critic=self.critic, title=self.article.title, cid=self.id)

    def __unicode__(self):
        return self.id

    #按时间下降排序
    class Meta:
        ordering = ['-pub_date']
        verbose_name = "评论"
        verbose_name_plural = "评论"

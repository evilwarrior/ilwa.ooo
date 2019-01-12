#coding:utf8
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Select, TextInput, FileInput, Textarea, CharField
from blog.models import Criticism

class CriticismForm(ModelForm):

    class Meta:
        model = Criticism
        fields = ['article', 'critic', 'portrait', 'content', ]
        widgets = {
            'article': Select(attrs={
                "style": "display:none",
            }),
            'critic': TextInput(attrs={
                "class": "commf-crit-form",
            }),
            'portrait': FileInput(attrs={
                "class": "commf-portr-form",
                "onchange": "change",
            }),
            'content': Textarea(attrs={
                "class": "commf-ctent-form",
            }),
        }
        labels = {
            'critic': _('Pseudonym'),
            'portrait': _('Avatar'),
            'content': _('Comment'),
        }
        error_messages = {
            'critic': {
                'max_length': _("别名请控制在50字以内qqqxx。"),
                'required': _("行，但是可以起个别名先么。"),
            },
            'content': {
                'max_length': _("评论请控制在600字以内qqqxx。"),
                'required': _("填点什么吧，，，"),
                'min_length': _('评语不要小于5字qqqxx。'),
            },
        }


# coding: utf-8
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from workshops.models import Application

register = template.Library()

def prime_or_not_str(appl):
    if appl.is_reserve:
        return u'резервный'
    else:
        return u'основной'

@register.filter
def workshops(obj):
    ret = u"<ol>"
    for a in Application.objects.filter(applicant=obj):
        ret += u'<li>%s (%s выбор)</li>' % (a.workshop, prime_or_not_str(a))
    return mark_safe(ret + u"</ol>")

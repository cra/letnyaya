# coding: utf-8
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


def twitlink(obj):
    link = obj.twitter
    if (link is not None) and (len(link) > 0):
        return u'<a href="http://twitter.com/%s"><img src="%s/twitter-icon.png" alt="icon-twi"></a>' % (link, settings.STATIC_URL)
    return u""


def vklink(obj):
    link = obj.vk_group
    if (link is not None) and (len(link) > 0):
        return u'<a href="http://vk.com/%s"><img src="%s/vkontakte-icon.png" alt="icon-vk"></a>' % (link, settings.STATIC_URL)
    else:
        return u""


def mail_link(obj):
    link = obj.leader
    return u'<a href="mailto:%s"><img src="%s/mail-icon.png" alt="icon-mail"></a>' % (link, settings.STATIC_URL)


def blog_link(obj):
    link = obj.blog_link
    if (link is not None) and (len(link) > 0):
        return u'<a href="%s">Блог</a>' % (link,)
    else:
        return u""

def site_link(obj):
    link = obj.site_link
    if (link is not None) and (len(link) > 0):
        return u'<a href="%s">www</a>' % (link,)
    else:
        return u""

@register.filter
def social(obj, autoescape=None):
    return mark_safe("\n".join(map(
        lambda f: u"%s" % f(obj), [site_link, blog_link, twitlink, vklink, mail_link])
    ))

social.needs_autoescape = True

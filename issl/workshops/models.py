# coding: utf-8

from django.db import models
from django.core.urlresolvers import reverse

from applications.models import Applicant


class Workshop(models.Model):
    ''' Внутренний класс мастерской '''
    slug = models.SlugField(max_length=200, null=True)
    name = models.CharField(max_length=200,
        verbose_name=u'Название мастерской')
    short_name = models.CharField(max_length=200,
        verbose_name=u'Короткое название мастерской',
        help_text=u"Так отобржается в списке и в анкете")
    leader = models.EmailField(u'Контактный адрес')
    subleader = models.EmailField(u'Контактный адрес запасного руководителя')
    about = models.TextField(u'О мастерской')
    badge = models.ImageField(u'Эмблема', upload_to='badges/%Y-%m-%d/')
    visible = models.BooleanField(u'Видна в списке', help_text=u"Если не готова к отображению, лучше галочку снять")
    about_leader = models.TextField(u'О руководителях', max_length=1000, help_text=u"Можно несколько различных всяких-разных товарищей, да.", blank=True)

    #notes = models.CharField(max_length=400,
        #verbose_name=u'Какая-то информация о мастерской ещё')
    contacts = models.TextField(max_length=300,
        verbose_name=u'Контакты всякие, свободное поле', blank=True)

    twitter = models.CharField("Twitter", max_length=200, help_text=u"Только имя аккаунта, без префиксов", blank=True)
    vk_group = models.CharField(u"Группа Вконтакте", max_length=200, help_text=u"Всё, что после http://vk.com/", blank=True)
    fb_group = models.CharField(u"Группа Facebook", max_length=200, help_text=u"Полная ссылка", blank=True)
    site_link = models.CharField(u"Уютный сайтег", max_length=200, help_text=u"Полная ссылка", blank=True)
    blog_link = models.CharField(u"Бложег", max_length=200, help_text=u"Полная ссылка", blank=True)

    applicants = models.ManyToManyField(Applicant, through='Application')

    def __unicode__(self):
        return self.short_name


class Application(models.Model):
    ''' представление заявки в системе '''
    applicant = models.ForeignKey(Applicant)
    workshop = models.ForeignKey(Workshop)
    is_reserve = models.BooleanField(u"Резервный выбор")
    is_accepted = models.NullBooleanField(u"Принят", default=None)
    is_interviewed = models.BooleanField(u"Отсобеседован")
    comment = models.TextField(u"Комментарий к заявке", max_length=1000, blank=True)
    date_submitted = models.DateField(u"Дата подачи заявки")
    leaders_notified = models.BooleanField(u"Мастерская осведомлена", help_text=u"Лидер и запасной лидер знают об этой заявке")

    edit_link = models.CharField(u"Хэш: редактирование статусов заявки", 
            help_text=u"Служебное поле. Очень секьюрно же, гг",
            max_length=200)

    def __unicode__(self):
        return u"%s хочет в '%s' (%s)" % (
                self.applicant,
                self.workshop.short_name,
                u"резерв" if self.is_reserve else u"приоритетно")

    def control_msg(self):
        return u"""Управление анкетой: http://letnyayashkola.org%s""" % reverse('application_edit', args=[self.edit_link])

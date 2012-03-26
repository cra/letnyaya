# encoding: utf-8

from django.db import models
from django import forms


class Applicant(models.Model):
    ''' Модель подающего заявку участника. Большая часть полей анкеты просто хранится текстом
    '''

    ## personal stuff
    name = models.CharField(max_length=150,
            verbose_name=u'Полное Имя',)
    city = models.CharField(max_length=100,
            verbose_name=u'Город')
    email = models.EmailField(u'e-mail')
    telephone = models.CharField(u'Телефон', max_length=15)
    age = models.PositiveIntegerField(u'Возраст')
    photo = models.ImageField(u'Фото', upload_to='applicant-photos/%Y-%j-%H_%M_%S/')

    ## activity in environmental conditions
    workplace = models.TextField(u"Место работы", max_length=300)
    job = models.CharField(u"Специальность", max_length=300)
    onboard = models.TextField(u"Активность на ЛШ", max_length=500)

    ## activity on school
    been_before = models.CharField(u"Ездил ли раньше", max_length=300)
    how_long = models.TextField(u"Срок (предположительно)", max_length=800) 

    ## 
    courses = models.TextField(u"Курсы", max_length=500)
    dosug = models.TextField(u"Досуг", max_length=500)

    money = models.CharField(u"Деньги/день", max_length=150)
    questions = models.TextField(u'Вопросы', max_length=1000,)

    comment = models.TextField(u"Полуавтоматический комментарий", max_length=1000, blank=True)

    view_link = models.CharField(u"Хэш: информацию по заявке", 
            help_text=u"Служебное поле. Инфа по заявке",
            max_length=200)

    is_approved = models.BooleanField(u"email подтверждён")

    def __unicode__(self):
        return u"%s" % self.name 

    def nice_representation(self):
        return u"""
Содержимое заполненной анкеты
-----------------------------

[ Персональная информация ]

Полное имя желающего: %s
Откуда: %s
e-mail: %s
телефон: %s
возраст: %s
ссылка на фото: http://letnyayashkola.org/%s (also, см. приложение)
""" % (self.name, self.city, self.email, self.telephone, self.age, self.photo.url) + u"""
[ Активность в обычной жизни ]
Где работает: \n%s
По жизни кто: \n%s
Что хочет делать на ЛШ: \n%s
""" % (self.workplace, self.job, self.onboard) + u"""
[ Активность на ЛШ ]
Был раньше: \n%s
Примерный срок: \n%s
Что хочет рассказать: \n%s
Предложил досуг: \n%s
""" % (self.been_before, self.how_long, self.courses, self.dosug) + u"""
Про деньги: %s

Вопросы: \n%s

Какой-то комментарий от 'системы', если есть, будет ниже: \n%s
""" % (self.money, self.questions, self.comment or u"Нет ничего")


    def onsite_representation(self):
        ''' can't make it work though :( '''
        return u"""
# Содержимое заполненной анкеты

## Персональная информация

1. **Полное имя желающего**: %s
2. **Откуда**: %s
3. **e-mail**: %s
4. **телефон**: %s
5. **возраст**: %s
6. **фотка будет**
""" % (self.name, self.city, self.email, self.telephone, self.age) + u"""
## Активность в обычной жизни
7. **Где работает**: 
   <p style='white-space:pre'> \n%s</p>

8. **Специальность**: \n%s
9. **Что хочет делать на ЛШ**: \n%s
""" % (self.workplace, self.job, self.onboard) + u"""
## Активность на ЛШ
0. **Был раньше**: \n%s
1. **Примерный срок**: \n%s
2. **Что хочет рассказать**: \n%s
3. **Идеи досуга**: \n%s
""" % (self.been_before, self.how_long, self.courses, self.dosug) + u"""
## Прочее
1. *Про деньги*: %s
2. *Вопросы*: \n%s
""" % (self.money, self.questions)

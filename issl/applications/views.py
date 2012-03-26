# encoding: utf-8

import os
from datetime import datetime

from django import forms
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from annoying.decorators import render_to

from applications.models import Applicant
from workshops.models import Workshop, Application


class PersonalForm(forms.Form):
    name = forms.CharField(label=u"Имя", max_length=100)
    surname = forms.CharField(label=u"Фамилия", max_length=100)
    second_name = forms.CharField(label=u"Отчество", max_length=100, required=False)
    city = forms.CharField(label=u"Город, где вы постоянно живёте", 
            help_text=u"Если город малоизвестный, укажите ещё и область")
    email = forms.EmailField(label=u"Электронная почта") 
    telephone = forms.CharField(label=u"Ваш мобильный телефон")
    age = forms.IntegerField(label=u"Возраст", min_value=4, max_value=150)
    photo = forms.ImageField(label=u"Фотка", 
            help_text=u"Желательно, чтобы файл был не больше 500Кб и было видно лицо")

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', False)
        if photo:
            if photo._size > 1024*1024:
                raise ValidationError(u"Картинка слишком большая (> 1mb).")
            return photo
        else:
            raise ValidationError(u"Не смог прочитать загруженную картинку")



class ApplicantForm(forms.Form):
    primary_workshop = forms.ModelChoiceField(
            label=u"Приоритетная мастерская", 
            queryset=Workshop.objects.all(),
            required=True,)
    reserve_workshop = forms.ModelChoiceField(
            label=u"Запасная мастерская", 
            queryset=Workshop.objects.all(),
            required=True,)


ONBOARD_CHOICES = [
    (0, u"В первую очередь, преподавать"),
    (1, u"В первую очередь, учиться"),
    (2, u"Помимо прочего, быть куратором школьников"),
    (3, u"Помимо прочего, заниматься организационными вопросами"),
    (4, u"Помимо прочего, заниматься хозяйственными вопросами"),
]

class AdditionalInfoForm(forms.Form):
    workplace = forms.CharField(
            label=u"Место работы", 
            widget=forms.Textarea, 
            help_text=u"Где вы учитесь, работаете, проявляете общественную активность. "
                      u"Рекомендуется отвечать подробно (но не более 500 знаков)", 
            max_length=500)
    job = forms.CharField(
            label=u"Специальность", 
            widget=forms.Textarea, 
            help_text=u"Как бы вы определили вашу главную специальность "
                      u"(медик, журналист, физик и т.п.)",
            max_length=300)
    onboard = forms.MultipleChoiceField(
            label=u"Что бы вы хотели делать на Летней Школе?", 
            choices=ONBOARD_CHOICES,
            help_text=u"Куратор школьников это что-то типа вожатого. Оргвопросы - в основном, составление расписаний и т.п. Хозяйственные вопросы - кухня, строительство и пр.",
            required=True,
            widget=forms.widgets.CheckboxSelectMultiple,)


class SchoolForm(forms.Form): 
    been_before = forms.MultipleChoiceField(
            label=u"Ездили ли вы раньше на Летнюю Школу?", 
            choices=[(t, u"%s" % t) for t in xrange(2004, datetime.today().year)],
            required=False,
            help_text=u"Если не ездили, просто не ставьте никаких галочек",
            widget=forms.widgets.CheckboxSelectMultiple,)
    how_long = forms.MultipleChoiceField(
            label=u"На какой срок (предположительно вы сможете приехать Летнюю Школу?", 
            choices=[
                (0, u"Почти на весь срок (25-35 дней)"),
                (1, u"На 2-3 учебных цикла"),
                (2, u"На один учебный цикл (6-7 дней)"),
                (3, u"Другое"),
            ],
            help_text=u'Если вы выбрали пункт "Другое", разверните свой ответ ниже',
            required=True,
            widget=forms.widgets.CheckboxSelectMultiple,)
    how_long_comment = forms.CharField(
            label=u"Комментарий к срокам. Что угодно про время вашего пребывания, коротко.", 
            required=False,
            widget=forms.Textarea,
            max_length=300)
    courses = forms.CharField(
            label=u"Курсы и лекции", 
            help_text=u"Какие курсы и разовые лекции вы готовы (хотя бы гипотетически) прочитать? На какие темы вы хотели бы организовать дискуссии, тренинги, мастер-классы?",
            required=False,
            widget=forms.Textarea,
            max_length=500)
    dosug = forms.CharField(
            label=u"Какие досугово-развлекательные мероприятия вы хотели бы предложить?",
            required=False,
            widget=forms.Textarea,
            max_length=500)


class MoneyForm(forms.Form):
    money = forms.ChoiceField(
            label=u"Какая сумма оплаты за день кажется вам адекватной?", 
            choices=[(t, u"%s руб." % t) for t in xrange(100, 501, 50)] \
                    + [(-1, u"более 500 руб.")],
            required=True,)


class QuestionsForm(forms.Form):
    questions = forms.CharField(
            label=u"Какие вопросы вы хотели бы задать организаторам Летней Школы?",
            required=False,
            widget=forms.Textarea,
            max_length=1000)

def test_mail(request):
    ''' Просто проверка, что почта работает. Ничего личного
    '''

    send_mail(u'Test', 
            u'Mensaje. Hi there. Also, тест русских букв. %s' % datetime.now(),
            'from_me_darling@example.com', 
            ['c6h10o5@gmail.com'], 
            fail_silently=False)

    return redirect('home')


def new_hash():
    ''' сгенерировать новый хэш '''
    return os.urandom(20).encode('hex')


@render_to('apply.html')
def apply(request):
    ''' Подать заявку на участие
    '''
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST, request.FILES)
        applicant_form = ApplicantForm(request.POST)
        additional_info_form = AdditionalInfoForm(request.POST)
        school_form = SchoolForm(request.POST)
        money_form = MoneyForm(request.POST)
        questions_form = QuestionsForm(request.POST)

        if all([f.is_valid() for f in [additional_info_form, school_form, 
                personal_form, applicant_form, questions_form, money_form,
            ]]):

            newbie = Applicant()

            cd = personal_form.cleaned_data
            newbie.name = u' '.join(u'%s' % cd.get(t) \
                    for t in ['surname', 'name', 'second_name'])
            for t in ['city', 'email', 'telephone', 'age']:
                newbie.__dict__[t] = cd.get(t)
            newbie.photo = cd['photo']

            cd = additional_info_form.cleaned_data
            for t in ['workplace', 'job']:
                newbie.__dict__[t] = cd.get(t)

            newbie.onboard = '\n'.join([
                dict(additional_info_form.fields['onboard'].choices)[int(choice)]
                for choice in cd.get('onboard')])

            cd = school_form.cleaned_data
            if cd.get('been_before'):
                newbie.been_before = ', '.join([
                    dict(school_form.fields['been_before'].choices)[int(choice)]
                    for choice in cd.get('been_before')])
            else:
                newbie.been_before = u"Раньше не был"
            newbie.how_long = '\n'.join([
                dict(school_form.fields['how_long'].choices)[int(choice)]
                for choice in cd.get('how_long')])
            if cd.get('how_long_comment'):
                newbie.how_long += u"\nКомментарий: '%s'" % cd.get('how_long_comment')
            for t in ['courses', 'dosug']:
                newbie.__dict__[t] = cd.get(t)

            cd = money_form.cleaned_data
            newbie.money = u"%s/день" % dict(money_form.fields['money'].choices)[int(cd.get('money'))]

            cd = questions_form.cleaned_data
            newbie.questions = cd.get('questions')

            newbie.view_link = new_hash()

            newbie.comment = u"Время заполнения анкеты %s" % datetime.now()

            newbie.save()

            ## submit applications
            cd = applicant_form.cleaned_data
            primary_workshop = get_object_or_404(Workshop, pk=cd.get('primary_workshop').pk)
            reserve_workshop = get_object_or_404(Workshop, pk=cd.get('reserve_workshop').pk)
            
            primary_hash = new_hash()
            app_primary = Application(applicant=newbie,
                    workshop=primary_workshop,
                    is_reserve=False,
                    is_accepted=None,
                    is_interviewed=False,
                    edit_link=primary_hash,
                    date_submitted=datetime.today())
            app_primary.save()

            app_reserve = u""
            if primary_workshop != reserve_workshop:
                reserve_hash = new_hash()
                app_reserve = Application(applicant=newbie,
                        workshop=reserve_workshop,
                        is_reserve=True,
                        is_accepted=None,
                        is_interviewed=False,
                        edit_link=reserve_hash,
                        date_submitted=datetime.today())
                app_reserve.save()

            #TODO: Whistles
            #return redirect('home')


            bounce_text =  u'''
Ваша заявка принята.

Ссылка на подверждение: http://letnyayashkola.org%s 

Чтобы подтвердить вашу заявку, перейдите по ссылке с подтверждением и нажмите кнопку "Подтвердить"

''' % reverse('applicant_view', args=[newbie.view_link])


            # TODO: check email вдруг уже был такой подан
            if settings.SEND_MAIL:
                send_mail(u'Летняя Школа 2012. Заявка принята', 
                        bounce_text + settings.MAIL_CODA,
                        'mailmonkey@letnyayashkola.org', 
                        [newbie.email],
                        fail_silently=False)

            return redirect('application-success')

    else:
        personal_form = PersonalForm()
        applicant_form = ApplicantForm()
        additional_info_form = AdditionalInfoForm()
        school_form = SchoolForm()
        money_form = MoneyForm(initial={'money': 250})
        questions_form = QuestionsForm()

    return {'personal_form': personal_form,
            'applicant_form': applicant_form,
            'additional_info_form': additional_info_form,
            'school_form': school_form,
            'money_form': money_form,
            'questions_form': questions_form,
            }


def approve(request, view_link):
    ''' Подтвердить данные о данном подающем '''

    applicant = get_object_or_404(Applicant, view_link=view_link)

    if not applicant.is_approved:
        if settings.SEND_MAIL:

            approve_time = datetime.now()

            preamble_text = u"""
Ващемпта, такие дела, малята. Кто-то захотел на вашу мастерскую и заполнил анкетку на сайте.

Это человек был настолько твёрд в своих решениях, что даже подтвердил свою анкету!! На часах было %s (охренеть точность, ога? Кстати, это московское время).
""" % approve_time
            
            for app in Application.objects.filter(applicant=applicant):
                subject = u"Application: %s" \
                        % (u'reserve' if app.is_reserve else u'priority')
                #FIXME fail_silently is a bad idea
                email = EmailMessage(subject, 
                        preamble_text \
                        + u"\n(Мастерская: %s)\n" % app.workshop \
                        + applicant.nice_representation() \
                        + app.control_msg() \
                        + settings.MAIL_CODA,
                    'mailmonkey@letnyayashkola.org', 
                    set([app.workshop.leader, app.workshop.subleader]),
                    settings.BCC_LIST) # last one is bcc
                email.attach_file(os.path.join(settings.MEDIA_ROOT, applicant.photo.name))
                email.send(fail_silently=True)
                app.leaders_notified = True
                app.save()

        messages.success(request, u"Данные подтверждены.")
        messages.success(request, u"Руководители мастерских осведомлены")
        applicant.is_approved = True
        applicant.comment += u"\ne-mail подтверждён %s" % approve_time
        applicant.save()
    else:
        messages.error(request, u"Такие данные уже подтверждены")

    return redirect('applicant_view', slug=view_link)

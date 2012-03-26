# coding: utf8

from django import forms
from django.shortcuts import get_object_or_404, redirect
from annoying.decorators import render_to

from workshops.models import Application


class PersonalForm(forms.Form):
    ''' форма заявки '''
    comment = forms.CharField(label=u"Имя", max_length=500)


@render_to('application/edit_application.html') 
def edit_application(request, edit_link):
    ''' редактирование заявки '''

    #Application.objects.select_related.get(edit_link=edit_link)
    application = get_object_or_404(Application, edit_link=edit_link)

    return {'applicant': application.applicant,
            'workshop': application.workshop,
            'application': application}


def examined_application(request, edit_link):
    ''' "отсобеседование" заявки '''

    application = get_object_or_404(Application, edit_link=edit_link)
    application.is_interviewed = True
    application.save()

    return redirect('application_edit', edit_link=edit_link)


def approve_application(request, edit_link):
    ''' подтверждение заявки '''

    application = get_object_or_404(Application, edit_link=edit_link)
    application.is_accepted = True
    application.save()

    return redirect('application_edit', edit_link=edit_link)


from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from workshops.models import Workshop, Application
from applications.models import Applicant

w_qs = Workshop.objects.filter(visible=True)
application_qs = Application.objects.all()
applicant_qs = Applicant.objects.all()

urlpatterns = patterns('',
    #url(r'^issl/', include('issl.foo.urls')),

    url(r'^$',
        'django.views.generic.list_detail.object_list', 
        {'queryset':w_qs, 'template_name':'home.html'},
        name='home'),


    url(r'^robots\.txt$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),


    url(r'^apply/$',
        'applications.views.apply',
        name='apply'),

    url(r'^test-mail/$',
        'applications.views.test_mail'),

    url(r'^apply-success/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'application/success.html'},
        name='application-success'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<slug>[-\w]+)/$',
        'django.views.generic.list_detail.object_detail', 
        {'queryset':w_qs, 'template_name':'workshop/about.html'},
        name='workshop_about'),

    url(r'^a/(?P<slug>[-\w]+)/$',
        'django.views.generic.list_detail.object_detail',
            {'queryset':applicant_qs, 
             'template_name':'application/view_applicant.html', 
             'template_object_name': 'applicant',
             'slug_field': 'view_link'},
        name='applicant_view'),

    url(r'^a/(?P<view_link>[-\w]+)/approve/$',
        'applications.views.approve',
        name='approve_applicant'),

    url(r'^a/edit/(?P<edit_link>[-\w]+)/$',
        'workshops.views.edit_application',
        name='application_edit'),

    url(r'^a/edit/(?P<edit_link>[-\w]+)/examined$',
        'workshops.views.examined_application',
        name='application_examined'),

    url(r'^a/edit/(?P<edit_link>[-\w]+)/approved$',
        'workshops.views.approve_application',
        name='application_approved'),
)

urlpatterns += staticfiles_urlpatterns()

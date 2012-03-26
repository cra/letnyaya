# coding: utf-8

from workshops.models import Workshop, Application
from django.contrib import admin

def publish(modeladmin, request, queryset):
    queryset.update(visible=True)
publish.short_description = u"Сделать видимыми выбранные мастерские"

def unpublish(modeladmin, request, queryset):
    queryset.update(visible=False)
unpublish.short_description = u"Спрятать выбранные мастерские"

class WorkshopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('slug', 'name', 'leader', 'subleader', 'visible')
    actions = [publish, unpublish]

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 
        'date_submitted', 
        'leaders_notified',
        'is_interviewed',
        'is_accepted', 
    )

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Application, ApplicationAdmin)

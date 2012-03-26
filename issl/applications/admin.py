from django.contrib import admin
from applications.models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'telephone', 'is_approved')

admin.site.register(Applicant, ApplicantAdmin)

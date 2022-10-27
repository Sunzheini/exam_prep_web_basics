from django.contrib import admin

from exam_prep_web_basics.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

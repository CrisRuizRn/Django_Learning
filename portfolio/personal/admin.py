from django.contrib import admin
from personal.models import Skill, Education, Work, SuccessStory

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    pass


class WorkAdmin(admin.ModelAdmin):
    pass


class SuccessAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(SuccessStory, SuccessAdmin)
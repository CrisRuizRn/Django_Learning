from django.contrib import admin
from personal.models import Skill, Education, Work, SuccessStory
from projects.models import Technology, Project

# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class SkillAdmin(admin.ModelAdmin):
    pass


class SuccessAdmin(admin.ModelAdmin):
    pass


class TechnologyAdmin(admin.ModelAdmin):
    pass


class WorkAdmin(admin.ModelAdmin):
    pass



admin.site.register(Education, EducationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SuccessStory, SuccessAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Work, WorkAdmin)
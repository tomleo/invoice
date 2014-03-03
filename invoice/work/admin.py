from django.contrib import admin

from .models import Span, Task, Contact, Company, WorkDay, WorkMonth

admin.site.register(Span)

class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

class CompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company, CompanyAdmin)

class WorkDayAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkDay, WorkDayAdmin)

class WorkMonthAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkMonth, WorkMonthAdmin)

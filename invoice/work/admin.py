from django.contrib import admin

from .models import Span, Task, Contact, Company, Day, Month

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
admin.site.register(Day, WorkDayAdmin)

class WorkMonthAdmin(admin.ModelAdmin):
    pass
admin.site.register(Month, WorkMonthAdmin)

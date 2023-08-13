from django.contrib import admin

from task.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("tags",)
    list_filter = ("tags",)


admin.site.register(Tag)

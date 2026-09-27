from django.contrib import admin

from .models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "is_done", "datetime", "deadline",)
    list_filter = ("is_done", "deadline")

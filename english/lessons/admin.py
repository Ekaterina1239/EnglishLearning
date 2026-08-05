from django.contrib import admin

from .models import Lesson, LessonProgress


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "grammar_topic", "reading_text", "test")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "is_completed", "completed_at")
    list_filter = ("is_completed",)
    readonly_fields = [f.name for f in LessonProgress._meta.fields]

    def has_add_permission(self, request):
        return False
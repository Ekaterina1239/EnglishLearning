from django.contrib import admin

from .models import ComprehensionQuestion, ReadingText


class ComprehensionQuestionInline(admin.TabularInline):
    model = ComprehensionQuestion
    extra = 1


@admin.register(ReadingText)
class ReadingTextAdmin(admin.ModelAdmin):
    list_display = ("title", "level")
    list_filter = ("level",)
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ComprehensionQuestionInline]
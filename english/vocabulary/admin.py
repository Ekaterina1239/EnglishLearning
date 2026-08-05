from django.contrib import admin

from .models import VocabularySet, Word


class WordInline(admin.TabularInline):
    model = Word
    extra = 1


@admin.register(VocabularySet)
class VocabularySetAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [WordInline]
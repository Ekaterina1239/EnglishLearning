from django.contrib import admin

from .models import GrammarExample, GrammarTopic


class GrammarExampleInline(admin.TabularInline):
    model = GrammarExample
    extra = 1


@admin.register(GrammarTopic)
class GrammarTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "order")
    list_filter = ("level",)
    search_fields = ("title", "explanation")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GrammarExampleInline]
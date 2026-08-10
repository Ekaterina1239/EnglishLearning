from django.contrib import admin

from .models import Choice, Question, Test, TestAttempt


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "test", "category", "order")
    list_filter = ("test", "category")
    inlines = [ChoiceInline]


@admin.register(TestAttempt)
class TestAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "test", "score_percent", "completed_at")
    list_filter = ("test",)
    readonly_fields = [f.name for f in TestAttempt._meta.fields]

    def has_add_permission(self, request):
        return False
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from lessons.models import Lesson, LessonProgress
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lessons:list")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})


@login_required
def profile(request):
    total_lessons = Lesson.objects.count()
    completed_lessons = LessonProgress.objects.filter(
        user=request.user, is_completed=True
    ).count()
    progress_percent = round((completed_lessons / total_lessons) * 100) if total_lessons else 0

    return render(request, "users/profile.html", {
        "total_lessons": total_lessons,
        "completed_lessons": completed_lessons,
        "progress_percent": progress_percent,
    })
from django.shortcuts import get_object_or_404, render
from .models import ReadingText


def text_list(request):
    texts = ReadingText.objects.all()
    return render(request, 'reading/list.html', {'texts': texts})


def text_detail(request, slug):
    text = get_object_or_404(ReadingText, slug=slug)
    return render(request, 'reading/detail.html', {'text': text})
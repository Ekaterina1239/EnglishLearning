from django.shortcuts import get_object_or_404, render
from .models import VocabularySet


def set_list(request):
    sets = VocabularySet.objects.all()
    return render(request, 'vocabulary/list.html', {'sets': sets})


def set_detail(request, slug):
    vocab_set = get_object_or_404(VocabularySet, slug=slug)
    return render(request, 'vocabulary/detail.html', {'vocab_set': vocab_set})
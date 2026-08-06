from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VocabularySetForm, WordForm
from .models import VocabularySet, Word


def set_list(request):
    # Показываем официальные наборы (owner=None) + свои личные, если залогинен
    sets = VocabularySet.objects.filter(owner__isnull=True)
    if request.user.is_authenticated:
        sets = VocabularySet.objects.filter(Q(owner__isnull=True) | Q(owner=request.user))
    return render(request, 'vocabulary/list.html', {'sets': sets})


def set_detail(request, slug):
    vocab_set = get_object_or_404(VocabularySet, slug=slug)
    can_edit = request.user.is_authenticated and vocab_set.owner_id == request.user.id
    return render(request, 'vocabulary/detail.html', {'vocab_set': vocab_set, 'can_edit': can_edit})


@login_required
def my_sets(request):
    sets = VocabularySet.objects.filter(owner=request.user)
    return render(request, 'vocabulary/my_sets.html', {'sets': sets})


@login_required
def set_create(request):
    if request.method == "POST":
        form = VocabularySetForm(request.POST)
        if form.is_valid():
            vocab_set = form.save(commit=False)
            vocab_set.owner = request.user
            vocab_set.save()
            return redirect('vocabulary:detail', slug=vocab_set.slug)
    else:
        form = VocabularySetForm()
    return render(request, 'vocabulary/set_form.html', {'form': form, 'is_create': True})


@login_required
def set_edit(request, slug):
    vocab_set = get_object_or_404(VocabularySet, slug=slug, owner=request.user)
    if request.method == "POST":
        form = VocabularySetForm(request.POST, instance=vocab_set)
        if form.is_valid():
            form.save()
            return redirect('vocabulary:detail', slug=vocab_set.slug)
    else:
        form = VocabularySetForm(instance=vocab_set)
    return render(request, 'vocabulary/set_form.html', {'form': form, 'is_create': False})


@login_required
def set_delete(request, slug):
    vocab_set = get_object_or_404(VocabularySet, slug=slug, owner=request.user)
    if request.method == "POST":
        vocab_set.delete()
        return redirect('vocabulary:my_sets')
    return render(request, 'vocabulary/set_confirm_delete.html', {'vocab_set': vocab_set})


@login_required
def word_add(request, slug):
    vocab_set = get_object_or_404(VocabularySet, slug=slug, owner=request.user)
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.vocabulary_set = vocab_set
            word.save()
            return redirect('vocabulary:detail', slug=vocab_set.slug)
    else:
        form = WordForm()
    return render(request, 'vocabulary/word_form.html', {'form': form, 'vocab_set': vocab_set})


@login_required
def word_delete(request, slug, word_id):
    vocab_set = get_object_or_404(VocabularySet, slug=slug, owner=request.user)
    word = get_object_or_404(Word, id=word_id, vocabulary_set=vocab_set)
    word.delete()
    return redirect('vocabulary:detail', slug=vocab_set.slug)
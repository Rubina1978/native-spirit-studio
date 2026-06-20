from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Reflection
from .forms import ReflectionForm
from django.contrib.auth.decorators import login_required
import random

quotes = [
    ("When you want something, \
        all the Universe conspires in helping you to achieve it",
        "Paulo Coelho"),
    ("The secret of life is to fall seven times and to get up the eight times",
     "Paulo Coelho"),
    ("Remember your dreams and fight for them.\
        You must know what you want from life", "Paulo Coelho"),
    ("Faith loves the journey. Gratitude loves the moment. \
        Inner peace loves the pause.", "Maxime Lagace"),
    ("One small positive thought can change your whole day", "Zig Ziglar"),
    ("Success is walking from failure to failure with no loss of enthusiasm",
     "Winston Churchil"),
    ("It does not matter how slowly you go as long as you do not stop",
        "Confucius"),
    ("I am thankful to all who said no to me. \
     It is because of them that I'm doing it myself.",
        "Albert Einstein"),
    ("Miracles happen to those who believe in them", "Bernard Berenson"),
    ("Write it in your heart that every day is the best day in the year.",
     "Ralph Waldo Emerson"),
    ("Change your thoughts and you change your world.", "Vincent Peale"),
    ("Believe you can and you're half way there.", "Theodore Roosevelt")
]


@login_required
def journal(request):
    reflections = Reflection.objects.filter(
        user=request.user
        ).order_by('-created_on')

    context = {
        'reflections': reflections,

    }
    return render(request, 'journal/journal.html', context)


@login_required
def add_reflection(request):
    quote, author = random.choice(quotes)
    if request.method == 'POST':
        form = ReflectionForm(request.POST)
        if form.is_valid():
            reflection = form.save(commit=False)
            reflection.user = request.user
            reflection.save()

            messages.success(
                request, "Your reflection was successfully added")

        else:
            messages.error(
                request, "An error occured when adding reflection.\
                    Please check if form is valid and try again later")

        return redirect('journal')

    else:
        form = ReflectionForm()

    context = {
            'form': form,
            'quote': quote,
            'author': author,
        }
    return render(request, 'journal/add_reflection.html', context)


@login_required
def edit_reflection(request, reflection_id):
    reflection = get_object_or_404(
         Reflection, pk=reflection_id, user=request.user)

    if request.method == 'POST':

        form = ReflectionForm(request.POST, instance=reflection)
        if form.is_valid():
            form.save()
            messages.success(
                request, "your reflection was successfully edited.")
            return redirect(reverse('journal'))
    else:
        form = ReflectionForm(instance=reflection)
        messages.error(
            request, "An error occured when editing reflection, \
            please try again later.")

    context = {
        'form': form,
        'reflection': reflection,
    }

    return render(request, 'journal/add_reflection.html', context)


@login_required
def delete_reflection(request, reflection_id):
    reflection = get_object_or_404(
         Reflection, pk=reflection_id, user=request.user)

    reflection.delete()
    messages.success(request, "Reflection successfully deleted.")

    return redirect('journal')

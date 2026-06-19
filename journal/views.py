from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Reflection
from .forms import ReflectionForm
from django.contrib.auth.decorators import login_required


# Create your views here.

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

    if request.method == 'POST':
        form = ReflectionForm(request.POST)
        if form.is_valid():
            reflection = form.save(commit=False)
            reflection.user = request.user
            reflection.save()
            messages.success(request, "Your reflection was successfully added")

            return redirect('journal')

    else:
        form = ReflectionForm()
        messages.error(
            request, "An error occured when adding reflection. \
            Please xheck if form is valid and try again later")

    context = {
            'form': form
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

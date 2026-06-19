from django.shortcuts import render, get_object_or_404, redirect, reverse
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

            return redirect('journal')

    else:
        form = ReflectionForm()

    context = {
            'form': form
        }
    return render(request, 'journal/add_reflection.html', context)


def edit_reflection(request, reflection_id):
    reflection = get_object_or_404(
         Reflection, pk=reflection_id, user=request.user)

    if request.method == 'POST':

        form = ReflectionForm(request.POST, instance=reflection)
        if form.is_valid():
            form.save()
            return redirect(reverse('journal'))
    else:
        form = ReflectionForm(instance=reflection)
    
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
    
    return redirect('journal')



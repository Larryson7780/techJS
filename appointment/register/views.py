from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Inscription réussie")
        else:
            messages.info(request, "votre mot de passe doit contenir au moins 8 caractères / votre mot de passe ne peut pas être un mot de passe couramment utilisé / votre mot de passe ne peut pas être entièrement numérique")
    context = {'form': form}
    return render(request, 'registration/register.html', context)

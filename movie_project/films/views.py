from django.shortcuts import render, redirect
from .models import Film
from .forms import Film_form

def home(request):
	films = Film.objects.all()
	return render(request, 'films/index.html', {"films": films, "active": 1})

def add_film(request):
	error = ''
	if request.method == 'POST':
		form = Film_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = "Данные были заполнены некорректно" 
	form = Film_form()
	return render(request, 'films/new.html', {'form': form, 'error': error})
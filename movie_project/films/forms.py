from .models import Film
from django.forms import ModelForm, TextInput, Textarea

class Film_form(ModelForm):
	class Meta:
		model = Film
		fields = ['title', 'description', 'review']
		widgets = {
			'title': TextInput(attrs={'placeholder': 'Название фильма', 'class': 'form-control', 'required': True}),
			'description': Textarea(attrs={'placeholder': 'Описание фильма', 'class': 'form-control', 'rows': '3', 'required': True}),
			'review': Textarea(attrs={'placeholder': 'Отзыв о фильме', 'class': 'form-control', 'rows': '3', 'required': True}),
		}
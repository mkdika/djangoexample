from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Author
from .forms import AuthorForm

# Create your views here.

def authors(request):
  
  print(">>>>>>>>>>>>>>>>>>>>>>>")

  author_list =  Author.objects.all()
  form = AuthorForm()

  response_dict = {
    'list':author_list,
    'form':form,
  }
    
  return render(request, 'formcomponent/authors.html', response_dict)

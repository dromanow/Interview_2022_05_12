from django.shortcuts import render
from django.views.generic import ListView
from .models import Author


class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.all()
    template_name = 'index.html'

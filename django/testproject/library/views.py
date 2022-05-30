from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Bio, Book


class UserListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            # 'user': {'name': 'Denis', 'age': '41'}
        })
        return context


class AuthorListView(UserListView):
    model = Author
    queryset = Author.objects.all()
    template_name = 'index.html'


class BookListView(UserListView):
    model = Book
    # queryset = Bio.objects.select_related('author').all()
    queryset = Book.on_site.prefetch_related('authors').all()
    template_name = 'book.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'user': {'name': 'Denis', 'age': '41'},
            'site': get_current_site(request=self.request)
        })
        return context


class BioListView(UserListView):
    model = Bio
    queryset = Bio.objects.not_deleted().select_related('author').all()
    template_name = 'bio.html'
    # extra_context = {
    #     'user': {'name': 'Denis', 'age': '41'}
    # }

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context.update({
    #         'user': {'name': 'Denis', 'age': '41'}
    #     })
    #     return context


def return_extra():
    return {'name': 'Denis', 'age': '41'}


def get_page(request):
    return render(request, 'index.html', context={
        'object_list': Author.objects.all(),
        'user': return_extra()
    })


def get_page_1(request):
    return render(request, 'index1.html', context={
        'object_list_1': Author.objects.all(),
        'user': return_extra()
    })



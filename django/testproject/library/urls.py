from django.urls import path
from .views import AuthorListView, get_page, BioListView, BookListView

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('bio', BioListView.as_view()),
    path('book', BookListView.as_view()),
    # path('get', get_page)
]

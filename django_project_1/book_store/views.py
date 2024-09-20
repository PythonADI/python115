from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from book_store.models import Author, Book



def author_and_books_view(request: HttpRequest) -> HttpResponse:
    return render(
        request, 
        'store.html',
        {
            'authors': Author.objects.all().order_by('-id')[:5],
            'books': Book.objects.all().order_by('-id')[:5]
        }
    )

class AuthorAndBooksView(TemplateView):
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all().order_by('-id')[:5]
        context['books'] = Book.objects.all().order_by('-id')[:5]
        return context
    

class AuthorListView(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name', 'age']
    success_url = reverse_lazy('author_list_view')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name', 'age']
    success_url = reverse_lazy('author_list_view')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list_view')
    context_object_name = 'author'

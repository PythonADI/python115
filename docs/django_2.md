## Django

### Contents
- [QuerySets](#querysets)
- [Class Based Views (CRUD)](#class-based-views)

### QuerySets
in this example we will use `python manage.py shell` to interact with the database

let's create a new model
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

now let's create some data

we can acess data using the model manager `objects` like this
```python
from myapp.models import Author, Book

# create a new author
author = Author.objects.create(name='John Doe', age=30)

# create a new book
book = Book.objects.create(title='My Book', author=author)

# get all authors
authors = Author.objects.all()

# get all books
books = Book.objects.all()
```

let's create 10 other authors with 10 books each
```python
import random
for i in range(10):
    author = Author.objects.create(name=f'Author {i}', age=random.randint(20, 50))
    for j in range(10):
        Book.objects.create(title=f'Book {j}', author=author)


# create authors without books
# start range from 10 to avoid conflicts with the previous authors
for i in range(10, 20):
    Author.objects.create(name=f'Author {i}', age=random.randint(20, 50))
```

now let's query the database

```python
# get all authors
authors = Author.objects.all()

# get all books
books = Book.objects.all()

# get the first author
author = Author.objects.first()

# get the last author
author = Author.objects.last()

# get the author with id=1
author = Author.objects.get(id=1)

# get the author with name='John Doe'
author = Author.objects.get(name='John Doe')

# filter authors that are older than 30
authors = Author.objects.filter(age__gt=30)

# filter authors that are older than 30 and younger than 40
authors = Author.objects.filter(age__gt=30, age__lt=40)

# filter authors that are younger or equal to 30
authors = Author.objects.filter(age__lte=30)

# let's sort the authors by age
authors = Author.objects.order_by('age')

# let's sort the authors by age in descending order
authors = Author.objects.order_by('-age')

# let's get the first 5 authors
authors = Author.objects.all()[:5]

# let's get the last 5 authors
authors = Author.objects.all()[-5:]

# let's get john doe books
books = Book.objects.filter(author__name='John Doe')

# OR
author = Author.objects.get(name='John Doe')
books = Book.objects.filter(author=author)

# OR
books = author.book_set.all()

# let's get all books that have the word 'book' in the title
books = Book.objects.filter(title__icontains='book')

# Warning with icontains vs contains
# icontains is case insensitive
# contains is case sensitive
# However sqlite cannot use contains it will always be insensitive

# let's get all books that have the word 'book' in the title and the author is older than 30
books = Book.objects.filter(title__icontains='book', author__age__gt=30)

# let's get all authors that have books
authors = Author.objects.filter(book__isnull=False)

# let's get all authors that don't have books
authors = Author.objects.filter(book__isnull=True)
```

app/views.py
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'authors': Author.objects.all(),
        'books': Book.objects.all()
    })
```


### Class Based Views
Django provides a set of class-based views that can be used to create CRUD views with minimal code


app/views.py
```python
from django.views.generic import (
    TemplateView,
    ListView, 
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Author, Book

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['books'] = Book.objects.all()
        return context


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = '__all__'
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_form.html'
    fields = '__all__'
    success_url = reverse_lazy('author-list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

```

app/urls.py
```python
from django.urls import path
from .views import (
    AuthorListView, 
    AuthorDetailView, 
    AuthorCreateView, 
    AuthorUpdateView, 
    AuthorDeleteView,
)

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]
```





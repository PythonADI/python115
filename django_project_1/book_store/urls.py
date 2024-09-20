from django.urls import path
from book_store.views import (
    AuthorAndBooksView,
    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
)

urlpatterns = [
    # path('', author_and_books_view, name='author_and_books_view'),
    path('', AuthorAndBooksView.as_view(), name='author_and_books_view'),
    path('authors/', AuthorListView.as_view(), name='author_list_view'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail_view'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create_view'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update_view'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete_view'),
]

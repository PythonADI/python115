from django.urls import path
from blog.views import home, about

urlpatterns = [
    path('', home),
    path('about/', about),
]

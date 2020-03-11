from django.views.generic import DetailView
from django.views.generic import ListView

from library.models import Author


class MainAuthorListView(ListView):
    template_name = 'main.html'
    model = Author


class AuthorDetailView(DetailView):
    template_name = 'author/detail.html'
    model = Author

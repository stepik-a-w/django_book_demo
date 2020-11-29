from django.http import HttpResponseNotFound
from django.shortcuts import render

from library.models import Author


def main_view(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "main.html", context)


def author_detail_view(request, id):
    context = {}

    author = Author.objects.filter(id=id).first()
    if not author:
        return HttpResponseNotFound(f"Нет автора с id {id}")

    context["author"] = author
    return render(request, "author/detail.html", context)

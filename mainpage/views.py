from django.shortcuts import render, get_object_or_404
from mainpage.models import Main


def index(request, pk):
    main = get_object_or_404(Main, pk=pk)

    return render(request, 'mainpage/index.html', {'main': main})

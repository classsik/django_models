from django.shortcuts import render, redirect

from .forms import NewsAddForm
from .models import News


def home(request):
    news = News.objects.all()
    return render(request, 'main/news.html', {"news": news})


def add_news(request):
    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsAddForm()
    return render(request, 'main/form.html', {'form': form})

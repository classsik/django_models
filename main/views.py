from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewsForm
from .models import News


def home(request):
    news = News.objects.all()
    return render(request, 'main/news.html', {"news": news})


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'main/form.html', {'form': form})


def edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm(instance=news)
    return render(request, 'main/edit.html', {'form': form})


def delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('home')

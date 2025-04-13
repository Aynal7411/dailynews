from django.shortcuts import render, get_object_or_404
from .models import Category, NewsArticle

def home(request):
    articles = NewsArticle.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'home.html', {'articles': articles, 'categories': categories})

def category_news(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = NewsArticle.objects.filter(category=category)
    return render(request, 'category.html', {'articles': articles, 'category': category})

def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    return render(request, 'detail.html', {'article': article})

from .models import Article, Categorie
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentaireForm
from django.core.paginator import Paginator
from django.db.models import Q


def liste_articles(request):
    articles = Article.objects.filter(publie=True)

    recherche = request.GET.get('q', '').strip()
    if recherche:
        articles = articles.filter(
            Q(titre__icontains=recherche) | Q(contenu__icontains=recherche)
        )

    paginator = Paginator(articles, 6)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'articles/liste.html', {
        'page': page,
        'categories': Categorie.objects.all(),
        'recherche': recherche,
    })


def articles_par_categorie(request, slug):
    categorie = get_object_or_404(Categorie, slug=slug)
    articles = Article.objects.filter(publie=True, categorie=categorie)
    categories = Categorie.objects.all()
    return render(request, 'articles/liste.html', {
        'articles': articles,
        'categories': categories,
        'categorie_active': categorie,
    })


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.save()
            return redirect('articles:detail', slug=article.slug)
    else:
        form = CommentaireForm()

    commentaires = article.commentaires.filter(approuve=True)
    return render(request, 'articles/detail.html', {
        'article': article,
        'form': form,
        'commentaires': commentaires,
    })
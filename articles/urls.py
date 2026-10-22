from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.liste_articles, name='liste'),
    path('article/<slug:slug>/', views.detail_article, name='detail'),
]
urlpatterns = [
    path('', views.liste_articles, name='liste'),
    path('categorie/<slug:slug>/', views.articles_par_categorie, name='categorie'),
    path('article/<slug:slug>/', views.detail_article, name='detail'),
]
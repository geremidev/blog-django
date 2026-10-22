from django.contrib import admin
from .models import Categorie, Article, Commentaire


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'article', 'date_creation', 'approuve')
    list_filter = ('approuve',)
    search_fields = ('nom', 'contenu')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug')
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'publie', 'date_creation')
    list_filter = ('publie', 'categorie')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}
from django import forms
from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom', 'contenu']
        labels = {'nom': 'Votre nom', 'contenu': 'Votre commentaire'}
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Ex : Marie'}),
            'contenu': forms.Textarea(attrs={'placeholder': 'Écrivez votre commentaire...', 'rows': 4}),
        }
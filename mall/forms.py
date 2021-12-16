from .models import Comment, Cart
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('product',)
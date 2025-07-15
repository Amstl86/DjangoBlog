from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """
    Форма для отправки поста по почте.
    """

    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


class CommentForm(forms.ModelForm):
    """Форма для комментариев к посту через ModelForm"""

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'name': 'Ваше имя',
            'email': 'Ваш email',
            'body': 'Комментарий',
        }
        widgets = {
            'body': forms.Textarea,
        }

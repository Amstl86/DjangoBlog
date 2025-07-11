from django import forms


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

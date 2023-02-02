from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['post_topic', 'post_text', 'author']

    def clean(self):
        cleaned_data = super().clean()
        post_topic = cleaned_data.get('post_topic')
        post_text = cleaned_data.get('post_text')
        if post_topic == post_text:
            raise ValidationError(
                "Заголовок не должен быть равен содержанию."
            )
        return cleaned_data
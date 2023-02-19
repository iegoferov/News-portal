from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Category


class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=20)
    post_category = forms.ModelMultipleChoiceField(
        label='Category',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Post
        fields = ['post_topic', 'post_text', 'author', 'post_category']


    def clean(self):
        cleaned_data = super().clean()
        post_topic = cleaned_data.get('post_topic')
        post_text = cleaned_data.get('post_text')

        if post_topic == post_text:
            raise ValidationError(
                "Заголовок не должен быть равен содержанию."
            )
        return cleaned_data
from .models import Post, Category
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('post_topic', 'post_text')
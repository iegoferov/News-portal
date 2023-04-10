from django.contrib import admin
from .models import Post, Category
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )
class CategoryAdmin(TranslationAdmin):
    model = Category

class PostAdmin(TranslationAdmin):
    model = Post

admin.site.register(Post)
admin.site.register(Category)

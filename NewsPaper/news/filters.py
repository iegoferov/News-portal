from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelChoiceFilter(field_name='post_category',
                                 queryset=Category.objects.all(),
                                 label='Post category',
                                 empty_label='All')

    time_later = DateTimeFilter(field_name='time',
                             lookup_expr='gt',
                             label='Time later:',

                             widget=DateTimeInput(format='%Y-%m-%dT%H:%M',
                             attrs={'type': 'datetime-local'},))

    class Meta:
       model = Post
       fields = {
           # поиск по названию
           'post_topic': ['icontains'],

       }
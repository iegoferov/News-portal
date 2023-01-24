from django import template
import string


register = template.Library()


obscene_words = ['плохой', 'дурак', 'бяка']


@register.filter()
def bad_words(text):
    # Создаем цикл по словам
    for word in text.split():
        # Отбрасываем пунктуацию
        word_trans = word.translate(str.maketrans('', '', string.punctuation))
        # Приводим к строчному виду
        word_trans_lower = word_trans.lower()

        if word_trans_lower in obscene_words:
            word_g = word[0] + (len(word_trans)-1) * "*"
            text = text.replace(word_trans, word_g)
    return text
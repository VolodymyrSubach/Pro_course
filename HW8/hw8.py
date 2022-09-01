from collections import Counter
import string


def get_last_repeat_word(sentence):
    input_text = sentence.translate(str.maketrans('', '', string.punctuation))
    count_dict = dict(Counter(input_text.lower().split()))
    i = 0
    for key, value in count_dict.items():
        if value > 1:
            i = key

    return i if i != 0 else 'No any repeated words!'


text = 'Please repeat repeat times it last to last times.'
print(get_last_repeat_word(text))



import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from lyb.text import *

text = "Привет, мир! Привет!!!"
good_text = tokenize(normalize(text))
words = len(good_text)
unique = len(set(good_text)) 
top = top_n(count_freq(good_text))
print(f'Всего слов: {words}')
print(f'Уникальных слов: {unique}')
print('Топ-5:')
for i in top:
    print(f'{i[0]} : {i[1]}')
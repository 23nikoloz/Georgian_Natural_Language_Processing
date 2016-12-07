import nltk
from nltk import pos_tag, word_tokenize

text = word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

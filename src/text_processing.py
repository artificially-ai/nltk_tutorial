"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

from string import punctuation

customStopwords = set(stopwords.words('english') + list(punctuation))

def tokenize(text):
    sentences = sent_tokenize(text)
    print('Sentences:', '\n', sentences, '\n')
    words = [word_tokenize(sentence) for sentence in sentences]
    print('Words:', '\n', words, '\n')


def filter_stopwords(text):
    noStopwords = [word for word in word_tokenize(text) if word not in customStopwords]
    print('Words without stopwords:', '\n', noStopwords, '\n')


def stemming(text):
    # Stemming words in different morphological forms.
    st = LancasterStemmer()
    stemmedWords = [st.stem(word) for word in word_tokenize(text)]
    print('Stemmed words using Lancaster Stemmer:', '\n', stemmedWords, '\n')


def tag_words(text):
    # NLTK can automatically tag words as nouns, verbs, conjunctions, etc.
    words = nltk.pos_tag(word_tokenize(text))
    print('Tagged words:', '\n', words, '\n')

if __name__ == '__main__':
    text1 = 'Mary had a little lamb. Her fleece was white as snow.'
    text2 = 'Mary closed on closing night when she was in the mood to close.'
    tokenize(text1)
    filter_stopwords(text1)

    stemming(text2)

    tag_words(text2)
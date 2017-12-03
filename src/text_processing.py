"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from nltk.tokenize import word_tokenize, sent_tokenize


def tokenize(text):
    sentences = sent_tokenize(text)
    print('Sentences:', '\n', sentences, '\n')
    words = [word_tokenize(sentence) for sentence in sentences]
    print('Words:', '\n', words, '\n')


if __name__ == '__main__':
    text = "Mary had a little lamb. Her fleece was white as snow."
    tokenize(text)
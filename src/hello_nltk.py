"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

'''
    Understand the context of a text.

    concordance()
        - Displays all occurrences of a word along with the contexy.
    similar()
        - Returns a list of words that appear in similar context - usually synonyms.
    common_context()
        - Returns context shared by two words.
    dispersion_plot()
        - Prints a plot of all the occurrences of the words relative to the beginning of the text.
    
    Processing text
    
    sent_tokenize(), word_tokenize()
        - Tokenize text into lists of sentences (or) lists of words.
    stopwords.words()
        - Get a list of stopwords (e.g. the, an, a) commonly occurring words.
    bigrams(), ngrams()
        - Generate bigrams (pairs of words) or n-grams (groups of n-words) for a sentence or a text.
    collocations()
        - Find the most commonly occurring bigrams. E.g. New York is a collocation because it most commonly comes
        together.
'''

# It is not advisable to download all corpora. Instead, try nltk.download('book_name')
# or from nltk.corpus import gutenberg (for instance).
# When downloading everything, if any book is missing, you will get an error and should try
# to download manually by executing: nltk.download('book_name'). After that, the import * should work.

#from nltk.book import *

from nltk.book import text1, text2


def find_occurrences(book, word = 'monstrous'):
    # Returns occurrences with some context.
    print('\n','Word occurrences on', book.name, '\n')
    print(book.concordance(word), '\n')


def find_similar_words(book, word = 'monstrous'):
    # Returns a list of words appearing in the context of 'word'
    print('\n','Words in similar context on', book.name, '\n')
    print(book.similar(word), '\n')


if __name__ == '__main__':
    # Observe the different connotations in the use of the word 'monstrous' by Melville and Austen
    find_occurrences(text1)
    find_occurrences(text2)

    find_similar_words(text1)
    find_similar_words(text2)
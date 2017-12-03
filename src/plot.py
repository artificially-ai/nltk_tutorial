"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from nltk.book import text1, text2, text4


def plot_changes_in_use_of_words(book, words):
    # Dispersion plot of the use of natural language in different contexts or situations. For example,
    # the use of certain words used by Presidents over the years.
    book.dispersion_plot(words)


if __name__ == '__main__':
    # Inaugural Address Corpus
    plot_changes_in_use_of_words(text4, ['citizen', 'democracy', 'freedom', 'duties', 'America'])
    # Herman Melville - Moby Dick
    plot_changes_in_use_of_words(text1, ['happy', 'sad'])
    # Jane Austen - Sense and Sensibility
    plot_changes_in_use_of_words(text2, ['happy', 'sad'])
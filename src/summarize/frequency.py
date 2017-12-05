"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""
import pandas as pd

from collections import defaultdict
from nltk.corpus import stopwords

from string import punctuation

from nltk.tokenize import word_tokenize

from summarize.downloader import WPArticleDownloader

class FrequencySummarizer(object):


    def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') +
                              list(punctuation) +
                              [u"'s", '"', '“', '‘', '-', '”', '’', '—', 'A'])


    def compute_frequencies(self, word_sent, customStopwords=None):
        if customStopwords is None:
            stopwords = self._stopwords
        else:
            stopwords = set(customStopwords).union(self._stopwords)

        noStopwords = [word for word in word_tokenize(word_sent) if word not in stopwords]
        words_df = pd.DataFrame({'word' : noStopwords})
        words_grouped = pd.DataFrame({'count' : words_df.groupby('word').size()}).reset_index()

        m = words_grouped['count'].max()
        words_grouped['frequency'] = words_grouped['count'] / m

        frequency_df = words_grouped[['word','frequency']][(words_grouped['frequency'] > self._min_cut) & (words_grouped['frequency'] < self._max_cut)]
        return frequency_df.set_index('word')['frequency'].to_dict()


if __name__ == '__main__':
    url = 'https://www.washingtonpost.com/politics/trump-lawyer-says-president-knew-flynn-had-given-fbi-the-same-account-he-gave-to-vice-president/2017/12/03/5c59a620-d849-11e7-a841-2066faf731ef_story.html?hpid=hp_hp-top-table-main_trumpobstruct-1115pm%3Ahomepage%2Fstory'

    downloader = WPArticleDownloader()
    sentences = ''.join(downloader.get_article_text(url))

    f = FrequencySummarizer()
    frequency_dict = f.compute_frequencies(sentences)
    print(frequency_dict)
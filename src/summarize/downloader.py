"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from urllib import request

from bs4 import BeautifulSoup


class WPArticleDownloader(object):


    def get_article_text(self, url):
        try:
            connection = request.urlopen(url)
            page = connection.read().decode("utf8")
            connection.close()
        except Exception as e:
            print('-> Exception:', '\n', e)
            return None, None

        soup = BeautifulSoup(page, 'lxml')
        if soup is None:
            return None, None

        if soup.article is not None:
            return soup.title.text, soup.article.text
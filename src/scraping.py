"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from bs4 import BeautifulSoup


html = ['<html><heading style="font-size:20px"><i>This is the title<br><br></i></heading>',
        '<body><b>This is the body</b><p id="para1">This is the first paragraph. <a href="www.google.com">Google</d></p>',
        '<p id="para2">This is the second paragraph.</p></body></html>']
html = ''.join(html)

soup = BeautifulSoup(html, 'lxml')


def prettify():
    print('-> HTML attribute:', '\n', soup.html.name, '\n')
    print('-> BODY attribute:', '\n', soup.body.name, '\n')
    print('-> BODY parent:', '\n', soup.body.parent.name, '\n')
    print('-> Prettify the HTML code:', '\n', soup.prettify())


def extract_body_text():
    print('-> Everything wrapped by the body tag:', '\n', soup.body.text, '\n')


def extract_children():
    print('-> Contents (children) of a given tag:', '\n', soup.html.contents, '\n')


def extract_siblings():
    print('-> Next sibling:', '\n', soup.b.nextSibling, '\n')
    print('-> Previous sibling:', '\n', soup.b.previousSibling, '\n')


def find_by_tag(search_tag):
    # Use find, findAll, findNext, findPrevious to search the parse tree.
    tag = soup.findAll(search_tag)
    print('-> A list of all bold text in the HTML:', '\n', tag, '\n')
    print('-> A bold text in the HTML:', '\n', tag[0].text, '\n')

    tags_text = '\n'.join([p.text for p in soup.findAll(search_tag)])
    print('-> All text found for a given tag:', '\n', tags_text, '\n')


def find_by_attribute(id):
    text = soup.findAll(id=id)
    print('-> List of tags found by attribute id:', '\n', text, '\n')


def find_by_style(style):
    text = '\n'.join([p.text for p in soup.findAll(style=style)])
    print('-> List of tags found by style:', '\n', text, '\n')


def find_by_attributes(ids):
    text = '\n'.join([p.text for p in soup.findAll(ids)])
    print('-> List of tags found by multiple IDs:', '\n', text, '\n')


def find_links():
    links = soup.find('a')
    print('-> Links found in the HTML:', '\n', links, '\n')

    print('-> Link and Text:', '\n', links['href'], links.text, '\n')


def diverse_finds():
    print('Find next tag after a given text:', '\n', soup.find(text='Google').findNext('p'))
    print('Tag in the body:', '\n', soup.body('p'), '\n')
    print('All "p" in the HTML:', '\n', soup.findAll('p'))


if __name__ == '__main__':
    # find_by_attributes(['i', 'b', 'p'])
    diverse_finds()
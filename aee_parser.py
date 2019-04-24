"""
All Ears English podcast parser
"""
from bs4 import BeautifulSoup as Bs
import requests

SITE = "https://www.allearsenglish.com/episodes/"


class AEE:
    """
    AEE podcast site class
    """
    def __init__(self, url):
        self.url = url
        self.page = None
        self.articles = None
        self.__soup = None

    def __iter__(self):
        return self

    def __get_articles(self):
        if self.page:
            self.__soup = Bs(self.page, 'lxml')
            self.articles = self.__soup.find_all(
                'article', attrs={'class': 'post'})

    def __get_url(self):
        resp = requests.get(self.url)
        resp.raise_for_status()
        self.page = resp.text

    def __find_next(self):
        numeric_pagination = self.__soup.find(
            'div', attrs={'class': 'numeric-pagination'}
        )
        return numeric_pagination.find('a', string='>').href

    def __next__(self):
        if not self.page:
            self.__get_url()
        next_page = self.__find_next()
        if next_page:
            return AEE(next_page)
        raise StopIteration


def get_url(url):
    """
    Return page content
    :param url: page url
    :return: page content or None
    """
    try:
        page = requests.get(url, timeout=10)
        page.raise_for_status()
        result = page.text
    except requests.exceptions.ConnectionError:
        result = None
    except requests.exceptions.HTTPError:
        result = None
    return result


def find_articles(page):
    """
    Return all articles tags from page
    :param page: page content
    :return: all articles or None
    """
    if page:
        soup = Bs(page, 'lxml')
    else:
        return None
    articles = soup.find_all('article', attrs={'class': 'post'})
    return articles


def main():
    """
    Main function
    :return: None
    """
    # page_result = get_url(SITE)
    # for article in find_articles(page_result):
    #     post_link = get_post_link(article)
    #     post_data = get_url(post_link)
    #
    # return post_data


if __name__ == '__main__':
    main()

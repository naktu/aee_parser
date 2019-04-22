"""
All Ears English podcast parser
"""
from bs4 import BeautifulSoup as Bs
import requests

SITE = "https://www.allearsenglish.com/episodes/"


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
    page_result = get_url(SITE)
    find_articles(page_result)


if __name__ == '__main__':
    main()

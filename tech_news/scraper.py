import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Scrap do link de acesso da noticia"""
    selector = Selector(html_content)
    if selector is None:
        return []
    url_selector = selector.css('.tec--card__info h3 a::attr(href)').getall()
    return url_selector


# Requisito 3
def scrape_next_page_link(html_content):
    """Scrap do botao da proxima pagina"""
    selector = Selector(html_content)
    nextPage = selector.css('.tec--list__item ~ a::attr(href)').get()
    if nextPage is None:
        return None
    return nextPage


# Requisito 4
def scrape_noticia(html_content):
    url = "head link[rel=canonical]::attr(href)"
    title = ".tec--article__header__title::text"
    writer = ".tec--author div p a::text"
    timestamp = 'time::attr(datetime)'
    shares_count = ".tec--toolbar__item::text"
    comments_count = "#js-comments-btn::attr(data-count)"

    summary = ".tec--article__body p:first-child *::text"

    sources = ".z--mb-16 h2 ~ div a::text"
    categories = "#js-categories a::text"
    news_abstraction = {
        "url": "",
        "title": "",
        "timestamp": "",
        "writer": None,
        "shares_count": 0,
        "comments_count": 0,
        "summary": "",
        "sources": [],
        "categories": [],
    }
    selector = Selector(html_content)

    news_abstraction["url"] = selector.css(url).get()
    news_abstraction["title"] = selector.css(title).get()
    news_abstraction["timestamp"] = selector.css(timestamp).get()
    writer = selector.css(writer).get()
    if writer and writer.strip()[0].isupper():
        news_abstraction["writer"] = writer.strip()
    elif writer and not writer.strip()[0].isupper():
        writer = selector.css(
            '.tec--author__info p::text').get()
        news_abstraction["writer"] = writer.strip()
    else:
        writer = selector.css(
            '.tec--timestamp__item.z--font-bold a::text').get()
        news_abstraction["writer"] = writer.strip()
    shares_count = selector.css(shares_count).get()
    if shares_count:
        news_abstraction["shares_count"] = int(shares_count.split(' ')[1])
    news_abstraction["comments_count"] = int(selector.css(comments_count)
                                             .get())

    news_abstraction["summary"] = ''.join(selector.css(summary).getall())

    sources_get = selector.css(sources).getall()
    news_abstraction["sources"] = [sources.strip() for sources
                                   in sources_get]
    categories_get = selector.css(categories).getall()
    news_abstraction["categories"] = ([category.strip() for category
                                       in categories_get])
    return news_abstraction



# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

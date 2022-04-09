# Requisito 6
import re
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    search_operation = search_news({"title": re.compile(title, re.IGNORECASE)})
    result = []
    for post in search_operation:
        result.append((post["title"], post["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    format = '%Y-%m-%d'
    try:
        bool(datetime.strptime(date, format))
    except ValueError:
        raise ValueError("Data inválida")
    search_operation = search_news({"timestamp": {"$regex": date}})
    result = []
    for post in search_operation:
        result.append((post["title"], post["url"]))
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    search_operation = search_news(
        {"sources": re.compile(source, re.IGNORECASE)})
    result = []
    for post in search_operation:
        result.append((post["title"], post["url"]))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    search_operation = search_news(
        {"categories": re.compile(category, re.IGNORECASE)})
    result = []
    for post in search_operation:
        result.append((post["title"], post["url"]))
    return result

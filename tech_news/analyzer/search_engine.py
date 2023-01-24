from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title: str) -> list:
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(news["title"], news["url"]) for news in search_news(query)]


# Requisito 7
def search_by_date(date: str) -> list:
    try:
        date_formated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$eq": date_formated}}

        return [(news["title"], news["url"]) for news in search_news(query)]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str) -> str:
    try:
        headers = {"user-agent": "Fake user-agent"}
        timeout = 3
        rate_limit = 1
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
        time.sleep(rate_limit)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str) -> list:
    selector = Selector(html_content)
    return selector.css(".cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content: str) -> str:
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

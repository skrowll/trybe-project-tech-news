import requests
import time


# Requisito 1
def fetch(url: str) -> str:
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

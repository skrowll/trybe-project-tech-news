import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


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
def scrape_news(html_content: str) -> dict:
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        'title': selector.css('h1.entry-title::text').get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count":
            len(selector.css("ol.comment-list li").getall()) or 0,
        "summary":
            re.sub(
                r'<[^<]+?>',
                '',
                selector.css(".entry-content p").get()
            ).strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css("span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount: int):
    base_url = 'https://blog.betrybe.com/'
    news_url_list = []
    news_list = []

    html_content = fetch(base_url)
    news_url_list.extend(scrape_updates(html_content))

    if len(news_url_list) <= amount:
        while len(news_url_list) <= amount:
            next_link = scrape_next_page_link(html_content)
            html_content = fetch(next_link)
            news_url_list.extend(scrape_updates(html_content))

    for news_url in news_url_list:
        html_content = fetch(news_url)
        news = scrape_news(html_content)
        news_list.append(news)

    create_news(news_list[:amount])
    return news_list[:amount]

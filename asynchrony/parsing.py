import datetime
import json
import requests
from bs4 import BeautifulSoup
import time

import asyncio
import aiohttp

my_path = r'C:\Users\sveta\OneDrive\Документы\ByteMePython\asynchrony\urls.json'


BASE_URL = "https://en.wikipedia.org"
START_PAGE = "/wiki/Special:AllPages"
MAX_PAGES = 5

CONCURRENT_REQUESTS = 10


def collect_urls(start_page, max_pages=5):
    '''Функция для сбора ссылок со страниц Wikipedia'''

    collection = set()
    current_url = BASE_URL + start_page

    for i in range(max_pages):
        payload = []
        response = requests.get(current_url, params=payload)
        print(current_url, '-', response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")

        # Собираем ссылки на статьи
        # Образец тега:
        # <div class="mw-allpages-body">
        #     <ul class="mw-allpages-chunk">
        #         <li class="allpagesredirect">
        #             <a href="/wiki/!" class="mw-redirect" title="!">!</a>
        #         </li>

        for li in soup.select("ul.mw-allpages-chunk li"):
            link = li.find("a")
            if link and link.get("href", "").startswith("/wiki/"):
                full_url = BASE_URL + link["href"]
                collection.add(full_url)

        # Переход на следующую страницу
        next_link = soup.select_one("a[title='Special:AllPages'][href*='from=']")
        if next_link:
            current_url = BASE_URL + next_link["href"]
            time.sleep(1)
        else:
            break

    # Сохраняем в JSON
    with open(my_path, "a", encoding="utf-8") as file:
        json.dump([{"url": url, "title": None} for url in collection], file, indent=2)

    print(f"Saved {len(collection)} links to 'urls.json'")


async def fetch_title(session, entry, semaphore):
    url = entry["url"]
    if entry.get("title"):  # если уже есть, пропускаем
        return entry

    async with semaphore:  # ограничиваем количество параллельных запросов
        try:
            async with session.get(url, timeout=10) as response:
                text = await response.text()
                soup = BeautifulSoup(text, "html.parser")
                title_tag = soup.find("title")
                entry["title"] = title_tag.text.strip() if title_tag else "No title found"
        except Exception as e:
            entry["title"] = f"Error: {e}"
    return entry


async def process_title():
    with open(my_path, 'r', encoding='utf-8') as file:
        links = json.load(file)
        semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    print(f"Начат поиск заголовков: {datetime.datetime.now()}")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_title(session, entry, semaphore) for entry in links]
        results = await asyncio.gather(*tasks)

    with open(my_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print(f"Обновлённые заголовки сохранены в urls.json :{datetime.datetime.now()}")



collect_urls(START_PAGE)
asyncio.run(process_title())

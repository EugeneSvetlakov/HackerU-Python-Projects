import os
import bs4
from bs4.element import ResultSet
import requests


# ДЗ № 7 Светлаков Е.С.
# Со страницы yandex.ru собрать новости (в то числе нижнюю динамическую строку)
# и вывести на экрна или сохранить в файл
# *
# Со страницы https://babybug.ru/brendy/melissa/ собрать данные о всех товарах,
# а именно название, цену и картинку
# картинки сохранить в папку images/,
# названия, цены и ссылки на товар в текстовый файл в виде:
# название1, цена1, ссылка1
# название2, цена2, ссылка2
# ....

# page = requests.get("https://yandex.ru")
# soup = bs4.BeautifulSoup(page.content.decode(), 'html.parser')
# spans: ResultSet = soup.find_all(
#     'span', attrs={"class": "news__item-content"})
# for i in spans:
#     print(i.text)

# product-card group
if not os.path.exists("./DZ/images/"):
    os.mkdir("./DZ/images/")
base_url = "https://babybug.ru"
page_link = "/brendy/melissa/"

page2 = requests.get(f"{base_url}{page_link}")
soup_card = bs4.BeautifulSoup(page2.content.decode(), 'html.parser')

# TODO: Нужно дописать чтобы парсило каждую карточку и получало из нее
# набор данных и складывало в список или словарь

find_del_price = soup_card.find_all('del', attrs={'data-price': ''})

# region Модель поиска Имени, Цены на одну карточку
find_prod_title = soup_card.find(
    'a', attrs={'class': 'product-card__title'})

get_prod_name = find_prod_title.get_text().strip()
get_prod_url = f"{base_url}{find_prod_title['href']}"

find_prices = soup_card.find(
    'div', attrs={'class': 'product-card__prices'}).children
price_list = list(
    map(
        lambda p: p.get_text(), filter(
            lambda x: type(x) is bs4.element.Tag, find_prices)))
# endregion

find_prod_pictures = soup_card.find_all(
    'img', attrs={'class': 'product-card__img'})
img_urls = list(map(lambda s: f"{base_url}{s['src']}", find_prod_pictures))
print()

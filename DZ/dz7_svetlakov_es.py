import os
import subprocess
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

# ДЗ по yandex.ru:
page = requests.get("https://yandex.ru")
soup = bs4.BeautifulSoup(page.content.decode(), 'html.parser')
spans: ResultSet = soup.find_all(
    'span', attrs={"class": "news__item-content"})
for i in spans:
    print(i.text)

# ДЗ по babybug.ru:
# product-card group
base_dir = "./DZ/"
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
img_dir = f"{base_dir}images/"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

base_url = "https://babybug.ru"
page_link = "/brendy/melissa/"
page_encoding = requests.get(f"{base_url}{page_link}").encoding

page2 = requests.get(f"{base_url}{page_link}")

soup_card = bs4.BeautifulSoup(
    page2.content.decode(page_encoding), 'html.parser')
# Получаем каталог товаров
find_cards_group = soup_card.find(
    'div', attrs={'class': 'catalog-list'})
# Получаем набор карточек товаров
find_cards = filter(
    lambda c: type(c) is bs4.element.Tag, find_cards_group.children)

products = []
images_urls = []
# Получаем из карточек товаров данные и складываем в списки
for card_item in find_cards:
    # region Модель поиска Имени, Цены на одну карточку товара
    d = card_item.div
    card = bs4.BeautifulSoup(card_item.__str__(), 'html.parser')
    # find_del_price = card.find('del', attrs={'data-price': ''}).get_text()
    # sd = find_del_price.replace('\xa0', ' ')
    # print("find_del_price:", find_del_price)
    # print("sd:", sd)

    find_prod_title = card.find(
        'a', attrs={'class': 'product-card__title'})

    # Наименование товара
    get_prod_name = find_prod_title.get_text().strip()

    # Сылка на страницу товара
    get_prod_url = f"{base_url}{find_prod_title['href']}"

    # Список цен товара
    find_prices = card.find(
        'div', attrs={'class': 'product-card__prices'}).children

    price_list = dict(
        map(
            lambda x: (
                list(x.attrs.keys())[0],
                x.get_text().replace('\xa0', ' ')
            ),
            filter(lambda x: type(x) is bs4.element.Tag, find_prices)
        )
    )

    # Получаем ссылки на изображения товаров
    find_prod_pictures = card.find_all(
        'img', attrs={'class': 'product-card__img'})
    img_urls = list(map(lambda s: f"{base_url}{s['src']}", find_prod_pictures))

    # Сохраняем полученные данные в списки
    products.append((get_prod_name, price_list, get_prod_url))
    images_urls.extend(img_urls)
    # endregion

# Загружаем картинки товаров
for img_url in images_urls:
    image_path = os.path.join(img_dir, os.path.split(img_url)[1])
    subprocess.run(["wget", "-O", image_path, img_url])

# Сохраняем полученные данные о товарах
sn = '\n'.join(map(lambda x: ', '.join(map(str, x)), products))
with open(f"{base_dir}dz7_prod_list.txt", "w") as fw:
    fw.writelines(sn)

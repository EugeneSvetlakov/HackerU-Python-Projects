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
# spans: ResultSet = soup.find_all('span', attrs={"class": "news__item-content"})
# for i in spans:
#     print(i.text)

# product-card group
page2 = requests.get("https://babybug.ru/brendy/melissa/")
soup2 = bs4.BeautifulSoup(page2.content.decode(), 'html.parser')
product_cards: ResultSet = soup2.find_all(
    'div', attrs={"class": "product-card group"})
for i in product_cards:
    print(i.a["title"])
    card_prices_div = i.find('div', attrs={"class": "product-card__prices"})
    c1 = card_prices_div.contents
    print(type(c1))
    c11 = c1[1].text
    c12 = c1[3].text
    sd1 = list(map(lambda x: x.attrs if x != '\n' else '', c1))
    sd2 = list(map(lambda x: x.text if x != '\n' else '', c1))
    sd = list(filter(lambda f: len(f) > 0, map(lambda x: x.text if x != '\n' else '', c1)))
    for el in c1:
        t = el.text if el != '\n' else ''
    print(
        "type(card_prices_div): ", type(card_prices_div),
        "card_prices_div=", card_prices_div)
    print(type(i))

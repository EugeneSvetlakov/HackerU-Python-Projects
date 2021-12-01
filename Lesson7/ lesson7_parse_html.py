import os
import bs4


# Parsing html
# pip install bs4
# [Документация Beautiful Soup]
# (https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html)
# with open("./Lesson7/example.html") as page:
#     page = page.read()
#     soup = bs4.BeautifulSoup(page, 'html.parser')
#     print(soup.h1)
#     print(type(soup.h1))
#     print(soup.h1.text)
#     print(soup.h1.name)
#     h1_attr_style = soup.h1['style']
#     type_tag_string = type(soup.h1.string)
#     tag_h1 = soup.h1
#     fina_on_tag = tag_h1.find('a')
#     print(soup.tr.next.next)
#     print(soup.find('tr'))
#     h2s = soup.find_all('h2')
#     ol = soup.find('ol')
#     # find from parse html
#     lis = ol.find_all('li')
#     # conver result to str
#     lis_to_str = lis.__str__()
#     # get new BeautifulSoup object from
#     # str recieved from BeautifulSoup.find_all
#     soup2 = bs4.BeautifulSoup(lis_to_str, 'html.parser')
#     find_tags_in_res = soup2.find_all('img')

#     lis2 = ol.find_all('li', attrs={"id": "dfdsfdsfsf"})
#     find_by_id = soup.find(id="dfdsfdsfsf")
#     id_img_src = find_by_id.img['src']
#     find_by_class = soup.find(class_="fake foo")
#     use_lambda = soup.find_all(lambda t: t.has_attr('id'))
#     print()


if not os.path.exists("./Lesson7/images/"):
    os.mkdir("./Lesson7/images/")

with open("./Lesson7/prod_card.html") as page:
    soup_card = bs4.BeautifulSoup(page.read(), 'html.parser')
find_del_price = soup_card.find_all('del', attrs={'data-price': ''})

find_prod_title = soup_card.find(
    'a', attrs={'class': 'product-card__title'})

get_prod_name = find_prod_title.get_text().strip()
base_url = "https://babybug.ru"
get_prod_url = f"{base_url}{find_prod_title['href']}"

find_prices = soup_card.find(
    'div', attrs={'class': 'product-card__prices'}).children
price_list = list(
    map(
        lambda p: p.get_text(), filter(
            lambda x: type(x) is bs4.element.Tag, find_prices)))

find_prod_pictures = soup_card.find_all(
    'img', attrs={'class': 'product-card__img'})
img_urls = list(map(lambda s: f"{base_url}{s['src']}", find_prod_pictures))

print()

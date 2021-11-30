import bs4


# Parsing html
# pip install bs4
# [Документация Beautiful Soup]
# (https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html)
with open("./Lesson7/example.html") as page:
    page = page.read()
    soup = bs4.BeautifulSoup(page, 'html.parser')
    print(soup.h1)
    print(type(soup.h1))
    print(soup.h1.text)
    print(soup.h1.name)
    print(soup.tr.next.next)
    print(soup.find('tr'))
    h2s = soup.find_all('h2')
    ol = soup.find('ol')
    lis = ol.find_all('li')
    lis = ol.find_all('li', attrs={"id": "dfdsfdsfsf"})
    find_by_id = soup.find(id="dfdsfdsfsf")
    id_img_src = find_by_id.img['src']
    find_by_class = soup.find(class_="fake foo")
    use_lambda = soup.find_all(lambda t: t.has_attr('id'))
    print()

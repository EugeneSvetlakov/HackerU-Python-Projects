import urllib.request
import urllib.parse
# import bs4
import os
import os.path
import time


GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'


# def getlinks(search_text="машинки"):
#     page = urllib.request.urlopen(f"https://yandex.ru/images/search?text={urllib.parse.quote(search_text)}")
#
#     # print(page.read())
#     soup = bs4.BeautifulSoup(page.read(), "html.parser")
#     res = []
#     for link in soup.findAll('a', class_='serp-item__link'):
#         yalink: str = link.get('href')
#         if "http" in yalink:
#             inx = yalink.index("https")
#             # print(urllib.parse.unquote(yalink[inx:]).split("&")[0])
#             res.append(urllib.parse.unquote(yalink[inx:]).split("&")[0])
#     return res


def load_link(link):
    if not os.path.exists("./Lesson8/images"):
        os.mkdir("./Lesson8/images")
    try: #https://main-cdn.goods.ru/hlr-system/1480143414/100024187201b0.jpg
        # res = urllib.request.urlopen(link)
        # file = open("./images/image_" + link.split("/")[-1], 'wb')
        # file.write(res.read())
        with urllib.request.urlopen(link) as bts, open("./Lesson8/images/image_" + link.split("/")[-1], 'wb') as file:
            file.write(bts.read())
        print(f"{GREEN}done loading {link}{ENDC}")
    except Exception as e:
        print(f"{RED}error on loading {link}{ENDC}")


if __name__ == '__main__':
    # links = getlinks()
    # file = open("links.txt", "w")
    # file.writelines("\n".join(links))
    # print("done")
    print("Start")
    f = open("./Lesson8/links.txt")
    links = f.read().split("\n")
    f.close()
    t = time.time()
    for link in links:
        load_link(link)
    print("All done")
    print(f"{time.time() - t}s.") #39s

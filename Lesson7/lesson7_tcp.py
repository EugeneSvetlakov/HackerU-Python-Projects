from http.client import HTTPResponse
import urllib.request
import urllib.parse

baseurl = "https://yandex.ru/images/search?text="
search_text = "python+image"
search = urllib.parse.quote(search_text)
my_response: HTTPResponse = urllib.request.urlopen(baseurl + search)
ret_code = my_response.getcode()
print(ret_code)

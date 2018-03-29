import requests
import chardet
from bs4 import BeautifulSoup

url = 'http://www.bing.com/'
wb = requests.get(url,stream=True)
# wb.encoding = chardet.detect(wb.content)['encoding']
# print('content--->')
# print(wb.content)
#
# print('encoding--->' + wb.encoding)
print(wb.headers['content-type'])

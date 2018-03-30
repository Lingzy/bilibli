from selenium import webdriver
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
driver = webdriver.PhantomJS()
url = 'https://www.bilibili.com/video/av21061574/'
driver.get(url)
# driver.page_source.encoding = driver.page_source.apparent_encoding
print(driver.page_source)

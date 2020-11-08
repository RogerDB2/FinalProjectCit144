import request
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.whatbirdsareinmybackyard.com/2019/10/what-are-most-common-backyard-birds-in-kentucky.html'

response = request(url)
print(response.text)
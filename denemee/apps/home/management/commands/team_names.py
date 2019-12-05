import requests
import time
from selenium import webdriver
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        main_url = 'https://footystats.org/'
        time_now = strftime("%Y-%m-%d", gmtime())
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
        browser.get(main_url)
        time.sleep(4)
        source = bs(browser.page_source, 'lxml')

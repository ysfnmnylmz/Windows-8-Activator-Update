from selenium import webdriver
import requests
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams, Players, Squads
from denemee.apps.result.models import Matches


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        headers = {'User-agent': 'Mozilla/5.0'}
        driver = webdriver.Chrome()
        main_url = "http://tr.whoscored.com"
        r = driver.get(main_url)
        print(r)


from selenium import webdriver
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.matches.models import Matches
from denemee.apps.home.models import Teams, Players, Squads

import requests
import time


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        main_url = 'https://tr.whoscored.com'
        time_now = strftime("%Y-%m-%d", gmtime())
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
        browser.get(main_url)
        time.sleep(3)
        source = bs(browser.page_source, 'lxml')
        list_of_matches = source.find_all('tr', attrs={'class', 'match'})
        for match in list_of_matches:
            league_code = match.get('data-group-id')
            match_time = match.find('td', attrs={'class', 'time'}).text
            h_team = match.find('td', attrs={'class', 'team home'}).a.text
            a_team = match.find('td', attrs={'class', 'team away'}).a.text
            match_status = match.find('td', attrs={'class', 'status'}).span.text
            match_result = match.find('td', attrs={'class',
                                                   'result'}).a.text  # index 0 home team score, index 4 away team score
            matches = Matches()
            try:
                Matches.objects.get(a_team=a_team, h_team=h_team, date=time_now, hour=match_time)
                print("Maç var!")
            except:
                __away = Teams.objects.get(name=a_team)
                __home = Teams.objects.get(name=h_team)
                matches.a_team = __away
                matches.h_team = __home
                matches.date = time_now
                matches.save()
        browser.quit()

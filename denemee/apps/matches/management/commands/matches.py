from selenium import webdriver
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from datetime import datetime
from bs4 import BeautifulSoup as bs
from denemee.apps.matches.models import Matches
from denemee.apps.home.models import Teams, Players, Squads

import requests
import time


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        main_url = 'https://tr.whoscored.com'
        time_now = strftime("%Y-%m-%d", gmtime())
        ff = 1
        while ff < 5:
            dk = datetime.now().minute
            print(dk)
            for minutes in range(00, 59, 1):
                if dk == minutes:
                    browser = webdriver.Chrome()
                    browser.set_window_size(1920, 1080)
                    browser.minimize_window()
                    browser.get(main_url)
                    time.sleep(4)
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
                        Teams.objects.get_or_create(name=a_team)
                        Teams.objects.get_or_create(name=h_team)
                        __away = Teams.objects.filter(name=a_team)[0]
                        __home = Teams.objects.filter(name=h_team)[0]
                        try:
                            Matches.objects.get(a_team=__away, h_team=__home, date=time_now, hour=match_time)
                            print(str(__home) + " - " + str(__away))
                        except:
                            matches.a_team = __away
                            matches.h_team = __home
                            matches.date = time_now
                            matches.status = match_status
                            matches.hour = match_time
                            try:
                                matches.result_home = match_result[0]
                                matches.result_away = match_result[4]
                            except:
                                matches.result_home = ''
                                matches.result_away = ''
                            if league_code == "17590" or league_code == "17629" or league_code == "17630" or league_code == "17631":
                                matches.match_league = '/static/img/league_flags/england.svg'
                            elif league_code == "17702":
                                matches.match_league = '/static/img/league_flags/spain.svg'
                            elif league_code == "17835":
                                matches.match_league = '/static/img/league_flags/italy.svg'
                            elif league_code == "17682" or league_code == "17683":
                                matches.match_league = '/static/img/league_flags/germany.svg'
                            elif league_code == "17593":
                                matches.match_league = '/static/img/league_flags/france.svg'
                            elif league_code == "17594":
                                matches.match_league = '/static/img/league_flags/netherlands.svg'
                            elif league_code == "17795":
                                matches.match_league = '/static/img/league_flags/turkey.svg'
                            elif league_code == "17565":
                                matches.match_league = '/static/img/league_flags/russia.svg'
                            elif league_code == "17175":
                                matches.match_league = '/static/img/league_flags/brazil.svg'
                            elif league_code == "17737":
                                matches.match_league = '/static/img/league_flags/argentina.svg'
                            elif league_code == "17135":
                                matches.match_league = '/static/img/league_flags/china.svg'
                            elif league_code == "17710":
                                matches.match_league = '/static/img/league_flags/portugal.svg'
                            else:
                                matches.match_league = ''
                            matches.save()
                            print("Maç eklendi!")
                        # Skor güncellemesi
                        if Matches.objects.filter(a_team=__away, h_team=__home, date=time_now,
                                                  hour=match_time).count() > 0:
                            upgrade_match = Matches.objects.get(a_team=__away, h_team=__home, date=time_now,
                                                                hour=match_time)
                            print(match_result)
                            try:
                                upgrade_match.result_home = match_result[0]
                                upgrade_match.result_away = match_result[4]
                                upgrade_match.status = match_status
                                upgrade_match.save()
                            except:
                                print("Skor güncellenemedi!")
                    browser.quit()

# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
import csv

from denemee.apps.home.models import Teams, Players, TeamPowerUp, TeamCharacteristic


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        league_url = '/Regions/225/Tournaments/17/T%C3%BCrkiye-Super-Lig'
        main_url = 'https://tr.whoscored.com'
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
        browser.get(main_url + league_url)
        time.sleep(10)
        source = bs(browser.page_source, 'lxml')
        list_of_teams = source.find('tbody', attrs={'class', 'standings'})
        teams = list_of_teams.find_all('a', attrs={'class', 'team-link'})
        for team in teams:
            """t_add = Teams()
            t_add.name = team.text
            t_add.save()"""
            print(Teams.objects.filter(name=team.text))
            browser2 = webdriver.Chrome()
            team_page = team.get("href")
            browser2.get(main_url + team_page)
            team_page_source = bs(browser2.page_source, 'lxml')
            time.sleep(4)
            team_stats = team_page_source.find("div", {"class": "stats-container"})
            print(team.text)
            for i in team_stats.find('dl').find_all('dd'):
                print(i.text)
                for f in i.find_all('span'):
                    print(f.text)
            browser2.quit()
            break
        browser.quit()

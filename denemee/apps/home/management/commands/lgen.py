# -*- coding: utf-8 -*-
from idlelib.idle_test.test_config import tearDownModule

from django.core.management.base import BaseCommand
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
import csv

from denemee.apps.home.models import Leagues, Teams, Players, TeamPowerUp, TeamCharacteristic


# ----------------------------------------------------------------------
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        league_url = '/Regions/252/Tournaments/2/İngiltere-Premier-League'
        main_url = 'https://tr.whoscored.com'
        team_power_up_list = ['power1', 'power2', 'power3', 'power4', 'power5', 'power6', 'power7', 'power8', 'power9',
                              'power10', 'power11', 'power12', 'defans1', 'defans2', 'defans3', 'defans4', 'defans5',
                              'defans6', 'defans7', 'defans8', 'defans9', 'defans10', 'defans11', 'defans12']
        team_characteristic_list = ['power1', 'power2', 'power3', 'power4', 'power5', 'power6', 'power7', 'power8',
                                    'power9',
                                    'power10', 'power11', 'power12', 'defans1', 'defans2', 'defans3', 'defans4',
                                    'defans5',
                                    'defans6', 'defans7']
        values_of_powers = ['Çok güçlü', 'Güçlü', 'Zayıf', 'Çok Zayıf']
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
        browser.minimize_window()
        browser.get(main_url + league_url)
        time.sleep(9)
        source = bs(browser.page_source, 'lxml')
        list_of_teams = source.find('tbody', attrs={'class', 'standings'})
        teams = list_of_teams.find_all('a', attrs={'class', 'team-link'})
        for team in teams:
            t_add = Teams()
            try:
                Teams.objects.get(name=team.text)
                print("Takım kayıtlı")
            except:
                t_add.name = team.text
                t_add.save()
                print("Takım Eklendi!")
            team_strengths_list = {}
            team_weaknesses_list = {}
            team_style_list = []
            team_stats_list = []
            browser2 = webdriver.Chrome()
            browser2.minimize_window()
            team_page = team.get("href")
            browser2.get(main_url + team_page)
            time.sleep(11)
            team_page_source = bs(browser2.page_source, 'lxml')

            team_emblem = team_page_source.find("img", {"class": "team-emblem"}).get('src')
            player_stats = team_page_source.find("tbody", {"id": "player-table-statistics-body"})
            team_strengths = team_page_source.find("div", {"class": "strengths"})
            team_weaknesses = team_page_source.find("div", {"class": "weaknesses"})
            team_style = team_page_source.find("div", {"class": "style"})
            team_stats = team_page_source.find("div", {"class": "stats-container"})
            # Takım oyuncuları
            for i in player_stats:
                p_add = Players()
                player_name = i.find("a", {"class": "player-link"}).text
                player_minsPlayed = i.find("td", {"class": "minsPlayed"}).text
                player_goal = i.find("td", {"class": "goal"}).text
                player_assistTotal = i.find("td", {"class": "assistTotal"}).text
                player_yellowCard = i.find("td", {"class": "yellowCard"}).text
                player_redCard = i.find("td", {"class": "redCard"}).text
                player_shotsPerGame = i.find("td", {"class": "shotsPerGame"}).text
                player_passSuccess = i.find("td", {"class": "passSuccess"}).text
                player_aerialWonPerGame = i.find("td", {"class": "aerialWonPerGame"}).text
                player_manOfTheMatch = i.find("td", {"class": "manOfTheMatch"}).text
                player_rating = i.find("td", {"class": "rating"}).text
                teamt = Teams.objects.get(name=team.text)
                try:
                    Players.objects.get(name=player_name, team=teamt)
                    print("Oyuncu Kayıtlı!")
                except:
                    p_add.name = player_name
                    p_add.team = teamt
                    p_add.mins = player_minsPlayed
                    p_add.goals = player_goal
                    p_add.asst = player_assistTotal
                    p_add.c_yellow = player_yellowCard
                    p_add.c_red = player_redCard
                    p_add.shot_ot = player_shotsPerGame
                    p_add.pass_success = player_passSuccess
                    p_add.aerial_won = player_aerialWonPerGame
                    p_add.man_o_match = player_manOfTheMatch
                    p_add.player_rating = player_rating
                    p_add.save()
                    print(str(player_name) + "Oyuncu Eklendi")
            print(team.text + " takımının oyuncuları eklendi.")
            for i in team_strengths.find('tbody').find_all('tr'):
                if len(i.find_all('td')) >= 2:
                    a = i.find_all('td')[0].text.strip()
                    b = i.find_all('td')[1].text
                    team_strengths_list[a] = b
            for i in team_weaknesses.find('tbody').find_all('tr'):
                if len(i.find_all('td')) >= 2:
                    a = i.find_all('td')[0].text.strip()
                    b = i.find_all('td')[1].text
                    team_weaknesses_list[a] = b
            for i in team_style.find('ul').find_all('li'):
                a = i.text.strip()
                team_style_list.append(a)
            for i in team_stats.find('dl').find_all('dd'):
                team_stats_list.append(i.text)
                for f in i.find_all('span'):
                    team_stats_list.append(f.text)
            browser2.quit()
            leagues = Leagues()
            try:
                Leagues.objects.get(name=team_stats_list[0])
                print("Lig Kayıtlı")
            except:
                leagues.name = team_stats_list[0]
                leagues.save()
                print("Yeni Lig eklendi")
            select_team = Teams.objects.get(name=team.text)
            select_team.league = Leagues.objects.get(name=team_stats_list[0])
            select_team.emblem = team_emblem
            select_team.goal_pg = team_stats_list[2]
            select_team.avg_possesion = team_stats_list[3].strip('%')
            select_team.pass_accuracy = team_stats_list[4].strip('%')
            select_team.shoots_pg = team_stats_list[5]
            select_team.tackles_pg = team_stats_list[6]
            select_team.dribbles_pg = team_stats_list[7]
            select_team.yellow_card = team_stats_list[9]
            select_team.red_card = team_stats_list[10]
            select_team.save()
            # Takımın karakteristik özellikleri
            for t_style in team_style_list:
                teamtstyle = Teams.objects.get(name=team.text)
                team_style_object = TeamCharacteristic()
                for t_style_field in team_characteristic_list:
                    style_field = TeamCharacteristic._meta.get_field(t_style_field).verbose_name
                    if t_style == style_field:
                        try:
                            add_team_style = TeamCharacteristic.objects.get(team=teamtstyle)
                            add_team_style.__setattr__(t_style_field, True)
                            add_team_style.save()
                        except:
                            team_style_object.team = teamtstyle
                            team_style_object.__setattr__(t_style_field, True)
                            team_style_object.save()
            print(str(teamtstyle) + " takımının karakteristik özellikler eklendi.")
            # Takımın güçlü yönleri
            for k, v in team_strengths_list.items():
                teamt = Teams.objects.get(name=team.text)
                team_pu = TeamPowerUp()
                for tpul in team_power_up_list:
                    field = TeamPowerUp._meta.get_field(tpul).verbose_name
                    if k == field:
                        if v.strip() == values_of_powers[0]:
                            v = 5
                        elif v.strip() == values_of_powers[1]:
                            v = 4
                        elif v.strip() == values_of_powers[2]:
                            v = 2
                        else:
                            v = 1

                        try:
                            add_team = TeamPowerUp.objects.get(team=teamt)
                            add_team.__setattr__(tpul, v)
                            add_team.save()
                        except:
                            team_pu.team = teamt
                            team_pu.__setattr__(tpul, v)
                            team_pu.save()
            print(str(teamt) + " takımının güçlü yönleri eklendi.")
            # Takımın zayıf yönleri
            for k, v in team_weaknesses_list.items():
                teamt = Teams.objects.get(name=team.text)
                team_pu = TeamPowerUp()
                for tpul in team_power_up_list:
                    field = TeamPowerUp._meta.get_field(tpul).verbose_name
                    if k == field:
                        if v.strip() == values_of_powers[0]:
                            v = 5
                        elif v.strip() == values_of_powers[1]:
                            v = 4
                        elif v.strip() == values_of_powers[2]:
                            v = 2
                        else:
                            v = 1

                        try:
                            add_team = TeamPowerUp.objects.get(team=teamt)
                            add_team.__setattr__(tpul, v)
                            add_team.save()
                        except:
                            team_pu.team = teamt
                            team_pu.__setattr__(tpul, v)
                            team_pu.save()
            print(str(teamt) + " takımının zayıf yönleri eklendi.")
        browser.quit()
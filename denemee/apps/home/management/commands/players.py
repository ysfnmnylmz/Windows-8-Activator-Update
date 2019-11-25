import requests
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams, Players


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print("Oyuncu Datası Güncelleniyor...")
        Players.objects.all().delete()
        url = "https://fbref.com/en/comps/26/Super-Lig-Stats"
        main_url = "https://fbref.com"
        time = strftime("%Y-%m-%d", gmtime())
        r = requests.get(url)
        soup = bs(r.content, "lxml")
        league_table = soup.find_all("tr")
        print("Güncel Oyuncu Datası Yükleniyor...")
        for team in league_table:
            team_ = team.find("td", attrs={"data-stat": "squad"})
            if team_:
                team_url = team_.a.get("href")
                team_r = requests.get(main_url + team_url)
                team_soup = bs(team_r.content, "lxml")
                lala = team_soup.find("table", attrs={"id": "stats_player"})
                players = lala.find_all("tbody")
                for player in players:
                    player_info = player.find_all("tr")

                    for p_info_ in player_info:
                        p_names = p_info_.find_all("th")
                        p_poss = p_info_.find_all("td", attrs={"data-stat": "position"})
                        p_apps = p_info_.find_all("td", attrs={"data-stat": "games"})
                        p_starts = p_info_.find_all("td", attrs={"data-stat": "games_starts"})
                        p_mins = p_info_.find_all("td", attrs={"data-stat": "minutes"})
                        p_mins_pg = p_info_.find_all("td", attrs={"data-stat": "minutes_per_game"})
                        p_goals = p_info_.find_all("td", attrs={"data-stat": "goals"})
                        p_assts = p_info_.find_all("td", attrs={"data-stat": "assists"})
                        p_shot_ot = p_info_.find_all("td", attrs={"data-stat": "shots_on_target"})
                        p_fouls = p_info_.find_all("td", attrs={"data-stat": "fouls"})
                        p_c_yellow = p_info_.find_all("td", attrs={"data-stat": "cards_yellow"})
                        p_c_red = p_info_.find_all("td", attrs={"data-stat": "cards_red"})
                        p_goals_pg = p_info_.find_all("td", attrs={"data-stat": "goals_per90"})
                        p_goals_a_pg = p_info_.find_all("td", attrs={"data-stat": "goals_assists_per90"})
                        p_shot_ot_pg = p_info_.find_all("td", attrs={"data-stat": "shots_on_target_per90"})
                        obj = list()
                        obj.append(team_.a.text)
                        for p_name in p_names:
                            obj.append(p_name.a.text)
                        for p_pos in p_poss:
                            obj.append(p_pos.text)
                        for p_app in p_apps:
                            obj.append(p_app.text)
                        for p_start in p_starts:
                            obj.append(p_start.text)
                        for p_min in p_mins:
                            obj.append(p_min.text)
                        for p_min_pg in p_mins_pg:
                            obj.append(p_min_pg.text)
                        for p_goal in p_goals:
                            obj.append(p_goal.text)
                        for p_asst in p_assts:
                            obj.append(p_asst.text)
                        for p_shot in p_shot_ot:
                            obj.append(p_shot.text)
                        for p_foul in p_fouls:
                            obj.append(p_foul.text)
                        for p_c_yellow in p_c_yellow:
                            obj.append(p_c_yellow.text)
                        for p_c_red in p_c_red:
                            obj.append(p_c_red.text)
                        for p_g_pg in p_goals_pg:
                            obj.append(p_g_pg.text)
                        for p_ga_pg in p_goals_a_pg:
                            obj.append(p_ga_pg.text)
                        for p_sot_pg in p_shot_ot_pg:
                            obj.append(p_sot_pg.text)
                        teamt = Teams.objects.get(name=team_.a.text)
                        p_add = Players()
                        p_add.team = teamt
                        p_add.name = obj[1]
                        p_add.position = obj[2]
                        p_add.apps = obj[3]
                        p_add.starts = obj[4]
                        p_add.mins = obj[5]
                        p_add.mins_pg = obj[6]
                        p_add.goals = obj[7]
                        p_add.asst = obj[8]
                        p_add.shot_ot = obj[9]
                        p_add.fouls = obj[10]
                        p_add.c_yellow = obj[11]
                        p_add.c_red = obj[12]
                        p_add.goals_pg = obj[13]
                        p_add.goals_a_pg = obj[14]
                        p_add.shot_ot_pg = obj[15]
                        p_add.save()
                        print("Oyuncu ismi: " + p_add.name + " Eklendi." + p_add.team.name)

        print("Güncel Oyuncu Datası Yüklendi...")

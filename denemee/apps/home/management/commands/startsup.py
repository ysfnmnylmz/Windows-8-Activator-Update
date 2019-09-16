import requests
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams, Players, Squads


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print("İlk 11 Bilgileri Güncelleniyor...")
        url = "https://fbref.com/en/comps/26/Super-Lig-Stats"
        main_url = "https://fbref.com"
        time = strftime("%Y-%m-%d", gmtime())
        r = requests.get(url)
        soup = bs(r.content, "lxml")
        league_table = soup.find_all("tr")
        Squads.objects.all().delete()
        for team in league_table:
            team_ = team.find("td", attrs={"data-stat": "squad"})
            if team_:
                team_url = team_.a.get("href")
                team_r = requests.get(main_url + team_url)
                team_soup = bs(team_r.content, "lxml")
                lala = team_soup.find("table", attrs={"id": "ks_sched_3301"})
                match_date = lala.find_all("td", attrs={"data-stat": "date"})
                for match_ in match_date:
                    if match_.a:
                        match_report_url = match_.a.get("href")
                        match_info_page = requests.get(main_url + match_report_url)
                        match_info_page_soup = bs(match_info_page.content, "lxml")
                        m_week = match_info_page_soup.find("div", attrs={
                            "id": "content",
                        })
                        week = m_week.find("div").text[-2:-1]
                        home_t_line_up = match_info_page_soup.find("div", attrs={
                            "id": "a",
                            "class": "lineup",
                        })
                        away_t_line_up = match_info_page_soup.find("div", attrs={
                            "id": "b",
                            "class": "lineup",
                        })
                        h_team_name = home_t_line_up.find("tr")
                        h_team_squad = home_t_line_up.find_all("td")
                        a_team_squad = away_t_line_up.find_all("td")
                        h_l = list()
                        a_l = list()
                        if team_.a.text == h_team_name.text:
                            for ht_squad in h_team_squad[:22]:
                                if ht_squad.a:
                                    h_l.append(ht_squad.a.text)
                                else:
                                    pass
                            player_teams = Teams.objects.get(name=team_.a.text)
                            squad = Squads()
                            squad.week = week
                            squad.team = player_teams
                            squad.p1 = h_l[0]
                            squad.p2 = h_l[1]
                            squad.p3 = h_l[2]
                            squad.p4 = h_l[3]
                            squad.p5 = h_l[4]
                            squad.p6 = h_l[5]
                            squad.p7 = h_l[6]
                            squad.p8 = h_l[7]
                            squad.p9 = h_l[8]
                            squad.p10 = h_l[9]
                            squad.p11 = h_l[10]
                            squad.save()
                        else:
                            for at_squad in a_team_squad[:22]:
                                if at_squad.a:
                                    a_l.append(at_squad.a.text)
                                else:
                                    pass
                            player_teams = Teams.objects.get(name=team_.a.text)
                            squad = Squads()
                            squad.week = week
                            squad.team = player_teams
                            squad.p1 = a_l[0]
                            squad.p2 = a_l[1]
                            squad.p3 = a_l[2]
                            squad.p4 = a_l[3]
                            squad.p5 = a_l[4]
                            squad.p6 = a_l[5]
                            squad.p7 = a_l[6]
                            squad.p8 = a_l[7]
                            squad.p9 = a_l[8]
                            squad.p10 = a_l[9]
                            squad.p11 = a_l[10]
                            squad.save()
                print(team_.a.text + " Takımı İlk 11 Bilgileri Güncellendi.")

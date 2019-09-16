import requests
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        teams = []
        url = "https://fbref.com/en/comps/26/Super-Lig-Stats"
        main_url = "https://fbref.com"
        time = strftime("%Y-%m-%d", gmtime())
        r = requests.get(url)
        soup = bs(r.content, "lxml")
        league_table = soup.find_all("tr")
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
                        a_team_name = away_t_line_up.find("tr")
                        a_team_squad = away_t_line_up.find_all("td")
                        # print("--" + h_team_name.text + "--")
                        ttt = h_team_name.text
                        if ttt in teams:
                            pass
                        else:
                            teams.append(ttt)

                        # for ht_squad in h_team_squad[:22]:
                        # if ht_squad.a:
                        #    print(ht_squad.a.text)
                        # else:
                        #    pass
                        # print("**--vs--**" * 10)
                        # print("--" + a_team_name.text + "--")
                        # for at_squad in a_team_squad[:22]:
                        # if at_squad.a:
                        #    print(at_squad.a.text)
                        # else:
                        #    pass
                        print("*" * 50)
                print("#" * 100)

        print(teams)
        Teams.objects.all().delete()
        for i in teams:
            obj = Teams()
            obj.name = i
            obj.save()

import requests
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams, Players, Squads
from denemee.apps.result.models import Matches


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        teams = []
        time = strftime("%m/%d/%Y", gmtime())
        main_url = "http://www.betistuta.de"
        url = main_url + "/BOYZFutbol.aspx?L=Sadece%20İddaa%20Maçları&D=" + time
        r = requests.get(url)
        soup = bs(r.content, "lxml")
        league_table = soup.find("table", attrs={"id": "ctl00_MainContentFull_MainContent_MainGrid"})
        matches = league_table.find_all("tr")
        mm = Matches.objects.all()
        for match in matches:
            dlist = []
            details = match.findChildren("td", recursive=False)
            for detail in details:
                try:
                    dlist.append(float(detail.text))
                except:
                    dlist.append(detail.text)

            if len(dlist) > 1:
                m_match = Matches()
                m_match.home_team = dlist[2]
                m_match.over_05 = dlist[19]
                m_match.over_15 = dlist[20]
                m_match.over_25 = dlist[21]
                m_match.over_35 = dlist[22]
                m_match.over_45 = dlist[23]
                m_match.iy_over_05 = dlist[16]
                m_match.iy_over_15 = dlist[17]
                m_match.iy_over_25 = dlist[18]
                m_match.kg = dlist[25]
                print(dlist)
                m_match.date = time
                if m_match.over_05 >= 30 or m_match.iy_over_05 >= 68 or m_match.over_45 >= 15 or m_match.over_35 >= 35 or m_match.over_25 >= 50 or m_match.over_15 >= 55:
                    m_match.tahmin05 = '0.5 Üst'
                if m_match.over_15 >= 55 or m_match.iy_over_15 >= 33 or m_match.over_45 >= 15 or m_match.over_35 >= 35 or m_match.over_25 >= 50:
                    m_match.tahmin15 = '1.5 Üst'
                if m_match.over_25 >= 50 or m_match.iy_over_25 >= 15 or m_match.over_45 >= 15 or m_match.over_35 >= 35:
                    m_match.tahmin25 = '2.5 Üst'
                if m_match.over_35 >= 35 or m_match.over_45 >= 15:
                    m_match.tahmin35 = '3.5 Üst Denenebilir'
                if m_match.over_45 >= 15:
                    m_match.tahmin45 = '4.5 Üst Değerli'
                if m_match.iy_over_05 >= 68 or m_match.iy_over_25 >= 15 or m_match.iy_over_15 >= 33:
                    m_match.tahmin_iy05 = 'İY 0.5 Üst'
                if m_match.iy_over_15 >= 33 or m_match.iy_over_25 >= 15:
                    m_match.tahmin_iy15 = 'İY 1.5 Üst'
                if m_match.iy_over_25 >= 15:
                    m_match.tahmin_iy25 = 'İY 2.5 Üst Denenebilir'
                if m_match.kg >= 55 and m_match.over_25 >= 50 and -15 < m_match.kg - m_match.over_25 < 15:
                    m_match.tahmin_kg = "KG Olur"
                else:
                    m_match.tahmin_kg = "KG Yok"
                """for m in Matches.objects.filter(home_team=m_match.home_team):
                    if m_match.home_team == m.home_team:
                        m.save(over_05=m_match.over_05, over_15=m_match.over_15, over_25=m_match.over_25,
                                 over_35=m_match.over_35, over_45=m_match.over_45, iy_over_05=m_match.iy_over_05,
                                 iy_over_15=m_match.iy_over_15, iy_over_25=m_match.iy_over_25,
                                 tahmin05=m_match.tahmin05,
                                 tahmin15=m_match.tahmin15, tahmin25=m_match.tahmin25, tahmin35=m_match.tahmin35,
                                 tahmin45=m_match.tahmin45, tahmin_iy05=m_match.tahmin_iy05,
                                 tahmin_iy15=m_match.tahmin_iy15,
                                 tahmin_iy25=m_match.tahmin_iy25, kg=m_match.kg, tahmin_kg=m_match.tahmin_kg)
"""
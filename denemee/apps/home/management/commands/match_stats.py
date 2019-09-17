import requests
from django.core.management.base import BaseCommand
from time import gmtime, strftime
from bs4 import BeautifulSoup as bs
from denemee.apps.home.models import Teams, Players, Squads
from denemee.apps.result.models import Matches


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        teams = []
        #test
        time = strftime("%m/%d/%Y", gmtime())
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
        # time = "9/15/2019"
        main_url = "http://www.betistuta.de"
        url = main_url + "/Futbol.aspx?L=Sadece%20İddaa%20Maçları&D=" + time
        r = requests.get(url, headers=headers)
        soup = bs(r.content, "lxml")
        league_table = soup.find("table", attrs={"id": "ctl00_MainContentFull_MainContent_MainGrid"})
        matches = league_table.find_all("tr")
        Matches.objects.all().delete()
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
                m_match.hour = dlist[1]
                m_match.home_team = dlist[2]
                m_match.score = dlist[3]
                m_match.away_team = dlist[4]
                m_match.fh_score = dlist[5]
                m_match.ms1 = dlist[8]
                m_match.ms0 = dlist[9]
                m_match.ms2 = dlist[10]
                m_match.iy1 = dlist[14]
                m_match.iy0 = dlist[15]
                m_match.iy2 = dlist[16]
                m_match.date = time
                if m_match.ms1 > m_match.ms0 and m_match.ms1 > m_match.ms2:
                    m_match.ms_tahmin = 'Ev Sahibi Kazanır'
                elif m_match.ms0 > m_match.ms1 and m_match.ms0 > m_match.ms2:
                    m_match.ms_tahmin = 'Beraberlik'
                elif m_match.ms2 > m_match.ms1 and m_match.ms2 > m_match.ms0:
                    m_match.ms_tahmin = 'Deplasman Kazanır'
                elif m_match.ms1 == m_match.ms0:
                    m_match.ms_tahmin = "1-0 Çifte Şans"
                elif m_match.ms1 == m_match.ms2:
                    m_match.ms_tahmin = "1-2 Çifte Şans"
                elif m_match.ms2 == m_match.ms0:
                    m_match.ms_tahmin = "0-2 Çifte Şans"

                if m_match.iy1 > m_match.iy0 and m_match.iy1 > m_match.iy2:
                    m_match.iy_tahmin = 'Ev Sahibi İlk Yarıyı Kazanır'
                elif m_match.iy0 > m_match.iy1 and m_match.iy0 > m_match.iy2:
                    m_match.iy_tahmin = 'İlk Yarı Beraberlik'
                elif m_match.iy2 > m_match.iy1 and m_match.iy2 > m_match.iy0:
                    m_match.iy_tahmin = 'İlk Yarıyı Deplasman Kazanır'
                elif m_match.iy1 == m_match.iy0:
                    m_match.iy_tahmin = "İY 1-0 Çifte Şans"
                elif m_match.iy1 == m_match.iy2:
                    m_match.iy_tahmin = "İY 1-2 Çifte Şans"
                elif m_match.iy2 == m_match.iy0:
                    m_match.iy_tahmin = "İY 0-2 Çifte Şans"
                m_match.save()

        url2 = main_url + "/BOYZFutbol.aspx?L=Sadece%20İddaa%20Maçları&D=" + time
        r2 = requests.get(url2)
        soup2 = bs(r2.content, "lxml")
        league_table2 = soup2.find("table", attrs={"id": "ctl00_MainContentFull_MainContent_MainGrid"})
        matches2 = league_table2.find_all("tr")
        for match2 in matches2:
            dlist2 = []
            details2 = match2.findChildren("td", recursive=False)
            for detail2 in details2:
                try:
                    dlist2.append(float(detail2.text))
                except:
                    dlist2.append(detail2.text)
            if len(dlist2) > 1:
                for i in Matches.objects.filter(home_team=dlist2[2]):
                    i.over_05 = dlist2[19]
                    i.over_15 = dlist2[20]
                    i.over_25 = dlist2[21]
                    i.over_35 = dlist2[22]
                    i.over_45 = dlist2[23]
                    i.iy_over_05 = dlist2[16]
                    i.iy_over_15 = dlist2[17]
                    i.iy_over_25 = dlist2[18]
                    i.kg = dlist2[25]
                    if i.over_05 >= 30 or i.iy_over_05 >= 68 or i.over_45 >= 15 or i.over_35 >= 35 or i.over_25 >= 50 or i.over_15 >= 55:
                        i.tahmin05 = '0.5 Üst'
                    if i.over_15 >= 55 or i.iy_over_15 >= 33 or i.over_45 >= 15 or i.over_35 >= 35 or i.over_25 >= 50:
                        i.tahmin15 = '1.5 Üst'
                    if i.over_25 >= 50 or i.iy_over_25 >= 15 or i.over_45 >= 15 or i.over_35 >= 35:
                        i.tahmin25 = '2.5 Üst'
                    if i.over_35 >= 35 or i.over_45 >= 15:
                        i.tahmin35 = '3.5 Üst Denenebilir'
                    if i.over_45 >= 15:
                        i.tahmin45 = '4.5 Üst Denenebilir'
                    if i.iy_over_05 >= 68 or i.iy_over_25 >= 15 or i.iy_over_15 >= 33:
                        i.tahmin_iy05 = 'İY 0.5 Üst'
                    if i.iy_over_15 >= 33 or i.iy_over_25 >= 15:
                        i.tahmin_iy15 = 'İY 1.5 Üst'
                    if i.iy_over_25 >= 15:
                        i.tahmin_iy25 = 'İY 2.5 Üst Denenebilir'
                    if i.kg >= 40 and i.over_25 >= 45 and -10 < i.kg - i.over_25 < 10 or i.kg >= 52:
                        i.tahmin_kg = "KG Olur"
                    else:
                        i.tahmin_kg = "KG Yok"
                    i.save()

from django.db import models
from django.utils.safestring import mark_safe
from denemee.apps.home.models import Teams, Players, Squads


class Matches(models.Model):
    date = models.DateField(blank=True, null=True, verbose_name="Maç Tarihi")
    hour = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="Maç Saati")
    home_team = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="Ev Sahibi Takım")
    home_score = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="Ev Sahibi Skoru")
    away_score = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="Deplasman Skoru")
    away_team = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="Deplasman Takımı")
    fh_score = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İlk Yarı skoru")
    ms1 = models.CharField(max_length=255, blank=True, null=True, default='',
                           verbose_name="Maç Sonucu 1 Tahmin Yüzdesi")
    ms0 = models.CharField(max_length=255, blank=True, null=True, default='',
                           verbose_name="Maç Sonucu 0 Tahmin Yüzdesi")
    ms2 = models.CharField(max_length=255, blank=True, null=True, default='',
                           verbose_name="Maç Sonucu 2 Tahmin Yüzdesi")
    iy1 = models.CharField(max_length=255, blank=True, null=True, default='',
                           verbose_name="İlk Yarı Sonucu 1 Tahmin Yüzdesi")
    iy0 = models.CharField(max_length=255, blank=True, null=True, default='',
                           verbose_name="İlk Yarı Sonucu 0 Tahmin Yüzdesi")
    iy2 = models.CharField(max_length=255, blank=True, null=True, default='',
                           verbose_name="İlk Yarı Sonucu 2 Tahmin Yüzdesi")
    ms_tahmin = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="MS Tahmin")
    iy_tahmin = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY Tahmin")
    over_05 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="0.5 Üst")
    over_15 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="1.5 Üst")
    over_25 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="2.5 Üst")
    over_35 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="3.5 Üst")
    over_45 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="4.5 Üst")
    iy_over_05 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY 0.5 Üst")
    iy_over_15 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY 1.5 Üst")
    iy_over_25 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY 2.5 Üst")
    kg = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="KG")
    tahmin05 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="0.5 Üst")
    tahmin15 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="1.5 Üst")
    tahmin25 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="2.5 Üst")
    tahmin35 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="3.5 Üst")
    tahmin45 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="4.5 Üst")
    tahmin_iy05 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY 0.5 Üst")
    tahmin_iy15 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY 1.5 Üst")
    tahmin_iy25 = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="İY 2.5 Üst")
    tahmin_kg = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name="KG Tahmin")

    class Meta:
        verbose_name = "Maç"
        verbose_name_plural = "Maçlar"

    def __str__(self):
        return "{} ile {} takımları arasındaki ilk yarı ve maç sonu tahmini".format(
            self.home_team,
            self.away_team,
        )

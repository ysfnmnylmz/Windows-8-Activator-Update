from django.db import models
from django.urls import reverse
from unicode_tr.extras import slugify
from denemee.apps.home.models import Teams


class Matches(models.Model):
    league_code = models.CharField(max_length=255, verbose_name='Lig Kodu', blank=True, null=True, default='')
    hour = models.CharField(max_length=255, verbose_name='Maç Saati', blank=True, null=True, default='')
    date = models.DateField(verbose_name='Maç Tarihi', blank=True, null=True, default='')
    h_team = models.ForeignKey(Teams, verbose_name='Ev Sahibi Takım', related_name='home_team', blank=True, null=True,
                               default='',
                               on_delete=models.CASCADE)
    h_team_logo = models.CharField(max_length=255, verbose_name='Ev Sahibi Takım Logo Konumu', blank=True, null=True,
                                   default='')
    a_team = models.ForeignKey(Teams, verbose_name='Deplasman Takım', related_name='away_team', blank=True, null=True,
                               default='',
                               on_delete=models.CASCADE)
    a_team_logo = models.CharField(max_length=255, verbose_name='Deplasman Takım Logo Konumu', blank=True, null=True,
                                   default='')
    result_home = models.CharField(max_length=255, verbose_name='Ev Sahibi skor', blank=True, null=True, default='')
    result_away = models.CharField(max_length=255, verbose_name='Deplasman skor', blank=True, null=True, default='')
    status = models.CharField(max_length=255, verbose_name='Durum', blank=True, null=True, default='')
    result = models.CharField(max_length=255, blank=True, null=True)
    match_league = models.CharField(max_length=255, blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Maç'
        verbose_name_plural = 'Maçlar'
        ordering = ['date', 'hour']

    def __str__(self):
        return '{} - {} - {}'.format(
            self.h_team,
            self.result,
            self.a_team,
        )

    def get_absolute_url(self):
        return reverse('matches:matches_details',
                       kwargs={'page_id': self.id, 'page_slug': slugify('{}-vs-{}'.format(self.h_team, self.a_team))})

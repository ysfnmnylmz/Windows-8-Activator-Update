from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=255, verbose_name='Takım ismi')

    class Meta:
        verbose_name_plural = 'Takım İsimleri'
        verbose_name = "Takım İsmi"

    def __str__(self):
        return self.name


class Players(models.Model):
    name = models.CharField(max_length=255, verbose_name="Oyuncu İsmi", blank=True, null=True)
    team = models.ForeignKey('home.Teams', on_delete=models.CASCADE)
    position = models.CharField(max_length=255, verbose_name="Mevki", blank=True, null=True)
    apps = models.IntegerField(verbose_name="Oynadığı Maç Sayısı", blank=True, null=True)
    starts = models.IntegerField(verbose_name="İlk 11'de Başladığı", blank=True, null=True)
    subs = models.IntegerField(verbose_name="Yedekten girdiği", blank=True, null=True)
    mins = models.CharField(max_length=255, verbose_name="Oynadığı Dakika", blank=True, null=True)
    goals = models.IntegerField(verbose_name="Attığı Gol", blank=True, null=True)
    asst = models.IntegerField(verbose_name="Asist", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Oyuncular"
        verbose_name = "Oyuncu"

    def __str__(self):
        return "{} - {} - {}".format(
            self.name,
            self.position,
            self.team,
        )


class Squads(models.Model):
    week = models.CharField(max_length=255, verbose_name="Hafta")
    team = models.ForeignKey('Teams', verbose_name="Takım", on_delete=models.CASCADE)
    p1 = models.CharField(max_length=255, verbose_name="1. Oyuncu")
    p2 = models.CharField(max_length=255, verbose_name="2. Oyuncu")
    p3 = models.CharField(max_length=255, verbose_name="3. Oyuncu")
    p4 = models.CharField(max_length=255, verbose_name="4. Oyuncu")
    p5 = models.CharField(max_length=255, verbose_name="5. Oyuncu")
    p6 = models.CharField(max_length=255, verbose_name="6. Oyuncu")
    p7 = models.CharField(max_length=255, verbose_name="7. Oyuncu")
    p8 = models.CharField(max_length=255, verbose_name="8. Oyuncu")
    p9 = models.CharField(max_length=255, verbose_name="9. Oyuncu")
    p10 = models.CharField(max_length=255, verbose_name="10. Oyuncu")
    p11 = models.CharField(max_length=255, verbose_name="11. Oyuncu")

    class Meta:
        verbose_name = "İlk 11"
        verbose_name_plural = "İlk 11'ler"

    def __str__(self):
        return "{} ({}. Hafta)".format(
            self.team,
            self.week,
        )

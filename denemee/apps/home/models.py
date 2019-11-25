from django.db import models


class Leagues(models.Model):
    name = models.CharField(max_length=255, verbose_name='Lig İsmi')

    class Meta:
        verbose_name = 'Lig'
        verbose_name_plural = 'Ligler'

    def __str__(self):
        return self.name


class Teams(models.Model):
    name = models.CharField(max_length=255, verbose_name='Takım ismi')
    league = models.ForeignKey('Leagues', default='', verbose_name='Lig', on_delete=models.CASCADE, null=True,
                               blank=True)
    goal_pg = models.CharField(max_length=100, verbose_name='Gol (Maç Başına)', default=None, null=True, blank=True)
    avg_possesion = models.CharField(max_length=100, verbose_name='Topa Sahip Olma', default=None, null=True, blank=True)
    pass_accuracy = models.CharField(max_length=100, verbose_name='Pas Yüzdesi', default=None, null=True, blank=True)
    shoots_pg = models.CharField(max_length=100, verbose_name='Şut (Maç Başına)', default=None, null=True, blank=True)
    tackles_pg = models.CharField(max_length=100, verbose_name='Top çalma (Maç Başına)', default=None, null=True, blank=True)
    dribbles_pg = models.CharField(max_length=100, verbose_name='Adam geçme (Maç Başına)', default=None, null=True, blank=True)
    yellow_card = models.CharField(max_length=100, verbose_name='Sarı Kart', default=None, null=True, blank=True)
    red_card = models.CharField(max_length=100, verbose_name='Kırmızı Kart', default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Takım İsimleri'
        verbose_name = "Takım İsmi"

    def __str__(self):
        return self.name


class Players(models.Model):
    name = models.CharField(max_length=255, verbose_name="Oyuncu İsmi", blank=True, null=True)
    team = models.ForeignKey('home.Teams', on_delete=models.CASCADE)
    position = models.CharField(max_length=255, verbose_name="Mevki", blank=True, null=True)
    apps = models.CharField(max_length=255, verbose_name="Oynadığı Maç Sayısı", blank=True, null=True)
    starts = models.CharField(max_length=255, verbose_name="İlk 11'de Başladığı", blank=True, null=True)
    mins = models.CharField(max_length=255, verbose_name="Oynadığı Dakika", blank=True, null=True)
    mins_pg = models.CharField(max_length=255, verbose_name="Maç Başına Oynadığı Dakika", blank=True, null=True)
    goals = models.CharField(max_length=255, verbose_name="Attığı Gol", blank=True, null=True)
    asst = models.CharField(max_length=255, verbose_name="Asist", blank=True, null=True)
    shot_ot = models.CharField(max_length=255, verbose_name='Kaleyi Bulan Şut', blank=True, null=True)
    fouls = models.CharField(max_length=255, verbose_name='Foul', blank=True, null=True)
    c_yellow = models.CharField(max_length=255, verbose_name='Sarı Kart', blank=True, null=True)
    c_red = models.CharField(max_length=255, verbose_name='Kırmızı Kart', blank=True, null=True)
    goals_pg = models.CharField(max_length=255, verbose_name='Maç Başına Gol', default=None, blank=True, null=True)
    goals_a_pg = models.CharField(max_length=255, verbose_name='Maç Başına Asist ve Gol', default=None, blank=True,
                                  null=True)
    shot_ot_pg = models.CharField(max_length=255, verbose_name='Maç Başına İsabetli Şut', default=None, blank=True,
                                  null=True)
    pass_success = models.CharField(max_length=255, verbose_name='Başarılı Pas Yüzdesi', default=None, blank=True,
                                    null=True)
    aerial_won = models.CharField(max_length=255, verbose_name='Hava Topu', default=None, blank=True,
                                  null=True)
    man_o_match = models.CharField(max_length=255, verbose_name='Maçın Adamı', default=None, blank=True,
                                  null=True)
    player_rating = models.CharField(max_length=255, verbose_name='Puanı', default=None, blank=True,
                                  null=True)

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


class TeamPowerUp(models.Model):
    team = models.ForeignKey('Teams', verbose_name='Takım', on_delete=models.CASCADE)
    power1 = models.IntegerField(verbose_name='Gol şanslarındaki bitiricilik', null=True, blank=True)
    power2 = models.IntegerField(verbose_name='Ara toplardan pozisyon yaratma', null=True, blank=True)
    power3 = models.IntegerField(verbose_name='Bireysel yeteneklerden pozisyon yaratma', null=True, blank=True)
    power4 = models.IntegerField(verbose_name='Yenilir pozisyondan geri dönmek', null=True, blank=True)
    power5 = models.IntegerField(verbose_name='Gol pozisyonlarına girme', null=True, blank=True)
    power6 = models.IntegerField(verbose_name='Frikiklerden şut çekme', null=True, blank=True)
    power7 = models.IntegerField(verbose_name='Ceza sahası dışından şut şansı yaratma', null=True, blank=True)
    power8 = models.IntegerField(verbose_name='Duran toplardan saldırma', null=True, blank=True)
    power9 = models.IntegerField(verbose_name='Kanatlardan saldırma', null=True, blank=True)
    power10 = models.IntegerField(verbose_name='Kontra ataklar', null=True, blank=True)
    power11 = models.IntegerField(verbose_name='Ofsayttan kaçınma', null=True, blank=True)
    power12 = models.IntegerField(verbose_name='Topa sahip olma', null=True, blank=True)

    defans1 = models.IntegerField(verbose_name='Duran topları savunma', null=True, blank=True)
    defans2 = models.IntegerField(verbose_name='Hava topu mücadelesi', null=True, blank=True)
    defans3 = models.IntegerField(verbose_name='Bireysel hatalardan kaçınma', null=True, blank=True)
    defans4 = models.IntegerField(verbose_name='Karşı takıma çok pozisyon vermeme', null=True, blank=True)
    defans5 = models.IntegerField(verbose_name='Rakipten top çalma', null=True, blank=True)
    defans6 = models.IntegerField(verbose_name='Ceza sahası dışından şut çektirmeme', null=True, blank=True)
    defans7 = models.IntegerField(verbose_name='Ara paslara karşı savunma', null=True, blank=True)
    defans8 = models.IntegerField(verbose_name='Tehlikeli noktalarda faul yapmaktan kaçınma', null=True, blank=True)
    defans9 = models.IntegerField(verbose_name='Galip durumdan kaybetmeme', null=True, blank=True)
    defans10 = models.IntegerField(verbose_name='Kontra atakları savunma', null=True, blank=True)
    defans11 = models.IntegerField(verbose_name='Kanatlardan saldırılara karşı savunma', null=True, blank=True)
    defans12 = models.IntegerField(verbose_name='Yetenekli oyunculara karşı savunma', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Takımların Güçlü-Zayıf Yönleri'
        verbose_name = 'Takımın Güçlü-Zayıf Yönleri'

    def __str__(self):
        return '{} takımının güçlü-zayıf yönleri'.format(
            self.team,
        )


class TeamCharacteristic(models.Model):
    team = models.ForeignKey('Teams', verbose_name='Takım', on_delete=models.CASCADE)
    power1 = models.BooleanField(verbose_name='Sık ara pas dener', null=True, blank=True)
    power2 = models.BooleanField(verbose_name='Sagdan saldırır', null=True, blank=True)
    power3 = models.BooleanField(verbose_name='Soldan saldırır', null=True, blank=True)
    power4 = models.BooleanField(verbose_name='Sahaya yayılarak oynar', null=True, blank=True)
    power5 = models.BooleanField(verbose_name='Uzun top', null=True, blank=True)
    power6 = models.BooleanField(verbose_name='Sık orta açmayı dener', null=True, blank=True)
    power7 = models.BooleanField(verbose_name='Sık şut çeker', null=True, blank=True)
    power8 = models.BooleanField(verbose_name='Oyunu rakip sahaya yıkar', null=True, blank=True)
    power9 = models.BooleanField(verbose_name='Topa daha çok sahip olur', null=True, blank=True)
    power10 = models.BooleanField(verbose_name='Kısa pas', null=True, blank=True)
    power11 = models.BooleanField(verbose_name='Ortadan saldırır', null=True, blank=True)
    power12 = models.BooleanField(verbose_name='Uzaktan şutlar çeker', null=True, blank=True)

    defans1 = models.BooleanField(verbose_name='Çok değişmeyen ilk onbir', null=True, blank=True)
    defans2 = models.BooleanField(verbose_name='Oyunu kendi sahasına yığar', null=True, blank=True)
    defans3 = models.BooleanField(verbose_name='Agresif değil', null=True, blank=True)
    defans4 = models.BooleanField(verbose_name='Rakip takımın agresif oynamasına sebep olur', null=True, blank=True)
    defans5 = models.BooleanField(verbose_name='Rotasyon yapar', null=True, blank=True)
    defans6 = models.BooleanField(verbose_name='Ofsayt taktiği oynar', null=True, blank=True)
    defans7 = models.BooleanField(verbose_name='Agresif', null=True, blank=True)

    class Meta:
        verbose_name = 'Takım oyun stili'
        verbose_name_plural = 'Takımların oyun stilleri'

    def __str__(self):
        return '{} takımının oyun stili'.format(
            self.team,
        )


class PlayerPowerUp(models.Model):
    player = models.ForeignKey('Players', verbose_name='Oyuncu', on_delete=models.CASCADE)
    power1 = models.IntegerField(verbose_name='Bitiricilik', null=True, blank=True)
    power2 = models.IntegerField(verbose_name='Uzaktan şutlar', null=True, blank=True)
    power3 = models.IntegerField(verbose_name='Ara pas verme', null=True, blank=True)
    power4 = models.IntegerField(verbose_name='Top tutma', null=True, blank=True)
    power5 = models.IntegerField(verbose_name='Hava topu', null=True, blank=True)
    power6 = models.IntegerField(verbose_name='Kilit pas verme', null=True, blank=True)
    power7 = models.IntegerField(verbose_name='Duran top kullanma', null=True, blank=True)
    power8 = models.IntegerField(verbose_name='Direkt free kick', null=True, blank=True)
    power9 = models.IntegerField(verbose_name='Pas verme', null=True, blank=True)
    power10 = models.IntegerField(verbose_name='Orta açma', null=True, blank=True)
    power11 = models.IntegerField(verbose_name='Ofsayt farkındalığı', null=True, blank=True)
    power12 = models.IntegerField(verbose_name='Adam geçme', null=True, blank=True)
    power13 = models.IntegerField(verbose_name='Kafayla şutlar', null=True, blank=True)

    defans1 = models.IntegerField(verbose_name='Defansif katkı', null=True, blank=True)
    defans2 = models.IntegerField(verbose_name='Top kapma', null=True, blank=True)
    defans3 = models.IntegerField(verbose_name='Disiplin', null=True, blank=True)
    defans4 = models.IntegerField(verbose_name='Konsantrasyon', null=True, blank=True)
    defans5 = models.IntegerField(verbose_name='Penaltı kurtarma', null=True, blank=True)
    defans6 = models.IntegerField(verbose_name='Şut durdurma refleksleri', null=True, blank=True)
    defans7 = models.IntegerField(verbose_name='Şut engelleme', null=True, blank=True)
    defans8 = models.IntegerField(verbose_name='Uzaktan şutları kurtarma', null=True, blank=True)
    defans9 = models.IntegerField(verbose_name='Kısa mesafe şutlarını kurtarma', null=True, blank=True)
    defans10 = models.IntegerField(verbose_name='Yan toplar', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Oyuncuların güçlü-zayıf yönleri'
        verbose_name = 'Oyuncunun güçlü-zayıf yönleri'

    def __str__(self):
        return '{} oyuncusunun güçlü-zayıf yönleri'.format(
            self.player,
        )


class PlayerCharacteristic(models.Model):
    Player = models.ForeignKey('Players', verbose_name='Oyuncu', on_delete=models.CASCADE)
    power1 = models.BooleanField(verbose_name='Koşu yoluna pas atmayı sever', null=True, blank=True)
    power2 = models.BooleanField(verbose_name='Kanattan içeri girmeyi sever', null=True, blank=True)
    power3 = models.BooleanField(verbose_name='Endirek duran topta tehlike', null=True, blank=True)
    power4 = models.BooleanField(verbose_name='Uzaktan şut çekmeyi sever', null=True, blank=True)
    power5 = models.BooleanField(verbose_name='Sık faul alır', null=True, blank=True)
    power6 = models.BooleanField(verbose_name='Adam geçmeyi sever', null=True, blank=True)
    power7 = models.BooleanField(verbose_name='Kontra atak tehditi', null=True, blank=True)
    power8 = models.BooleanField(verbose_name='Kısa pas vermeyi sever', null=True, blank=True)
    power9 = models.BooleanField(verbose_name='Topu havalandırmayı sever', null=True, blank=True)
    power10 = models.BooleanField(verbose_name='Uzun top oynamayı sever', null=True, blank=True)
    power11 = models.BooleanField(verbose_name='Orta açmayı sever', null=True, blank=True)
    power12 = models.BooleanField(verbose_name='Top indirmeyi sever', null=True, blank=True)

    defans1 = models.BooleanField(verbose_name='Top çalmaya çalışmaz', null=True, blank=True)
    defans2 = models.BooleanField(verbose_name='Top çalmayı sever', null=True, blank=True)
    defans3 = models.BooleanField(verbose_name='Sık faul yapar', null=True, blank=True)
    defans4 = models.BooleanField(verbose_name='Sık topu defanstan uzaklaştırır', null=True, blank=True)
    defans5 = models.BooleanField(verbose_name='Topu yumruklamayı sever', null=True, blank=True)

    class Meta:
        verbose_name = 'Oyuncu oyun stili'
        verbose_name_plural = 'Oyuncuların oyun stilleri'

    def __str__(self):
        return '{} oyuncusunun oyun stili'.format(
            self.player,
        )

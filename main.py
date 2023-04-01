import pygame
import sys
import random
# dodac piosenke plik

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode((600, 600))
fps = 60
zegar = pygame.time.Clock()

hajsownik = pygame.image.load("./Pliki/Hajsownik.png")
pygame.display.set_caption("Nieśmieszny Hajsownik")
pygame.display.set_icon(hajsownik)

import pygame


class PasekZycia:
    def __init__(self, ekran, healthBarLength, hight, x, y):
        self.currentHealth = 1000
        self.basicHealth = 1000
        self.healthBarLenth = healthBarLength
        self.healthRatio = self.basicHealth / self.healthBarLenth
        self.hight = hight
        self.x = x
        self.y = y
        self.ekran = ekran

    def getDamage(self, ilosc):
        if self.currentHealth > 0:
            self.currentHealth -= ilosc
        if self.currentHealth <= 0:
            self.currentHealth = 0

        self.update()

    def setNewPosition(self, x, y):
        self.x = x
        self.y = y

    def getHealth(self, ilosc):
        if self.currentHealth < self.basicHealth:
            self.currentHealth += ilosc
        if self.currentHealth >= self.basicHealth:
            self.currentHealth = self.basicHealth

        self.update()

    def update(self):
        self.drawHealth()

    def drawHealth(self):
        pygame.draw.rect(self.ekran, (255, 0, 0),
                         (self.x, self.y,
                          self.currentHealth / self.healthRatio, self.hight))
        pygame.draw.rect(self.ekran, (0, 0, 0),
                         (self.x, self.y, self.healthBarLenth, self.hight), 4)

    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        self.drawHealth()


class Button():
    def __init__(self, color, x, y, width, height, text='', tekstSize=0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.tekstSize = tekstSize

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(
                win, outline,
                (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.tekstSize)
            text = font.render(self.text, True, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos, click):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                if click == True:
                    return True

        return False


class Przeciwnik:
    def __init__(self, x, photo, licznikStrzal):
        self.x = x
        self.y = -100
        self.photo = photo
        self.alive = True
        self.damage = 700
        self.listaStrzal = []
        self.licznikStrzal = licznikStrzal

    def get_damage(self):
        self.alive = False

    def draw(self):
        ekran.blit(self.photo, (self.x, self.y))

    def updatePosition(self):
        self.y += 2


def main_menu():
    font = pygame.font.SysFont("comicsans", 60)
    tekst1 = font.render("Nieśmieszny Hajsownik", True, (0, 0, 0))
    start = False
    wyjscieZInformacji = False
    click = False
    while (start == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        buttonStart = Button((255, 0, 0), 175, 280, 250, 60, "Start", 60)
        buttonInform = Button((255, 0, 0), 175, 360, 250, 60, "Informacje", 60)
        buttonExit = Button((255, 0, 0), 175, 440, 250, 60, "Exit", 60)

        ekran.fill((66, 69, 200))
        buttonStart.draw(ekran, False)
        buttonInform.draw(ekran, False)
        buttonExit.draw(ekran, False)
        ekran.blit(tekst1, (50, 50))

        positionMouse = pygame.mouse.get_pos()
        if buttonStart.isOver(positionMouse, click) == True:
            start = True
        if buttonInform.isOver(positionMouse, click) == True:
            informacjeISterowanie()
        if buttonExit.isOver(positionMouse, click) == True:
            sys.exit()

        pygame.display.flip()
        zegar.tick(fps)


def informacjeISterowanie():
    wyjscie = False
    klikniecie = False
    while (wyjscie == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                klikniecie = True

        zegar.tick(fps)
        ekran.fill((255, 255, 255))

        font1 = pygame.font.SysFont("comicsans", 30)
        linia1 = font1.render(
            "Witaj w grze pod tytółem: Nieśmieszny Hajsownik!", True,
            (0, 0, 0))
        linia2 = font1.render(
            "Twojim celem jest zbanowanie wszystkich niesmiesznych ", True,
            (0, 0, 0))
        linia3 = font1.render("memow, a na końcu Bosa!", True, (0, 0, 0))
        linia4 = font1.render(
            "porusznie: Myszką, stzrelanie: Lewym kliknięciem", True,
            (0, 0, 0))
        linia5 = font1.render(
            "Gra została napisana w Pythonie około 600 linijek kodu,", True,
            (0, 0, 0))
        linia6 = font1.render("Gra na około 2 min , Życzę miłego grania!",
                              True, (0, 0, 0))

        ekran.blit(linia1, (20, 70))
        ekran.blit(linia2, (20, 120))
        ekran.blit(linia3, (20, 170))
        ekran.blit(linia4, (20, 220))
        ekran.blit(linia5, (20, 270))
        ekran.blit(linia6, (20, 320))

        powrotBtn = Button((0, 0, 255), 10, 10, 60, 30, "Powrót", 20)
        powrotBtn.draw(ekran, True)

        mousePos = pygame.mouse.get_pos()
        if powrotBtn.isOver(mousePos, klikniecie):
            wyjscie = True
        pygame.display.flip()

    main_menu()


def cutScenki():
    scena1 = pygame.image.load("./Pliki/CutScenka/GimperCutScenka1.png")
    scena2 = pygame.image.load("./Pliki/CutScenka/GimperCutScenka2.png")
    scena3 = pygame.image.load("./Pliki/CutScenka/GimperCutScenka3.png")
    scena4 = pygame.image.load("./Pliki/CutScenka/GimperCutScenka4.png")
    scena1 = pygame.transform.scale(scena1, (600, 600))
    scena2 = pygame.transform.scale(scena2, (600, 600))
    scena3 = pygame.transform.scale(scena3, (600, 600))
    scena4 = pygame.transform.scale(scena4, (600, 600))

    ekran.blit(scena1, (0, 0))
    pygame.display.flip()
    pygame.time.wait(6000)

    ekran.blit(scena2, (0, 0))
    pygame.display.flip()
    pygame.time.wait(4000)

    ekran.blit(scena3, (0, 0))
    pygame.display.flip()
    pygame.time.wait(6000)

    ekran.blit(scena4, (0, 0))
    pygame.display.flip()
    pygame.time.wait(5000)


def gameOver():
    koniec = True
    licznik = 0
    scena1 = pygame.image.load("./Pliki/GameOverAnim/gameover1.png")
    scena2 = pygame.image.load("./Pliki/GameOverAnim/gameover2.png")
    scena3 = pygame.image.load("./Pliki/GameOverAnim/gameover3.png")
    scena1 = pygame.transform.scale(scena1, (400, 400))
    scena2 = pygame.transform.scale(scena2, (400, 400))
    scena3 = pygame.transform.scale(scena3, (400, 400))
    dlugiLicznik = 0
    friz = pygame.image.load("./Pliki/Friz.png")
    friz = pygame.transform.scale(friz, (300, 400))
    cziconka = pygame.font.SysFont("comicsense", 30)
    tekst1 = cziconka.render("Niesmieszny Hajsownik okazał sie Frizem,", True,
                             (0, 0, 0))
    tekst2 = cziconka.render("który Zazdrościł ci grópy na gimpbooku!", True,
                             (0, 0, 0))
    tekst3 = cziconka.render(
        "Niestety wstawił na grupe za dużo nieśmiesznych memów", True,
        (0, 0, 0))
    tekst4 = cziconka.render("i wszystkie Hajsowniky opóściły!!!", True,
                             (0, 0, 0))
    wyjscie = Button((255, 0, 0), 350, 500, 200, 50, "Wyjscie", 40)
    kliik = False
    sprobojPon = Button((255, 0, 0), 100, 500, 200, 50, "Spróbój Ponownie", 20)
    while (koniec):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                koniec = False
            elif event.type == pygame.KEYDOWN and pygame.KEYDOWN == pygame.K_ESCAPE:
                koniec = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                kliik = True

        ekran.fill((255, 255, 255))

        if dlugiLicznik < 10:
            if licznik == 0:
                ekran.blit(scena1, (100, 100))
            elif licznik == 1:
                ekran.blit(scena2, (100, 100))
            else:
                ekran.blit(scena3, (100, 100))
                licznik = -1

            licznik += 1
            dlugiLicznik += 1

        else:
            ekran.blit(tekst1, (20, 40))
            ekran.blit(tekst2, (20, 70))
            ekran.blit(tekst3, (20, 100))
            ekran.blit(tekst4, (20, 130))
            ekran.blit(friz, (150, 150))
            wyjscie.draw(ekran, True)
            sprobojPon.draw(ekran, True)

            if wyjscie.isOver(pygame.mouse.get_pos(), kliik):
                koniec = False

            if sprobojPon.isOver(pygame.mouse.get_pos(), kliik):
                pygame.mixer.music.load("./Pliki/Hymn.wav")
                pygame.mixer.music.play(1)
                pygame.mouse.set_visible(True)
                main()

        pygame.display.flip()

        zegar.tick(6)


def wygrana():
    pygame.mixer.music.stop()
    koniec = True

    friz = pygame.image.load("./Pliki/Friz2.png")
    friz = pygame.transform.scale(friz, (300, 400))
    cziconka = pygame.font.SysFont("comicsense", 30)
    tekst1 = cziconka.render("Niesmieszny Hajsownik okazał sie Frizem,", True,
                             (0, 0, 0))
    tekst2 = cziconka.render("który Zazdrościł ci grópy na gimpbooku!", True,
                             (0, 0, 0))
    tekst3 = cziconka.render("Naszczęście Udało ci się go powtrzymać,", True,
                             (0, 0, 0))
    tekst4 = cziconka.render("i odszedł o w smutku!", True, (0, 0, 0))
    wyjscie = Button((255, 0, 0), 350, 500, 200, 50, "Wyjscie", 40)
    kliik = False
    trofeumBut = Button((255, 0, 0), 100, 500, 200, 50, "Trofeum", 20)
    while (koniec):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                koniec = False
            elif event.type == pygame.KEYDOWN and pygame.KEYDOWN == pygame.K_ESCAPE:
                koniec = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                kliik = True

        ekran.fill((255, 255, 255))

        ekran.blit(tekst1, (20, 40))
        ekran.blit(tekst2, (20, 70))
        ekran.blit(tekst3, (20, 100))
        ekran.blit(tekst4, (20, 130))
        ekran.blit(friz, (150, 150))
        wyjscie.draw(ekran, True)
        trofeumBut.draw(ekran, True)

        if wyjscie.isOver(pygame.mouse.get_pos(), kliik):
            koniec = False

        if trofeumBut.isOver(pygame.mouse.get_pos(), kliik):
            trofeum()

        pygame.display.flip()

        zegar.tick(6)


def trofeum():
    ekran.blit(
        pygame.transform.scale(pygame.image.load("./Pliki/Puchar.png"),
                               (600, 600)), (0, 0))


def main():
    main_menu()
    cutScenki()

    def updateBullet(yBullet):
        yBullet -= 8
        return yBullet

    def updateHajBullet(hajBulY):
        hajBulY += 4
        return hajBulY

    def updatePrzecBullet(przecY):
        return przecY + 5

    # zmienne
    x, y = pygame.mouse.get_pos()
    run = True
    lastX = 0
    lastY = 0
    bulletLista = []
    pozostaleStrzaly = 2
    pozostaleStrzaly -= len(bulletLista)
    hajImage = pygame.image.load("./Pliki/Hajsownik.png")
    hajImage = pygame.transform.scale(hajImage, (100, 100))
    hajBulletImg = pygame.image.load("./Pliki/BulletHaj.png")

    livznikStrzalHajsownika = 0

    koniecMemow = False
    licznikTworzenia = 0

    listaStrzalHaj = []

    xx = 250
    hajMove = 2
    maxY = 50
    yy = -900
    hajPasek = PasekZycia(ekran, 70, 15, xx + 15, yy + 10)

    czyWPrawo = True
    livznkStrzalHajsownika = 0

    listaMemow = []
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem1.jpeg"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem2.jpeg"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem3.jpeg"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem4.JPG"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem5.jpeg"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem6.JPG"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem7.JPG"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem8.jpeg"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem9.JPG"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem10.jpeg"),
                               (60, 50)))
    listaMemow.append(
        pygame.transform.scale(pygame.image.load("./Pliki/Memy/mem11.jpeg"),
                               (60, 50)))
    listaPrzeciwnikow = []

    strzalap = pygame.image.load("./Pliki/StrzalaPrzeciwnik.png")

    strzalap = pygame.transform.scale(strzalap, (20, 20))

    iloscMemow = 0

    czyPierwsze = True

    licznikowyLicznik = 0
    font8 = pygame.font.SysFont("comicsans", 60)
    tekstNadchodzi = font8.render("Nadchodzi!!!", True, (0, 0, 0))

    def screenUpdate(licznikTekstuGimper, x, y, pozStrzaly, yy, xx, czyWPrawo,
                     licznikStrzalHajsownika, czyPierwsze, koniecMemow,
                     licznikowyLicznik):
        # if do licnzika dodac
        # boss
        ekran.fill((255, 255, 255))

        if koniecMemow == True:
            ekran.blit(hajImage, (xx, yy))
            hajPasek.setNewPosition(xx + 15, yy + 10)
            hajPasek.drawHealth()

            if yy < maxY:
                yy += hajMove
            else:
                if czyWPrawo == False:
                    if xx > 100:
                        xx -= hajMove
                    else:
                        czyWPrawo = True
                elif czyWPrawo == True:
                    if xx < 400:
                        xx += hajMove
                    else:
                        czyWPrawo = False

        ekran.blit(fb, (200, 250))
        ekran.blit(gimper, (x, y))

        gimperBar.setNewPosition(x - 10, y + 60)
        gimperBar.drawHealth()
        for t in range(len(bulletLista)):
            widocznosc = True
            bulletRep = bulletLista[t - 1]
            ekran.blit(bulletPhoto, (bulletRep[0], bulletRep[1]))
            yChwilowe = updateBullet(bulletRep[1])
            licznik = bulletRep[2]
            licznik += 1
            bulletLista.pop(t - 1)

            if koniecMemow == True:
                if bulletRep[0] > xx - 20 and bulletRep[
                        0] < xx + 100 and bulletRep[1] > yy and bulletRep[
                            1] < yy + 100:
                    hajPasek.getDamage(70)
                    widocznosc = False
            if licznik != 80 and widocznosc == True:
                bulletLista.append((bulletRep[0], yChwilowe, licznik))

        if koniecMemow == True and len(listaStrzalHaj) > 0:
            for j in range(len(listaStrzalHaj)):
                bulletHajRep = listaStrzalHaj[j - 1]
                ekran.blit(hajBulletImg, (bulletHajRep[0], bulletHajRep[1]))
                listaStrzalHaj.pop(j - 1)
                yyyy = updateHajBullet(bulletHajRep[1])
                if yyyy < 700:
                    if bulletHajRep[0] > x and bulletHajRep[
                            0] < x + 50 and yyyy > y and yyyy < y + 50:
                        gimperBar.getDamage(300)
                        pygame.mixer.music.load("./Pliki/Ouh.wav")
                        pygame.mixer.music.play()

                    else:
                        listaStrzalHaj.append((bulletHajRep[0], yyyy))
        if len(listaPrzeciwnikow) > 0:
            for l in listaPrzeciwnikow:
                l.draw()
                l.updatePosition()
                for i in bulletLista:
                    if i[0] > l.x and i[0] < l.x + 60 and i[1] > l.y and i[
                            1] < l.y + 50:
                        listaPrzeciwnikow.pop(listaPrzeciwnikow.index(l))
                        bulletLista.pop(bulletLista.index(i))

                if len(l.listaStrzal) < 3:
                    if l.licznikStrzal >= 100 or czyPierwsze == True:
                        l.listaStrzal.append([l.x, l.y])
                        l.licznikStrzal = 0
                        czyPierwsze = False
                    else:
                        l.licznikStrzal += 1

                for t in range(len(l.listaStrzal)):
                    rep = l.listaStrzal[t - 1]
                    ekran.blit(strzalap, rep)
                    l.listaStrzal.pop(t - 1)
                    rep[1] = updatePrzecBullet(rep[1])
                    if rep[1] > -100:
                        l.listaStrzal.append(rep)

                    if rep[0] > x and rep[0] < x + 50 and rep[1] > y and rep[
                            1] < y + 50:
                        gimperBar.getDamage(10)
                        pygame.mixer.music.load("./Pliki/Ouh.wav")
                        pygame.mixer.music.play()
        '''pygame.draw.rect(ekran, (123, 104, 238), rectHajsownicy)
        ekran.blit(tekst1, (rectHajsownicy.x + 10, rectHajsownicy.y + 10))'''

        if iloscMemow >= 18:
            koniecMemow = True
            if licznikowyLicznik <= 120 and licznikowyLicznik > 40:
                ekran.blit(tekstNadchodzi, (200, 100))
            licznikowyLicznik += 1

        if licznikTekstuGimper < 200:
            ekran.blit(tekst2, (x - 5, y - 30))
        licznikTekstuGimper += 1
        '''hajsownicyBar.drawHealth()'''

        if licznikStrzalHajsownika >= 70 and koniecMemow == True and len(
                listaStrzalHaj) < 2:
            licznikStrzalHajsownika = 0
            listaStrzalHaj.append((xx + 50, yy + 10))

        else:
            licznikStrzalHajsownika += 1

        pygame.display.flip()

        return licznikTekstuGimper, yy, xx, czyWPrawo, licznikStrzalHajsownika, czyPierwsze, koniecMemow, licznikowyLicznik

    # cutscenki

    scenka1 = pygame.image.load("./Pliki/CutScenka/GimperCutScenka1.png")
    scenka1 = pygame.transform.scale(scenka1, (600, 600))
    scenka2 = pygame.image.load("./Pliki/CutScenka/GimperCutScenka2.png")
    scenka2 = pygame.transform.scale(scenka2, (600, 600))

    # ladowanie zdj

    gimper = pygame.image.load("./Pliki/Gimpson.png")
    fb = pygame.image.load("./Pliki/Facebook.png")
    fb = pygame.transform.scale(fb, (200, 100))

    gimper = pygame.transform.scale(gimper, (55, 45))
    # bullet settings
    bulletPhoto = pygame.image.load("./Pliki/Rakieta.png")

    licznikTEkstuGimper = 0
    '''y = 500
    x = 300'''

    # text
    font1 = pygame.font.SysFont("comicsans", 50)
    font2 = pygame.font.SysFont("comicsans", 30)
    font3 = pygame.font.SysFont("comicsans", 60)
    # tekst1 = font1.render("Prawilni Hajsownicy", True, (0, 0, 0))
    tekst2 = font2.render("Gimper", True, (0, 0, 0))
    # levelText = font1.render(f"Fala {level}",True,(191,191,191))

    # rectHajsownicy = pygame.Rect(100, 570, 400, 30)
    # hajsownicyBar = PasekZycia(ekran,150,20,300,575)

    gimperBar = PasekZycia(ekran, 75, 10, x, y)

    while (run):
        zegar.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                pygame.mouse.set_visible(True)
                main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(bulletLista) < 2:
                    bulletLista.append((x + 5, y, 0))
        '''if pygame.key.get_pressed()[pygame.K_LEFT]:
            x -= 4

        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            x += 4

        elif pygame.key.get_pressed()[pygame.K_UP]:
            y -= 4

        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            y += 4'''

        # updating mouse position
        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        if x + 60 < 600 and x > 0 and y + 50 < 600 and y > 0:
            licznikTEkstuGimper, yy, xx, czyWPrawo, livznikStrzalHajsownika, czyPierwsze, koniecMemow, licznikowyLicznik = screenUpdate(
                licznikTEkstuGimper, x, y, pozostaleStrzaly, yy, xx, czyWPrawo,
                livznikStrzalHajsownika, czyPierwsze, koniecMemow,
                licznikowyLicznik)
            lastX = x
            lastY = y
        else:
            licznikTEkstuGimper, yy, xx, czyWPrawo, livznikStrzalHajsownika, czyPierwsze, koniecMemow, licznikowyLicznik = screenUpdate(
                licznikTEkstuGimper, lastX, lastY, pozostaleStrzaly, yy, xx,
                czyWPrawo, livznikStrzalHajsownika, czyPierwsze, koniecMemow,
                licznikowyLicznik)

        if koniecMemow == True:
            if y + 23 > yy and y + 23 < yy + 100:
                if x + 28 > xx and x + 28 < xx + 100:
                    gimperBar.getDamage(4)

        if licznikTworzenia >= 80 and koniecMemow == False:
            wybor = random.randint(0, 11)
            miejsce = random.randint(1, 15)
            miejsce *= 40

            place = x
            b = random.randint(1, 2)
            if b == 1:
                place += 50
            if b == 2:
                place -= 50
            przeciwnik = Przeciwnik(place, listaMemow[wybor - 1], 0)
            listaPrzeciwnikow.append(przeciwnik)
            licznikTworzenia = 0
            iloscMemow += 1

        else:
            licznikTworzenia += 1

        if gimperBar.currentHealth <= 0:
            run = False
            pygame.time.wait(1000)
            pygame.mouse.set_visible(True)
            gameOver()
        if hajPasek.currentHealth <= 0:
            pygame.mouse.set_visible(True)
            wygrana()
            run = False


if __name__ == '__main__':
    main()

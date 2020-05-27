import pygame
import random

pygame.init()
#kolorki ktore moga sie przydac zeby nie wpisawac kodu RGB za kazdym razem
colors = {"black":(0,0,0), "grey":(128,128,128),"lightgrey":(200,200,200),
          "white":(255,255,255), "red":(255,0,0),
          "green":(0,255,0), "blue":(0,0,255)}
wrong_font = pygame.font.Font(None, 50) #czcionka dla wypisywania blednych liter, ktorych nie ma w hasle
default_font = pygame.font.Font(None, 40) #zwykla czcionka do wypisywania hasla na ekranie
round_font = pygame.font.Font(None, 90) #czcionka do pytania o kolejna runde
word = 'haslo maslo' #przykladowe haslo XD

s_width,s_height=1200,800 # szerokosc ekranu = 1200px, wysokosc ekranu = 900px

screen = pygame.display.set_mode((s_width, s_height)) #tworze ekran

turns = 11 #liczba tur
#wspolrzedne x i y dla zlej litery zeby sie wypisywala w okreslonym okienku
wrong_x=55
wrong_y=80

def another_round(): #funkcja pytajaca o kolejna runde
    text = round_font.render('Another round?',True,colors['black'])
    textRect = text.get_rect()
    textRect.center = (s_width/2,s_height*0.7)
    screen.blit(text, textRect)
    for button in round_buttons: 
        button.on_screen = True #zaznaczam ze guzik jest na ekranie, zeby pozniej byl nieklikalny kiedy zniknie z ekranu
        button.draw_button() #rysuje guziki z odpowiedza yes/no na ekranie

def letter_list(letter): #funkcja doajaca elementy do listy uzytych liter ktorych nie ma w hasle
    global wrong_x
    global wrong_y
    global wrong_letters
    wrong_letters.append([letter,[wrong_x,wrong_y]]) #przypisuje kazdej literce od razu wspolrzedne zeby sie wyswietlaly w danym miejscu
    # modyfikuje wspolrzedne kolejnych liter tak zeby wszystkie sie zmiescily w okreslonym okienku
    if wrong_x > 190:
        wrong_x = 55 
        wrong_y += 50
    else:
        wrong_x += 30

def print_wrong_letter(letters): #funkcja wypisujaca uzyte litery ktorych nie ma w hasle
    for letter in letters:
        text = wrong_font.render(letter[0],True,colors['red'])
        textRect = text.get_rect()
        textRect.center = letter[1] #uzywam wspolrzednych ktore kazdej literze przypisala funkcja 'letter list'
        screen.blit(text, textRect)

class button: #klasa opisujaca przyciski uzywane w grze
    def __init__(self,name,pos):
        self.color = colors['blue'] #wybieram kolor
        self.on_screen = False #zmienna logiczna odpowiadajaca za sprawdzanie czy dany przycisk jest na ekranie poniewaz bez niej dany fragment ekranu jest klikalny nawet kiedy guzik juz zniknal
        self.active = False #zmienna logiczna do sprawdzania czy kursor myszki jest na ekranie i zmieniania koloru przycisku
        self.name = name #tekst wyswietlany na guziku
        self.pos = pos #pozycja guzika
        self.surface = pygame.Surface((200,50)) # wyznaczam wymiary fragmentu ekranu na ktorym bedzie guzik
        self.surface.fill(self.color) #zapelniam ta powierzchnie kolorem
        self.text = default_font.render(self.name,True,colors['white'])

    def draw_button(self): #metoda rysujaca guzik na ekranie gry
        if self.active == True: #jesli jest aktywny czyli kursor jest na guziku to rozjasnij (takie interaktywne bajery)
            self.surface.set_alpha(150)
        else:
            self.surface.set_alpha(255) #jesli kursor nie jest na guzkiu to przywrodz normalna alfe
        screen.blit(self.surface,self.pos) #rysuje guzik w wybranych wspolrzednych 'pos'
        textRect = self.text.get_rect()
        textRect.center = (100,25) #wyznaczam wspolrzedne tekstu w srodku guzika 
        self.surface.blit(self.text,textRect)

round_buttons = [button('Yes',(300,600)),button('No',(s_width-500,600))] #tablica z guzikami rund, poniewaz iteruje rozne guziki w roznych miejscach kodu
alfabet = 'abcdefghijklmnopqrstuvwxyz'
wrong_letters = [] #tablica w ktorej zapisuje wprowadzone litery ktorych nie ma w hasle
running = True
while running: #no to lecim
    for event in pygame.event.get(): #badanie eventu
        if event.type == pygame.KEYDOWN: #sprawdzanie czy został wciśnięty jakiś klawisz
            if event.key == pygame.K_ESCAPE: #sprawdzanie czy wciśniętym klawiszem jest ESC
                running=False #wyjście z gry
            #jesli runda zostala przegrana to przestaje doadwac litery bledne do listy 'wrong_letters' 
        elif event.type == pygame.QUIT: #sprawdzanie czy został kliknięty przycisk zamknięcia okna
            running = False #wyjście z gry
        elif event.type == pygame.MOUSEMOTION: #wykrywam ruch kursora
            for button in round_buttons: #tu dzieje si eto samo co z przyciskami kategorii tylko dal przyciskow 'yes' i 'no' przy pytaniu o kolejna runde
                temp_rect = button.surface.get_rect(topleft=(button.pos[0],button.pos[1]))
                if temp_rect.collidepoint(pygame.mouse.get_pos()):
                    button.active = True
                else:
                    button.active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #wykrywam czy zostal wcisniety LPM
                if round_buttons[0].active == True and round_buttons[0].on_screen == True: #LPM wcisniety jesli na przycisku 'Yes' jest kursor i przycisk ten jest na ekranie powoduje wyzerownaie zmiennych kluczowych
                    #przywracam pierwotne wartosci zmiennych 
                    turns = 11
                    wrong_x=55
                    wrong_y=80
                    word = 'maslo trzaslo'
                    #czyszce tablice odgadnietych i zlych liter
                    wrong_letters.clear()
                    #usuwam mozliwosc klikniecia przyciskow yes/no poniewaz zaczyna si enowa partia
                    round_buttons[0].on_screen = False
                    round_buttons[1].on_screen = False
                if round_buttons[1].active == True and round_buttons[1].on_screen == True: #jesli przycisk 'No' zostanie wcisniety to gra sie konczy
                    running = False
    screen.fill((colors['white']))
    if turns>0:
        for letter in alfabet:
            if letter not in word and letter not in wrong_letters:
                letter_list(letter)
                turns -= 1
    else:            
        another_round()

    pygame.draw.rect(screen, colors['black'], [30,50,200,200],2) #rysuje 'okienko' w ktorym wypisywane beda bledne litery
    print_wrong_letter(wrong_letters) #wypisuje wybrane literki ktorych nie ma w hasle zeby uzytkownik wiedzial jakich liter nie uzywac ponownie
    
    pygame.display.flip() #odswierzam ekran zeby w ogole cokolwiek sie wyswietlalo XD
pygame.quit() #po przerwaniu petli zatrzymuje pygame

#Wisielec - projekt grupy Katowice - final
#porgram do dzialania wymaga umieszczenia w tym samym folderze pliku 'render_hangman.py' oraz folderu 'img'
import random
from tkinter import*
from tkinter import Tk, Canvas, Frame, BOTH, messagebox
from PIL import Image, ImageTk
from render_hangman import * #importuje modul Kingi ktory odpowiada za renderowanie wisielca na ekranie

#statystyki
liczba_prob = 10
liczba_wygranych = 0
liczba_przegranych = 0
wyniki = [] #przechowywanie danych z funkcji statystyki, żeby je później zniszczyc i zaktualizowac ich wynik

guessed=[] #tablica w ktorej zapisujemy poprawnie odgadniete litery
word = "" #haslo do gry
alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
animals = ["chimpanzee", "cockroach", "pigeon", "guinea pig", "herring", "sturgeon"]
# chimpanzee - szympans, cockroach - karaluch, pigeon - gołąb, guinea pig - świnka morska,
# herring - śledź, sturgeon - jesiotr (XD)
plants = ["almond tree", "cabbage", "buckeye", "clover", "hogweed", "sneezeweed"]
# almond tree - migdałowiec, cabbage - kapusta, buckeye - kasztanowiec, clover - koniczyna, hogeweed - barszcz,
# sneezeweed - dzielżan(taki kwiatek ładny)
professions = ["software engineer", "physiotherapist", "veterinarian", "maintenance man",
               "shipyard worker", "tax collector"]
# software engineer - inżynier oprogramowania, programista, physiotherapist - fizjoterapeura, veterinarian - weterynarz,
# maintenance man - konserwator, shipyard worker - pracownik stoczni, tax collector - poborca podatkowy
proverbs = ["an empty vessel makes much noise", "barking dogs seldom bite", "the show must go on",
            "you cant unscramble a scrambled egg", "all that glitters is not gold"]
# [0]foolish or stupid people are the most talkative, [1]people who appear threatening rarely do harm,
# [2]A performance, event, etc., must continue even though there are problems, [3]Some actions are irreversible,
# [4]Things that look good outwardly may not be as valuable or good

# tłumaczenia teoretycznie nie mają większego znaczenia, ale why not
# to suchar, ale jestem dumna z jesiotra w kategorii animals

main_window = Tk() # tworzę okno gry
main_window.title("Hangman") # tytuł utworzonego okna
main_window.geometry("1200x800") # wymiary okna gry
main_window.configure(bg='white') #ustawiam białe tło ekranu a pozniej tez innych obiektów poniewaz pojedyncze klatki wisielca maja biale tlo

wisiel = Render_controler() #uruchamiam klase ktora odpowiada za renderowanie wisielca
wisiel.load_images() #laduje obrazy z folderu 'img' ktory powinien znajdowac sie w tym samym folderze w ktorym znajduje sie plik z tym kodem oraz plikiem 'render_hangman'

#funkcja, która wyświetla liczby wygranych i przegranych rund oraz pozostałych prób
def statystyki(wygrane, przegrane, proby): 
    wygrane_rundy = Label(main_window, text= 'Wins: '+str(wygrane), font=(None,15),bg='white')
    wyniki.append(wygrane_rundy)
    wygrane_rundy.place(x=1100, y=200, anchor='center')

    przegrane_rundy = Label(main_window, text= 'Loses: '+str(przegrane), font=(None,15),bg='white')
    wyniki.append(przegrane_rundy)
    przegrane_rundy.place(x=1100, y=250, anchor='center')

    pozostale_proby = Label(main_window, text= 'Turns left: '+str(liczba_prob), font=(None,15),bg='white')
    wyniki.append(pozostale_proby)
    pozostale_proby.place(x=1100, y=300, anchor='center')

#funkcja, która wypisuje hasło na ekranie
def wypisywanie_hasla(): 
    global word
    global guessed
    global lancuch_znakow
    global liczba_wygranych
    global zasloniete
    zasloniete = len(word) #zmienna sluzaca dosprawdzania ile liter wyswietla sie jako zasloniete
    ukryte_haslo = '' #pusty łańcuch znaków, w którym zostaną zapisane litery, spacje i podłogi, a później zostanie wyświetlony na ekranie
    for litera in word:
        if litera == ' ':
            ukryte_haslo += ' ' #jeśli w haśle jest spacja to dodawana jest przerwa do łańcucha
            zasloniete -= 1 
        else: #jeśli litera nie jest spacją to zostaje sprawdzone, czy została już odgadnięta
            if litera in guessed:
                ukryte_haslo += litera #jeśli została odgadnięta to dodawana jest do łańcucha znaków
                zasloniete -= 1
            else:
                ukryte_haslo += '_' #jeśli litera nie została odgadnięta to dodawana jest do łańcucha znaków w jej miejscu podłoga
        ukryte_haslo += ' ' #dodanie przerwy między literami, aby podłogi się nie łączyły
    #umieszczanie łańcucha znaków na ekranie
    lancuch_znakow = Label(main_window, text=ukryte_haslo, font=(None,30),bg='white')
    lancuch_znakow.place(x=600, y=480, anchor='center')
    if zasloniete == 0: #jesli wszystkie litery w hasle zostaly odsloniete to zwiekszam licznik wygranych o 1 i wyswietlam odpowiedni komunikat
        liczba_wygranych += 1
        for statystyka in wyniki: #niszczenie statystyk wypisanych wczesniej na ekranie, żeby móc je zaktualizować
            statystyka.destroy()
        statystyki(liczba_wygranych,liczba_przegranych,liczba_prob)
        messagebox.showinfo("Winner!", "Congratulations, you've won!!!\nTo play another round press the \'New game\' button")

def wrong_window(): #funkcja tworząca na ekranie okienko w ktorym wypisywane pozniej beda wybrane litery ktorychnie ma w hasle, czyli bledy
    global canvas
    global wrong_guesses_label
    global stat_label
    canvas = Canvas(main_window,bg='white') #tworze canvas na ktorym narysuje prostokat w ktorym beda bledne litery oraz do nktorego beda ladowane kolejne obrazy z klatkami wisielca
    canvas.create_rectangle(30, 50, 300, 290, outline='red', width=2) #rysuje prostokat na canvasie
    canvas.create_rectangle(1030, 170, 1170, 340, outline='blue', width=2) 
    canvas.pack(fill=BOTH, expand=True)
    wrong_guesses_label = Label(main_window, text= 'Wrong guesses',font=(None,20),fg='red',bg='white') #podpisuje okienko z blednymi literami, zeby gracz wiedzial do czego ono sluzy
    wrong_guesses_label.place(x=70,y=5)
    stat_label = Label(main_window, text= 'Stats',font=(None,20),fg='blue',bg='white') #podpisuje okienko z blednymi literami, zeby gracz wiedzial do czego ono sluzy
    stat_label.place(x=1100,y=140,anchor='center')

def caategory_selection_label(): #wypisywanie pytania o kategorie w kodzie Oliwii zamienilem w funkcje zeby latwiej je wyswietlac przy restarcie ekranu po wyborze nowej gry
    global tekst
    tekst = StringVar() # zmienna, dzięki której ustawię tekst na ekranie początkowym i potem będę mogła go nadpisywać
    tekst.set("Which category from list do you \nwant to choose?") # ustawienie treści
    category_selection = Label(main_window, textvariable=tekst, fg="blue",bg='white') # tworzę tekst, który wyświetli się na ekranie
    category_selection.config(font=("Courier, 30")) # modyfikacja labela
    category_selection.place(x=330,y=50) # ustawienie pozycji labela
    category_selection = Entry(main_window)

def category_selection1():
    global word # zmienna word będzie działała dzięki temu również poza tą funkcją, a nie tylko wewnątrz niej
    word = random.choice(animals) # funkcja ma sprawić, że po naciśnięciu przycisku ANIMALS itd. losuje się słowo z tej listy
    # messagebox.showinfo("Hejka", word) # messagebox'y były do sprawdzenia, czy wszystko śmiga (czy losuje się hasło po naciśnięciu przycisku)
    tekst.set("") # nadpisuje label pustym tekstem, żeby po wciśnięciu przycisku też zniknął z ekranu
    category1.destroy() # destroy - jeżeli zostanie wciśnięty przycisk z wyborem kategorii to następnie wszystkie przyciski mają zniknąć, żeby przejść do dalszej części gry
    category2.destroy()
    category3.destroy()
    category4.destroy()
    #dopiero po wybraniu kategorii i zniszczeniu obiektow z dotychczasowego okna inicjuje tworzenie nowych
    wrong_window() #tworze okienko w ktorym beda blednie wybrane litery
    button_action() #uruchamiam tworzenie przyciskow z guzikami liter
    wypisywanie_hasla()
    statystyki(liczba_wygranych,liczba_przegranych,liczba_prob)
    #print(word) #wypisywalem haslo w konsoli w celu sprawdzania funkcji ktore go dotycza

def category_selection2():
    global word
    word = random.choice(plants)
    # messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()
    wrong_window()
    button_action()
    wypisywanie_hasla()
    statystyki(liczba_wygranych,liczba_przegranych,liczba_prob)
    #print(word)

def category_selection3():
    global word
    word = random.choice(professions)
    # messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()
    wrong_window()
    button_action()
    wypisywanie_hasla()
    statystyki(liczba_wygranych,liczba_przegranych,liczba_prob)
    #print(word)

def category_selection4():
    global word
    word = random.choice(proverbs)
    # messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()
    wrong_window()
    button_action()
    wypisywanie_hasla()
    statystyki(liczba_wygranych,liczba_przegranych,liczba_prob)
    #print(word)

def category_buttons(): #tworzenie guzikow w kodzie Oliwii wstawilem w funkcje zeby przy wybraniu nowej gry szybko wywolac ten fragment kodu
    global category1 #category1, 2, 3 i 4 zamieniem w zmienne globalne zeby mozna bylo je niszczyc poza funkcja 'category_buttons' 
    global category2
    global category3
    global category4
    # tworzę przyciski z nazwami kategorii i podpinam pod nie funkcje, które (po naciśnięciu przyciku) mają losować słowo z danej kategorii
    category1 = Button(main_window, text="ANIMALS", fg="red", width=20, height=4, command = category_selection1,font=(None,10))
    category1.place(x=200,y=300)
    category2 = Button(main_window, text="PLANTS", fg="red", width=20, height=4, command = category_selection2,font=(None,10))
    category2.place(x=400, y=300)
    category3 = Button(main_window, text="PROFESSIONS", fg="red", width=20, height=4, command = category_selection3,font=(None,10))
    category3.place(x=600, y=300)
    category4 = Button(main_window, text="PROVERBS", fg="red", width=20, height=4, command = category_selection4,font=(None,10))
    category4.place(x=800, y=300)

wrong_x =  45 #wspolrzedna x dla pierwszej blednej litery
wrong_y = 60 #wspolrzedna y dla pierwszej blednej litery
wrong_letters = [] #tablica do zapisywania blednie wybranych liter
letter_labels = [] #tworze tablice do ktorej bede zapisywal labele z kolejnymi blednymi literami ktore wypisuje zeby przy wyborze nowej gry szybko je usuwac
def print_wrong_letter(letter): #funkcja wypisujaca bledna litere w okienku tworzonym w funkcji 'wrong_window', wywoluje ja tylko jesli wybrana litera nie jest w hasle
    global wrong_x
    global wrong_y
    global wrong_letters
    global letter_labels
    global canvas
    global liczba_prob
    global wyniki
    global liczba_przegranych
    global word
    if letter not in wrong_letters: #sprawdzam czy litera nie zostala juz wybrana wczesniej, zeby kazdy blad wyswietlal sie w okienku tylko raz
        liczba_prob -= 1 #zmniejszam liczbe prob o 1 poniewaz wybrana zostala nowa litera ktorej nie ma w hasle 
        if liczba_prob < 1:
            liczba_przegranych += 1
        for statystyka in wyniki: #niszczenie statystyk wypisanych wczesniej na ekranie, żeby móc je zaktualizować
            statystyka.destroy()
        statystyki(liczba_wygranych,liczba_przegranych,liczba_prob)
        label = Label(main_window, text= letter,font=(None,20),bg='white') #tworze label z uzyta litera ktory pozniej ozstanie dodany na ekranie
        letter_labels.append(label) #dolaczam ten label do listy z ktorej pozniej bede bral argumenty zeby je usuwac z ekranu po wyborze nowej gry
        label.place(x=wrong_x,y=wrong_y)
        wrong_letters.append(letter) #dodaje litere do tablicy 'wrong_letters' zeby sprawdzac ktore litery zostaly juz uzyte i nie wypisywac ich drugi raz
        wisiel.show_next(canvas,word) #przy bledzie wyswietlam kolejna klatke wisielca z kodu Kingi, Oliwia zauwazyla ze pomocne moze byc wyswietlanie hasla uzytkownikowi kiedy go nie odgadnal zeby wiedzial jakie bylo wiec dodalem tekst do okna z informacja w module 'render_hangman' i dlatego wstawiam 'word' jako argument funkcji
    # modyfikuje wspolrzedne kolejnych liter tak zeby wszystkie sie zmiescily w okreslonym okienku
        if wrong_x > 240:
            wrong_x = 45
            wrong_y += 50
        else:
            wrong_x += 30

def nowa_gra(): #tutaj resetuje zmienne odpowiedzialne za przebieg jednej rozgrywki jesli gracz wybierze nowa gre 
    global wrong_x
    global wrong_y
    global word
    global wrong_letters
    global wyniki
    global liczba_prob
    liczba_prob = 10
    wisiel.counter = 0 #resetuje licznik tur w module 'render_hangaman' Kingi zeby w nowej rozgrywce przy bledach kolejne klatki wyswietlaly sie od nowa
                        #w przeciwnym razie wyswietlalyby sie dalej od miejsca w ktoym wybralo sie nowa rozgrywke
    wrong_x = 45 #przywracam wspolrzedne x i y pierwszej zlej litery do pierwotnych ustawien zeby w nowej rozgrywce wypisywaly sie w tym samym miejscu co poprzednie
    wrong_y = 60
    # teraz resetuje ekran, zeby wrocic do ekranu wyboru kategorii:
    for button in letter_buttons:
        button.destroy() #usuwam z ekranu guzki z literami
    for label in letter_labels:
        label.destroy() #usuwam wypisane w okienku 'wrong_window' litery
    for statystyka in wyniki: #niszczenie statystyk wypisanych wczesniej na ekranie, żeby móc je zaktualizować
        statystyka.destroy()
    canvas.destroy() #usuwam canvas na ktoym wypisany jest prostokat okienka 'wrong_window' i dany obraz z wisielcem
    wrong_guesses_label.destroy() #usuwam tytuly okienka z bledami i statystykami
    stat_label.destroy()
    guessed.clear()
    wrong_letters.clear() #czyszcze liste zapisanych blednych liter zeby w kolejnej rozgrywce zapisywac bledy od nowa
    przycisk_nowa_gra.destroy() #usuwam przyciski nowej gry i quit poniewaz wydaje mi sie ze nie sa potrzebne na tym ekranie    
    QUIT.destroy()
    lancuch_znakow.destroy()
    #messagebox.showinfo('Restart','Let\'s play another round! :)') #informuje gracza o restarcie
    #od nowa tworze ekran wyboru kategorii:
    caategory_selection_label() #wyswietlam pytanie o wybor kategorii
    category_buttons() #wyswietlam guziki wyboru kategorii

# no i teraz funkcje, które umożliwią przypisanie każdemu przyciskowi odpowiadającej mu litery
# to lecim
def letter_A():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0: #ten warunek sluzy do zablokowania funkcji guzikow w przyapdku wygranej (kiedy liczba zaslonietych liter osiagnie 0) lub przegranej (kiedy liczba_prob osiagnie 0)
        if "a" in word:
            if "a" not in guessed:
                guessed.append("a") # jeżeli dana literka jest w wylosowanym wcześniej słowie i nie ma jej na liście już zgadniętych liter to zostaje ona do niej dodana
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('a') #jesli danej litery nie ma w hasle zostaje odeslana do funkcji ktora ja przetworzy jako blad i wykona odpowiednie operacje
#to samo powtarza sie kolejne 25 razy dla pozostalych liter:
def letter_B():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "b" in word:
            if "b" not in guessed:
                guessed.append("b")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('b')
def letter_C():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "c" in word:
            if "c" not in guessed:
                guessed.append("c")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('c')
def letter_D():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "d" in word:
            if "d" not in guessed:
                guessed.append("d")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('d')
def letter_E():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "e" in word:
            if "e" not in guessed:
                guessed.append("e")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('e')
def letter_F():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "f" in word:
            if "f" not in guessed:
                guessed.append("f")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('f')
def letter_G():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "g" in word:
            if "g" not in guessed:
                guessed.append("g")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('g')
def letter_H():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "h" in word:
            if "h" not in guessed:
                guessed.append("h")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('h')
def letter_I():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "i" in word:
            if "i" not in guessed:
                guessed.append("i")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('i')
def letter_J():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "j" in word:
            if "j" not in guessed:
                guessed.append("j")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('j')
def letter_K():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "k" in word:
            if "k" not in guessed:
                guessed.append("k")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('k')
def letter_L():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "l" in word:
            if "l" not in guessed:
                guessed.append("l")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('l')
def letter_M():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "m" in word:
            if "m" not in guessed:
                guessed.append("m")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('m')
def letter_N():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "n" in word:
            if "n" not in guessed:
                guessed.append("n")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('n')
def letter_O():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "o" in word:
            if "o" not in guessed:
                guessed.append("o")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('o')
def letter_P():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "p" in word:
            if "p" not in guessed:
                guessed.append("p")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('p')
def letter_Q():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "q" in word:
            if "q" not in guessed:
                guessed.append("q")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('q')
def letter_R():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "r" in word:
            if "r" not in guessed:
                guessed.append("r")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('r')
def letter_S():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "s" in word:
            if "s" not in guessed:
                guessed.append("s")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('s')
def letter_T():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "t" in word:
            if "t" not in guessed:
                guessed.append("t")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('t')
def letter_U():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "u" in word:
            if "u" not in guessed:
                guessed.append("u")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('u')
def letter_V():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "v" in word:
            if "v" not in guessed:
                guessed.append("v")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('v')
def letter_W():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "w" in word:
            if "w" not in guessed:
                guessed.append("w")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('w')
def letter_X():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "x" in word:
            if "x" not in guessed:
                guessed.append("x")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('x')
def letter_Y():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "y" in word:
            if "y" not in guessed:
                guessed.append("y")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('y')
def letter_Z():
    global word
    global guessed
    global liczba_prob
    global zasloniete
    if liczba_prob > 0 and zasloniete > 0:
        if "z" in word:
            if "z" not in guessed:
                guessed.append("z")
                lancuch_znakow.destroy()
                wypisywanie_hasla()
        else:
            print_wrong_letter('z')

# lista zbierająca wszystkie powyższe funkcje, żeby można było ją następnie przypisać do funkcji, która tworzy przyciski za pomocą pętli
Letters = [letter_A, letter_B, letter_C, letter_D, letter_E, letter_F, letter_G, letter_H, letter_I, letter_J, letter_K, letter_L, letter_M, letter_N, letter_O, letter_P, letter_Q, letter_R, letter_S, letter_T, letter_U, letter_V, letter_W, letter_X, letter_Y, letter_Z]

# teraz z kolei funkcja, która utworzy te przyciski z literami
def button_action():
    global Letters #udostepniamy funkcji liste funkcji dla konkretnych liter
    #definiujemy zmienne globalne, dzieki czemu lawtiej bedzie je usunac przy zmianie ekranu
    global letter_buttons
    global QUIT
    global przycisk_nowa_gra
    letter_buttons = [] #tworze tablice do ktorej bede zapisywal guziki z literami tworzone przez Oliwie, zeby sprawnie je usunac przy uruchamianiu nowej gry
    letter_x = 155
    letter_y = 550 # współrzędne dla pierwszego wyświetlającego się guzika
    for index, letter in enumerate(alfabet):
        letter_buttons.append(Button(main_window, text = letter, bg="yellow", fg="red", width=4, height=2,font=(None,15), command=Letters[index]))
        # każdej literze z listy "alfabet" na przycisku odpowiada funkcja z listy "Letters" o tym samym indeksie, ze względu na to, że liter jak i funkcji dla każdej z nich (logiczne) będzie tyle samo
        # enumerate(alfabet) zwraca indeks elementu i przypisany mu element listy, a więc do przycisku z "A" ("A" ma indeks [0] w alfabecie) podepnie funkcję letter_A, która ma indeks [0] na liście Letters
    for button in letter_buttons:
        button.place(x=letter_x, y=letter_y) #umiejscawiamy przyciski z literami na ekranie
        if letter_buttons.index(button) == 12: # kiedy pojawia się przycisk "M" reszta przycisków zaczyna wyświetlać się w następnej 'linijce' (dzięki letter_y = 620) w tym samym miejscu, w którym zaczynała się poprzednia linijka z przyciskami (dzięki letter_x = 155)
            letter_x = 155
            letter_y = 620
        else: # w przypadku pozostałych przycisków odległość między nimi, czyli x, zwiększa się o 70 (żeby nie zachodziły na siebie)
            letter_x += 70
    
    QUIT = Button(main_window,text = "QUIT",fg='red',command=main_window.quit,font=(None,15)) #tworze na ekranie guzik ewentualnego wyjscia z gry jesli uzytkownik bedzie mial taka ochote
    QUIT.place(x=1130,y=0)
    przycisk_nowa_gra=Button(main_window,text='New game',command=nowa_gra,font=(None,15)) #tworze guzik do wyboru nowej gry w przypadku przegranej lub wygranej jesli uzytkownik bedzie mial ochote grac dalej 
    przycisk_nowa_gra.place(x=1020,y=0)

#po calym tym kodzie pelnym funkcji w koncu cos odpalamy na ekranie czyli pytanie o wybor kategorii oraz guziki do wyboru ktorejs, co pozniej odpala kaskade wypisywania omowionych wyzej rzeczy na ekranie
caategory_selection_label()
category_buttons()

main_window.mainloop()

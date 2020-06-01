# Wybór kategorii hasła oraz losowanie hasła z wybranej kategorii

import random
from tkinter import*
from tkinter import messagebox

guessed=[]
word = ""
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
proverbs = ["An empty vessel makes much noise", "Barking dogs seldom bite", "The show must go on",
            "You cant unscramble a scrambled egg", "All that glitters is not gold"]
# [0]foolish or stupid people are the most talkative, [1]people who appear threatening rarely do harm,
# [2]A performance, event, etc., must continue even though there are problems, [3]Some actions are irreversible,
# [4]Things that look good outwardly may not be as valuable or good

# tłumaczenia teoretycznie nie mają większego znaczenia, ale why not
# to suchar, ale jestem dumna z jesiotra w kategorii animals

main_window = Tk() # tworzę okno gry
main_window.title("Hangman") # tytuł utworzonego okna
main_window.geometry("1200x800") # wymiary okna gry

# label = ("Which category from list do you \nwant to choose?")
tekst = StringVar() # zmienna, dzięki której ustawię tekst na ekranie początkowym i potem będę mogła go nadpisywać
tekst.set("Which category from list do you \nwant to choose?") # ustawienie treści
category_selection = Label(main_window, textvariable=tekst, fg="blue") # tworzę tekst, który wyświetli się na ekranie
category_selection.config(font=("Courier, 30")) # modyfikacja labela
category_selection.place(x=350,y=50) # ustawienie pozycji labela
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
    button_action()

def category_selection2():
    global word
    word = random.choice(plants)
    # messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()
    button_action()

def category_selection3():
    global word
    word = random.choice(professions)
    # messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()
    button_action()

def category_selection4():
    global word
    word = random.choice(proverbs)
    # messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()
    button_action()

category1 = Button(main_window, text="ANIMALS", fg="red", width=25, height=5, command = category_selection1)
category1.place(x=200,y=300)
# tworzę przyciski z nazwami kategorii i podpinam pod nie funkcje, które (po naciśnięciu przyciku) mają losować słowo z danej kategorii
category2 = Button(main_window, text="PLANTS", fg="red", width=25, height=5, command = category_selection2)
category2.place(x=400, y=300)
category3 = Button(main_window, text="PROFESSIONS", fg="red", width=25, height=5, command = category_selection3)
category3.place(x=600, y=300)
category4 = Button(main_window, text="PROVERBS", fg="red", width=25, height=5, command = category_selection4)
category4.place(x=800, y=300)


# no i teraz funkcje, które umożliwią przypisanie każdemu przyciskowi odpowiadającej mu litery
# to lecim

def letter_A():
    global word
    global guessed
    if "a" in word and "a" not in guessed:
        guessed.append("a") # jeżeli dana literka jest w wylosowanym wcześniej słowie i nie ma jej na liście już zgadniętych liter to zostaje ona do niej dodana

def letter_B():
    global word
    global guessed
    if "b" in word and "b" not in guessed:
        guessed.append("b")

def letter_C():
    global word
    global guessed
    if "c" in word and "c" not in guessed:
        guessed.append("c")

def letter_D():
    global word
    global guessed
    if "d" in word and "d" not in guessed:
        guessed.append("d")

def letter_E():
    global word
    global guessed
    if "e" in word and "e" not in guessed:
        guessed.append("e")

def letter_F():
    global word
    global guessed
    if "f" in word and "f" not in guessed:
        guessed.append("f")

def letter_G():
    global word
    global guessed
    if "g" in word and "g" not in guessed:
        guessed.append("g")

def letter_H():
    global word
    global guessed
    if "h" in word and "h" not in guessed:
        guessed.append("h")

def letter_I():
    global word
    global guessed
    if "i" in word and "i" not in guessed:
        guessed.append("i")

def letter_J():
    global word
    global guessed
    if "j" in word and "j" not in guessed:
        guessed.append("j")

def letter_K():
    global word
    global guessed
    if "k" in word and "k" not in guessed:
        guessed.append("k")

def letter_L():
    global word
    global guessed
    if "l" in word and "l" not in guessed:
        guessed.append("l")

def letter_M():
    global word
    global guessed
    if "m" in word and "m" not in guessed:
        guessed.append("m")

def letter_N():
    global word
    global guessed
    if "n" in word and "n" not in guessed:
        guessed.append("n")

def letter_O():
    global word
    global guessed
    if "o" in word and "o" not in guessed:
        guessed.append("o")

def letter_P():
    global word
    global guessed
    if "p" in word and "p" not in guessed:
        guessed.append("p")

def letter_Q():
    global word
    global guessed
    if "q" in word and "q" not in guessed:
        guessed.append("q")

def letter_R():
    global word
    global guessed
    if "r" in word and "r" not in guessed:
        guessed.append("r")

def letter_S():
    global word
    global guessed
    if "s" in word and "s" not in guessed:
        guessed.append("s")

def letter_T():
    global word
    global guessed
    if "t" in word and "t" not in guessed:
        guessed.append("t")

def letter_U():
    global word
    global guessed
    if "u" in word and "u" not in guessed:
        guessed.append("u")

def letter_V():
    global word
    global guessed
    if "v" in word and "v" not in guessed:
        guessed.append("v")

def letter_W():
    global word
    global guessed
    if "w" in word and "w" not in guessed:
        guessed.append("w")

def letter_X():
    global word
    global guessed
    if "x" in word and "x" not in guessed:
        guessed.append("x")

def letter_Y():
    global word
    global guessed
    if "y" in word and "y" not in guessed:
        guessed.append("y")

def letter_Z():
    global word
    global guessed
    if "z" in word and "z" not in guessed:
        guessed.append("z")

# lista zbierająca wszystkie powyższe funkcje, żeby można było ją następnie przypisać do funkcji, która tworzy przyciski za pomocą pętli
Letters = [letter_A, letter_B, letter_C, letter_D, letter_E, letter_F, letter_G, letter_H, letter_I, letter_J, letter_K, letter_L, letter_M, letter_N, letter_O, letter_P, letter_Q, letter_R, letter_S, letter_T, letter_U, letter_V, letter_W, letter_X, letter_Y, letter_Z]

# teraz z kolei funkcja, która utworzy te przyciski z literami
def button_action():
    global Letters
    letter_x = 155
    letter_y = 550 # współrzędne dla pierwszego wyświetlającego się guzika
    for index, letter in enumerate(alfabet):
        button = Button(main_window, text = letter, bg="yellow", fg="red", width=4, height=2,font=(None,15), command=Letters[index])
        # każdej literze z listy "alfabet" na przycisku odpowiada funkcja z listy "Letters" o tym samym indeksie, ze względu na to, że liter jak i funkcji dla każdej z nich (logiczne) będzie tyle samo
        # enumerate(alfabet) zwraca indeks elementu i przypisany mu element listy, a więc do przycisku z "A" ("A" ma indeks [0] w alfabecie) podepnie funkcję letter_A, która ma indeks [0] na liście Letters
        button.place(x=letter_x, y=letter_y)
        if letter == 'M': # kiedy pojawia się przycisk "M" reszta przycisków zaczyna wyświetlać się w następnej 'linijce' (dzięki letter_y = 620) w tym samym miejscu, w którym zaczynała się poprzednia linijka z przyciskami (dzięki letter_x = 155)
            letter_x = 155
            letter_y = 620
        else: # w przypadku pozostałych przycisków odległość między nimi, czyli x, zwiększa się o 70 (żeby nie zachodziły na siebie)
            letter_x += 70

main_window.mainloop()

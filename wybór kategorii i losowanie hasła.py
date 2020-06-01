# Wybór kategorii hasła oraz losowanie hasła z wybranej kategorii

import random
from tkinter import*
from tkinter import messagebox

word = ""
letter = ""
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
# proverbsy nie mają tłumaczeń po polsku celowo, bo może po odgadnięciu hasła z tej kategorii
# można też wtedy wyświetlić znaczenie proverbsa :D mały dodatek, tak dla funu

main_window = Tk()
main_window.title("Hangman")
main_window.geometry("1200x800") # wymiary okna gry

# label = ("Which category from list do you \nwant to choose?")
tekst = StringVar()
tekst.set("Which category from list do you \nwant to choose?")
category_selection = Label(main_window, textvariable=tekst, fg="blue")
category_selection.config(font=("Courier, 30")) # modyfikacja tekstu
category_selection.place(x=350,y=50) # ustawienie pozycji tekstu
category_selection = Entry(main_window)

def category_selection1():
    global word # zmienna word będzie działała dzięki temu również poza tą funkcją, a nie tylko wewnątrz niej
    word = random.choice(animals) # funkcja ma sprawić, że po naciśnięciu przycisku ANIMALS itd. losuje się słowo z tej listy
    # messagebox.showinfo("Hejka", word) # messagebox'y były do sprawdzenia, czy wszystko śmiga
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

# funkcja, która utworzy przyciski z literami
def button_action():
    letter_x = 155
    letter_y = 550
    for letter in alfabet:
        button = Button(main_window, text = letter, bg="yellow", fg="red", width=4, height=2,font=(None,15))
        button.place(x=letter_x, y=letter_y)
        if letter == 'M': # do momentu, w którym pojawi się na przyciku litera "M" przyciski wyświetlają się w miejscu x=155, y=620
            letter_x = 155
            letter_y = 620
        else: # przyciski z literami po literze "M" wyświetlają się w miejscu x=225(155+70), y=620
            letter_x += 70

# no i teraz funkcje, które umożliwią przypisanie każdemu przyciskowi odpowiadającej mu litery
# to lecim
def letter_A():
    global word
    global guessed
    if "A" in word and "A" not in guessed:
        guessed.append("A") # jeżeli dana literka jest w wylosowanym słowie i nie ma jej na liście już zgadniętych liter to zostaje ona do niej dodana

def letter_B():
    global word
    global guessed
    if "B" in word and "B" not in guessed:
        guessed.append("B")

def letter_C():
    global word
    global guessed
    if "C" in word and "C" not in guessed:
        guessed.append("C")

def letter_D():
    global word
    global guessed
    if "D" in word and "D" not in guessed:
        guessed.append("D")

def letter_E():
    global word
    global guessed
    if "E" in word and "E" not in guessed:
        guessed.append("E")

def letter_F():
    global word
    global guessed
    if "F" in word and "F" not in guessed:
        guessed.append("F")
def letter_G():
    global word
    global guessed
    if "G" in word and "G" not in guessed:
        guessed.append("G")

def letter_G():
    global word
    global guessed
    if "G" in word and "G" not in guessed:
        guessed.append("G")

def letter_H():
    global word
    global guessed
    if "H" in word and "H" not in guessed:
        guessed.append("H")

def letter_I():
    global word
    global guessed
    if "I" in word and "I" not in guessed:
        guessed.append("I")

def letter_J():
    global word
    global guessed
    if "J" in word and "J" not in guessed:
        guessed.append("J")

def letter_K():
    global word
    global guessed
    if "K" in word and "K" not in guessed:
        guessed.append("K")

def letter_L():
    global word
    global guessed
    if "L" in word and "L" not in guessed:
        guessed.append("L")

def letter_M():
    global word
    global guessed
    if "M" in word and "M" not in guessed:
        guessed.append("M")

def letter_N():
    global word
    global guessed
    if "N" in word and "N" not in guessed:
        guessed.append("N")

def letter_O():
    global word
    global guessed
    if "O" in word and "O" not in guessed:
        guessed.append("O")

def letter_P():
    global word
    global guessed
    if "P" in word and "P" not in guessed:
        guessed.append("P")

def letter_Q():
    global word
    global guessed
    if "Q" in word and "Q" not in guessed:
        guessed.append("Q")

def letter_R():
    global word
    global guessed
    if "R" in word and "R" not in guessed:
        guessed.append("R")

def letter_S():
    global word
    global guessed
    if "S" in word and "S" not in guessed:
        guessed.append("S")

def letter_T():
    global word
    global guessed
    if "T" in word and "T" not in guessed:
        guessed.append("T")

def letter_U():
    global word
    global guessed
    if "U" in word and "U" not in guessed:
        guessed.append("U")

def letter_V():
    global word
    global guessed
    if "V" in word and "V" not in guessed:
        guessed.append("V")

def letter_W():
    global word
    global guessed
    if "W" in word and "W" not in guessed:
        guessed.append("W")

def letter_X():
    global word
    global guessed
    if "X" in word and "X" not in guessed:
        guessed.append("X")

def letter_Y():
    global word
    global guessed
    if "Y" in word and "Y" not in guessed:
        guessed.append("Y")

def letter_Z():
    global word
    global guessed
    if "Z" in word and "Z" not in guessed:
        guessed.append("Z")

Letters = [letter_A(), letter_B(), letter_C(), letter_D(), letter_E(), letter_F(), letter_G(), letter_H(), letter_I(), letter_J(), letter_K(), letter_L(), letter_M(), letter_N(), letter_O(), letter_P(), letter_Q(), letter_R(), letter_S(), letter_T(), letter_U(), letter_V(), letter_W(), letter_X(), letter_Y(), letter_Z()]

main_window.mainloop()

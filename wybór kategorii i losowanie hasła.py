# Wybór kategorii hasła oraz losowanie hasła z wybranej kategorii

import random
from tkinter import*
from tkinter import messagebox

word = ""
letter = ""
# alfabet = "abcdefghijklmnopqrstuvwxyz"
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
    word = random.choice(animals) # funkcja ma sprawić, że po naciśnięciu przycisku ANIMALS itd. losuje się słowo z tej listy
    #messagebox.showinfo("Hejka", word) # messagebox'y były do sprawdzenia, czy wszystko śmiga
    tekst.set("") # nadpisuje label pustym tekstem, żeby po wciśnięciu przycisku też zniknął z ekranu 
    category1.destroy() # destroy - jeżeli zostanie wciśnięty przycisk z wyborem kategorii to następnie wszystkie przyciski mają zniknąć, żeby przejść do dalszej części gry
    category2.destroy()
    category3.destroy()
    category4.destroy()

def category_selection2():
    word = random.choice(plants)
    #messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()

def category_selection3():
    word = random.choice(professions)
    #messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()

def category_selection4():
    word = random.choice(proverbs)
    #messagebox.showinfo("Hejka", word)
    tekst.set("")
    category1.destroy()
    category2.destroy()
    category3.destroy()
    category4.destroy()

category1 = Button(main_window, text="ANIMALS", fg="red", width=25, height=5, command = category_selection1)
category1.place(x=200,y=300)
# tworzę przyciski z nazwami kategorii i podpinam pod nie funkcje, które (po naciśnięciu przyciku) mają losować słowo z danej kategorii
category2 = Button(main_window, text="PLANTS", fg="red", width=25, height=5, command = category_selection2)
category2.place(x=400, y=300)
category3 = Button(main_window, text="PROFESSIONS", fg="red", width=25, height=5, command = category_selection3)
category3.place(x=600, y=300)
category4 = Button(main_window, text="PROVERBS", fg="red", width=25, height=5, command = category_selection4)
category4.place(x=800, y=300)

main_window.mainloop()

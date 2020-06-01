from tkinter import Tk, Canvas, Frame, BOTH, messagebox
from tkinter import *

word = 'haslo maslo' #przykladowe haslo
alfabet ='qwertyuiopasdfghjklzxcvbnm' #alfabet do sprawdzania ktore litery sa w hasle
wrong_x =  45 #wspolrzedna x dla pierwszej blednej litery
wrong_y = 60 #wspolrzedna y dla pierwszej blednej litery
wrong_letters = [] #tablica do zapisywania blednie wybranych liter
turns=11 #przykladowa liczba tur

def letter_list(letter,wrong_letters): #funkcja dodajaca elementy do listy uzytych liter ktorych nie ma w hasle
    global wrong_x
    global wrong_y
    wrong_letters.append([letter,[wrong_x,wrong_y]]) #przypisuje kazdej literce od razu wspolrzedne zeby sie wyswietlaly w danym miejscu
    # modyfikuje wspolrzedne kolejnych liter tak zeby wszystkie sie zmiescily w okreslonym okienku
    if wrong_x > 240:
        wrong_x = 45
        wrong_y += 50
    else:
        wrong_x += 30

def print_wrong_letter(letters,screen): #funkcja wypisujaca uzyte litery ktorych nie ma w hasle
    for letter in letters:
            label = Label(screen, text= letter[0],font=(None,20))
            label.place(x=letter[1][0],y=letter[1][1])
class App(Frame): #klasa zarzadzajaca ekranem
    def __init__(self):
        super().__init__()
        self.wrong_window() #tworze 'okienko' na ekranie w ktorym beda wyswietlane bledne litery
        self.buttons() #tworze guziki wyjscia i nowej gry
    def nowa_gra(self): #tutaj resetuje zmienne odpowiedzialne za przebieg jednej rozgrywki jesli gracz wybierze nowa gre 
        global turns
        global wrong_x
        global wrong_y
        global word
        word ='qwerty'
        turns = 11
        wrong_x = 45
        wrong_y = 60
        wrong_letters.clear()
        messagebox.showinfo('Nowa gra','Restart')
    def buttons(self): #funkcja do tworzenia guzikow 'nowa gra' i 'quit'
        self.QUIT = Button(self,text = "QUIT",fg='red',command=self.quit,font=(None,15))
        self.QUIT.place(x=1100,y=0)
        
        self.przycisk_nowa_gra=Button(self,text='Nowa\ngra',command=self.nowa_gra,font=(None,15))
        self.przycisk_nowa_gra.place(x=1000,y=0)        
    def wrong_window(self):
        self.master.title("HANGMAN")
        self.pack(fill=BOTH, expand=1)
        label = Label(root, text= 'Wrong guesses',font=(None,20),fg='red') #podpisuje okienko z blednymi literami zeby gracz wiedzial jakich uzyl
        label.place(x=70,y=0)
        canvas = Canvas(self) #tworze canvas na ktorym narysuje prostokat w ktorym beda bledne litery
        canvas.create_rectangle(30, 50, 300, 290, outline="#f11", width=2)
        canvas.pack(fill=BOTH, expand=1)

root = Tk() #tworze ekran
app = App() #uruchamiam klase ktora wypisuje rzeczy na ekranie
root.geometry("1200x800")
for letter in alfabet:
    if letter not in word and letter not in wrong_letters and turns>0: #jesli litera nie jest w hasle i nie ma jej jeszcze w uztych blednych literach to ja do nich dodaje
        letter_list(letter,wrong_letters)
        turns-=1 #jako ze to zla litera to zmniejszam liczbe tur
print_wrong_letter(wrong_letters,root) #wypisuje uzyte bledne litery na ekranie
root.mainloop()

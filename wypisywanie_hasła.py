#Wypisywanie hasła i statystyki

from tkinter import*
import random

okno = Tk()
okno.geometry("600x600")
#przykładowe hasło i odgadnięte litery
haslo = "zielona herbata"
odgadniete = ['e', 'z', 'h'] 

liczba_prob = 10
liczba_wygranych = 0
liczba_przegranych = 0
wyniki = [] #przechowywanie danych z funkcji statystyki, żeby je później zniszczyc i zaktualizowac ich wynik

#funkcja, która wyświetla liczby wygranych i przegranych rund oraz pozostałych prób
def statystyki(wygrane, przegrane, proby): 
    wygrane_rundy = Label(okno, text= 'Wygrane rundy: '+str(wygrane), font=(None,15))
    wyniki.append(wygrane_rundy)
    wygrane_rundy.place(x=450, y=100, anchor='center')

    przegrane_rundy = Label(okno, text= 'Przegrane rundy: '+str(przegrane), font=(None,15))
    wyniki.append(przegrane_rundy)
    przegrane_rundy.place(x=450, y=150, anchor='center')

    pozostale_proby = Label(okno, text= 'Pozostale proby: '+str(liczba_prob), font=(None,15))
    wyniki.append(pozostale_proby)
    pozostale_proby.place(x=450, y=200, anchor='center')

#funkcja, która wypisuje hasło na ekranie
def wypisywanie_hasla(): 
    global haslo
    global odgadniete
    ukryte_haslo = '' #pusty łańcuch znaków, w którym zostaną zapisane litery, spacje i podłogi, a później zostanie wyświetlony na ekranie
    for litera in haslo:
        if litera == ' ':
            ukryte_haslo += ' ' #jeśli w haśle jest spacja to dodawana jest przerwa do łańcucha
        else: #jeśli litera nie jest spacją to zostaje sprawdzone, czy została już odgadnięta
            if litera in odgadniete:
                ukryte_haslo += litera #jeśli została odgadnięta to dodawana jest do łańcucha znaków
            else:
                ukryte_haslo += '_' #jeśli litera nie została odgadnięta to dodawana jest do łańcucha znaków w jej miejscu podłoga
        ukryte_haslo += ' ' #dodanie przerwy między literami, aby podłogi się nie łączyły
    #umieszczanie łańcucha znaków na ekranie
    lancuch_znakow = Label(okno, text=ukryte_haslo, font=(None,20))
    lancuch_znakow.place(x=200, y=200, anchor='center')

#funkcje, które pozwolą sprawdzić, czy wypisana postać hasła zmieni się po dodaniu litery do odgadniętych
def akcja_guzik_A(): 
    odgadniete.append('a')
def akcja_guzik_B(): 
    odgadniete.append('b')

#funkcja dla guzika, który zmienia wartości statystyk
def zmiana_statystyk(): 
    global liczba_wygranych
    global liczba_przegranych
    global liczba_prob
    global wyniki
    liczba_wygranych += random.randint(-1,1)
    liczba_przegranych += random.randint(-1,1)
    liczba_prob -= 1
    for statystyka in wyniki: #niszczenie statystyk wypisanych wczesniej na ekranie, żeby móc je zaktualizować
        statystyka.destroy()
    statystyki(liczba_wygranych, liczba_przegranych, liczba_prob) #wypisywanie od nowa statystyk na ekranie

#dodanie guzika, który dodaje do odgadniętych liter literę A
guzik_A = Button(okno, text='A', command=akcja_guzik_A, font=(None,15)) 
guzik_A.pack()
#dodanie guzika, który dodaje do odgadniętych liter literę B
guzik_B = Button(okno, text='B', command=akcja_guzik_B, font=(None,15)) 
guzik_B.pack()
#dodanie guzika, który aktualizuje statystyki
guzik_zmiany_statystyk = Button(okno, text='Zmiana statystyk', command=zmiana_statystyk, font=(None,15)) 
guzik_zmiany_statystyk.pack()
#dodanie guzika, który wyświetla hasło na ekranie, należy go wcisnąć po wciśnięciu A lub B, aby zobaczyć zmiany w haśle
pokaz_haslo = Button(okno, text='Pokaż hasło', command=wypisywanie_hasla, font=(None,15)) 
pokaz_haslo.pack()
#wyświetlanie statystyk
statystyki(liczba_wygranych, liczba_przegranych, liczba_prob) 

okno.mainloop()

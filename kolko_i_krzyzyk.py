pozycje = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # wszystkie możliwe pozycje, uwzględnione 0, ponieważ od niego zaczyna się indeksowanie
plansza = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
O_X = "O"


def plansza_do_gry():
    print("Twoja plansza do gry w kółko i krzyżyk: ")
    print("\t|", plansza[0], "|", plansza[1], "|", plansza[2], "| \n",
          "\t|", plansza[3], "|", plansza[4], "|", plansza[5], "| \n",
          "\t|", plansza[6], "|", plansza[7], "|", plansza[8], "|")


def pozycja_na_planszy(gracz):
    global pozycje
    print("Teraz ruch należy do gracza ", gracz)
    wybierz_pozycje = int(input("Wybierz cyfrę od 1 do 9 aby wybrać pozycję na planszy: ")) - 1  # indeksowanie od 0
    for i in pozycje:
        if wybierz_pozycje not in pozycje:
            print("Wybrano złą wartość.")
            exit()
    plansza[wybierz_pozycje] = gracz


gra = True


def graj():
    while gra:
        plansza_do_gry()
        pozycja_na_planszy(O_X)
        zamien()
        wygrana()
        #czy_nierozwiazana()

    if gra == False:
        print("Koniec gry. Wygrał gracz, który wykonywał ostatni ruch.")


def zamien():
    global O_X
    if O_X == "O":
        O_X = "X"
    elif O_X == "X":
        O_X = "O"


zwyciezca = None


def wygrana():
    w_kolumnie = czy_w_kolumnie()
    w_wierszu = czy_w_wierszach()
    w_przekatnej = czy_w_przekatnych()

    if w_kolumnie:
        zwyciezca = w_kolumnie
    elif w_wierszu:
        zwyciezca = w_wierszu
    elif w_przekatnej:
        zwyciezca = w_przekatnej


def czy_w_kolumnie():
    global gra
    kol1 = plansza[0] == plansza[3] == plansza[6]  # 0 1 2
    kol2 = plansza[1] == plansza[4] == plansza[7]  # 3 4 5
    kol3 = plansza[2] == plansza[5] == plansza[8]  # 6 7 8
    if kol1 or kol2 or kol3:
        gra = False


def czy_w_wierszach():
    global gra
    wiersz1 = plansza[0] == plansza[1] == plansza[2]
    wiersz2 = plansza[3] == plansza[4] == plansza[5]
    wiersz3 = plansza[6] == plansza[7] == plansza[8]
    if wiersz1 or wiersz2 or wiersz3:
        gra = False


def czy_w_przekatnych():
    global gra
    przekatna1 = plansza[0] == plansza[4] == plansza[8]
    przekatna2 = plansza[2] == plansza[4] == plansza[6]
    if przekatna1 or przekatna2:
        gra = False

"""def czy_nierozwiazana():
    global pozycje
    global gra
    for i in plansza:
        if pozycje not in plansza:
            gra = False # zakończenie gry, ale bez żadnej wygranej; wiem, że to nie zadziała, ale nie wymymyśliłam jak to zrobić
"""

def main():
    graj()


main()

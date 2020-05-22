dzien=int(input("Podaj dzień miesiąca (cyfra/liczba): "))
miesiac=int(input("Podaj miesiąc(Cyfra/liczba): "))
if miesiac==2 and dzien>28:
    print("Błąd, uruchom program ponownie")
    exit()
elif miesiac<=0 or miesiac>12 or dzien<=0 or dzien>31:
    print("Błąd, uruchom program ponownie")
    exit()
elif miesiac in [2,4,6,9,11] and dzien>30:
    print("Błąd, uruchom program ponownie")
    exit()
if miesiac >= 3 and miesiac <= 5:
    print("Wiosna")
elif miesiac >= 6 and miesiac <= 8:
    print("Lato")
elif miesiac >=9 and miesiac <=11:
    print("Jesień")
elif miesiac >=12 or miesiac <=2:
    print("Zima")
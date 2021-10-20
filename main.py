def citire(n, lst):
    """
    citeste o lista de n numere
    :param n:numarul de nr din lista
    :param lst: lista citita
    :return: lista citita
    """
    lst = []
    lst.clear()
    n = input("Dati numarul de numere ce doriti sa fie in lista")
    n = int(n)
    for i in range(0, n):
        lst.append(input("Urmatorul numar din lista este"))
    return lst


def cautare(lst, nr, poz):
    """
    verifica daca un nr se gaseste intr-o lista dupa pozita poz
    :param lst: lista in care cautam
    :param nr: numarul cautat
    :param poz: pozita dupa care incepe cautarea
    :return: DA daca a fost gasit NU in caz contrar
    """
    i = 0
    for i in range(poz, len(lst)):
        if lst[i] == nr:
            return True
    return False


def test_cautare():
    assert cautare([1, 2, 3, 4, 5, 6], 5, 2) is True
    assert cautare([1, 2, 3, 4, 5, 6], 5, 4) is True
    assert cautare([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6) is False


def suma_pare(lst):
    suma = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            suma = suma + lst[i]
    return suma


def test_suma_pare():
    assert suma_pare([1, 2, 3, 4, 5]) == 6
    assert suma_pare([2, 4, 6, 6]) == 18
    assert suma_pare([1, 3, 5, 7]) == 0


def afisare_pare(lst):
    """
    afiseaza toate nr pare din lista o singura data
    :param lst: lista din care se afiseaza
    :return: lista formata doar din nr pare
    """
    listpare = []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0 and cautare(listpare, lst[i], 0) is False:
            listpare.append(lst[i])
    return listpare


def test_afisare_pare():
    assert afisare_pare([1, 2, 3, 4]) == [2, 4]
    assert afisare_pare([2, 4, 2, 6, 4, 6]) == [2, 4, 6]
    assert afisare_pare([1, 3, 5]) == []


def inlocuire_tuplu(lst):
    """
    creeaza lista obținută prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe
    poziții distincte din listă care adunate dau acel număr, dacă se poate.
    :param lst: lista din care dorim sa creeam lista formata din tupluri
    :return: lista creeata
    """
    lsta = []
    lsta.extend(lst)
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            for k in range(j + 1, len(lst)):
                if lst[i] == lst[j] + lst[k] and i != j:
                    lsta[i] = (lst[j], lst[k])
    return lsta


def test_inlocuire_tuplu():
    assert inlocuire_tuplu([1, 2, 3, 4, 7]) == [1, 2, (1, 2), (1, 3), (3, 4)]
    assert inlocuire_tuplu([1, 0]) == [1, 0]
    assert inlocuire_tuplu([1, 0, 1, 2, 2, 4]) == [(0, 1), 0, (0, 1), (0, 2), (0, 2), (2, 2)]


def meniu():
    print('Selectati obtiunea')
    print('1.Cititi o lista')
    print('2.Afișați dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție'
          'citită de la tastatură.')
    print('3.Afisare suma nr pare din lista')
    print('4.Afisarea tuturor numerelor pare din lista')
    print('5.Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe '
          'poziții distincte din listă care adunate dau acel număr, dacă se poate.')
    print('x.Iesire din program')


if __name__ == '__main__':
    test_afisare_pare()
    test_suma_pare()
    test_afisare_pare()
    test_inlocuire_tuplu()
    test_cautare()
    meniu()
    lsta=[]
    isRuning=True
    while isRuning == True:
        obtiune = input('Alegeti obtiunea: ')
        if obtiune == '1':
            n = 0
            lsta = citire(n, lsta)
        elif obtiune =='2':
            nr=int(input('Numarul cautat este : '))
            poz=int(input('Pozitia dupa care se cauta este: '))
            if cautare(lsta, nr,poz) is True:
                print('DA')
            else:
                print('NU')
        elif obtiune =='3':
            print(suma_pare(lsta))
        elif obtiune =='4':
            print(afisare_pare(lsta))
        elif obtiune =='5':
            print(inlocuire_tuplu(lsta))
        elif obtiune =='x':
            isRuning=False
        else:
            print('Obtiune invalida')
        meniu()


def citire  (n,lst):
    """
    citeste o lista de n numere
    :param n:numarul de nr din lista
    :param lst: lista citita
    :return: lista citita
    """
    lst=[]
    lst.clear()
    n=input("Dati numarul de numere ce doriti sa fie in lista")
    n=int(n)
    for i in range (0,n):
        lst.append(int(input("Urmatorul numar din lista este")))
    return lst
def cautare(lst,nr,poz):
    """
    verifica daca un nr se gaseste intr-o lista dupa pozita poz
    :param lst: lista in care cautam
    :param nr: numarul cautat
    :param poz: pozita dupa care incepe cautarea
    :return: DA daca a fost gasit NU in caz contrar
    """
    i=0
    for i in range (poz,lst):
        if lst[i]==nr:
            return True
    return False
def test_cautare():
    assert cautare([1, 2, 3, 4, 5, 6], 5, 2) is True
    assert cautare([1, 2, 3, 4, 5, 6], 5, 4) is True
    assert cautare([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6) is False
if __name__ == '__main__':
    lista=[1,2]
    n=4
    lista=citire(n,lista)
    print(lista)
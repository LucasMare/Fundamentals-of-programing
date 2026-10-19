"""
Program rezolvare probleme lab2

 - 4. Ipoteza Goldbach (orice numar par poate fi scris ca suma de doua numere prime)
 - 7. Calculeaza produsul divizorilor proprii unui n
 - 9. Calculeaza palindromul unui numar n
 - 0. Exit

 - implementare produs divizori proprii n
 - implementare calcul palindrom 
 - implementare meniu

 - implementarea unui ciur al lui Eratostene
 - implementarea verificarii ipotezei lui Goldbach pentru un numar n
"""


def prodDivProp (x):
    """
    Functie care returneaza produsul divizoriilor proprii ai unui numar, -1 in cazul in care numarul nu are divizori proprii
    :params: an integer
    :return: an integer
    :raises:
    """ 
    x = int(x)
    rez = 1
    for i in range (2,x):
        if x%i==0: rez=rez*i
    if rez==1: return -1
    return rez

def palindrom (x):
    """
    Functie care returneaza palindromul unui numar. In cazul in care ultima cifra este 0, returneaza -1
    :params: an integer
    :returns: an integer
    :raises:
    """
    x = int (x)
    if x%10==0: return -1
    return int(str(x)[::-1])

def ciurE (n):
    """
        Functie care returneaza un dictionar cu cheile de la 2 pana la un numar dat n si valoare True daca e prim, False daca nu e prim (ciurul lui Eratostene)
        :params: an integer
        :returns: a dictionary
        :raises:
        """
    ciur = {}
    n = int(n)
    for i in range (0,n+1): 
        ciur[i]=True
    ciur[0] = False
    if n>0: ciur[1] = False

    for i in range (2,n+1):
        for j in range (2*i,n+1,i):
            ciur[j]=False

    return ciur

def isSum2Primes (n):
    """
        Functie care primeste un numar natural n si returneaza:
            - o lista cu 2 numere prime, care insumeaza numarul n
            - None, daca nu exista astfel de numere
        :params: an integer
        :returns: pair/none
        :raises:
        """
    ciur = ciurE(n)
    n = int(n)
    for key, value in ciur.items():
        if value == False: continue
        x = int(key)
        if ciur[n-x] == True: return [x, n-x]

    return None
        
        

    
def end_program ():
    print ("Numa bile")
    exit()

def menu():
    
    while True:
        print ("""
        Program rezolvare probleme lab2

        - 4. Verifica ipoteza Goldbach (orice numar par poate fi scris ca suma de doua numere prime)
        - 7. Calculeaza produsul divizorilor proprii unui n
        - 9. Calculeaza palindromul unui numar n
        - 0. Exit
        """)

        choice = input("Introduceti cerinta: ")
        try: 
            choice = int (choice)
        except: 
            None

        match choice:
            case 4: 
                n = input ("Introduceti un numar:  ")
                rez=isSum2Primes(n)
                if rez == None: print("Acest numar nu poate fi scris ca o suma de 2 numere prime")
                else: print(f"{n}={rez[0]}+{rez[1]}")
            case 7:  
                n = input ("Introduceti un numar:  ")
                match prodDivProp(n):
                    case -1: print ("Numarul nu are divizori proprii")
                    case _: print (f"Produsul divizorilor proprii ai numarului este {prodDivProp(n)}")
            
            case 9: 
                n = input ("Introduceti un numar:  ")
                match palindrom(n):
                    case -1: print ("Numarul nu are palindrom de aceeasi lungime")
                    case _: print (f"Palindromul numarului este {palindrom(n)}")
            
            case 0: end_program()

            case _: print("Alegere invalida")


def testProdDivProp ():
    assert prodDivProp(0) == -1
    assert prodDivProp(1) == -1
    assert prodDivProp(2) == -1
    assert prodDivProp(6) == 6
    assert prodDivProp(12) == 144

def testPalindrom ():
    assert palindrom(3) == 3
    assert palindrom(10) == -1
    assert palindrom(13874) == 47831

def testCiurE ():
    assert ciurE(10) == {0:False, 1:False, 2:True, 3:True, 4:False, 5:True, 6:False, 7:True, 8:False, 9:False, 10:False}
    assert ciurE(2) == {0:False, 1:False, 2:True}
    assert ciurE(0) == {0:False}

def testIsSum2Primes ():
    assert isSum2Primes(4) == [2,2]
    assert isSum2Primes(10) == [3,7]
    assert isSum2Primes(19) == [2,17]
    assert isSum2Primes(3) == None

testProdDivProp()
testPalindrom()
testCiurE()
testIsSum2Primes()

menu()


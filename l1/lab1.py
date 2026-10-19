## calculam suma a n numere
def sum_n_num():
    n = int(input("Introduceti un numar: "))
    print(f"Introduceti {n} numere pe linii diferite:")
    suma=0
    for iterator in range (n):
        suma=suma+int(input())
    print(f"Suma lor este {suma}")

def is_prime():
    x = int(input("Introduceti un numar: "))
    if x<2 or (x>2 and x%2==0):
        print("El nu este prim")
        return
    for i in range(2,x,2):
        if x%i==0: 
            print("El nu este prim")
            return
    print("El este prim")

def cmmdc():
    x = int(input("Introduceti 2 numere pe linii diferite:"))
    y = int(input())
    while y>0:
        r=x%y
        x=y
        y=r
    print(f"Cel mai mare divizor comun al lor este {x}")
    

nr_cerinta = int(input("Alege o cerinta(1,2,3): "))
match nr_cerinta:
    case 1: sum_n_num()
    case 2: is_prime()
    case 3: cmmdc()
"""
Aplicatie consola care citeste o lista si gaseste secventa cu lungime maxima (sau toate daca sunt mai multe) care:
    14. Oricare doua elemente consecutive au cel putin 2 cifre distincte comune

- realizarea unei functii care verifica daca doua numere au cel putin 2 cifre distincte comune
- realizarea unei functii care gaseste secventele de lungime maxima cu proprietatea ceruta
- realizarea unei functii meniu care se ocupa de consola
"""

def twoCif (x, y):
    """
    Checks if two numbers contain at least two different common numbers
    :params: two integers
    :returns: True or False
    :raises:
    """
    try: y=int(y)
    except: return False
    x = str(x)
    y = str(y)
    comun = {}
    for cif in x:
        if cif in y: comun[cif] = True
    if len(comun) >= 2: return True
    return False

def maxSequenceTwoCif(nr_list):
    """
        Finds the longest sequence of a list in which all consecutive numbers have at least two distinct digits in common. If there are multiple such sequences, it returns them all
        :params: a list
        :returns: a list, where the first element is the starting index of the sequence and the next element is a list of the numbers in the sequence
        :raises:
    """
    numbers_list = nr_list.copy()
    numbers_list.append('a') # appends an element to a copy of the list that always ends the current sequence
    
    indexes_list = []
    sequences_list = []
    current_sequence_start_index = 0
    length_of_longest_sequence = 1
    n = len(numbers_list)
    for current_index in range (1,n):
        
        length_current_sequence = current_index - current_sequence_start_index
        if twoCif(numbers_list[current_index-1],numbers_list[current_index]):
            continue
        if length_current_sequence > length_of_longest_sequence: 
            indexes_list.clear()
            length_of_longest_sequence = length_current_sequence
            indexes_list.append(current_sequence_start_index)
        elif length_current_sequence == length_of_longest_sequence:
            indexes_list.append(current_sequence_start_index)
        current_sequence_start_index = current_index
    for el in indexes_list:
        sequences_list.append(el)
        sequences_list.append(nr_list[el:el+length_of_longest_sequence])
    return sequences_list

def parseNumbers (c):
    """
    Parses numbers entered on the same line into a list of those numbers
    :params: a string
    :returns: a list
    :raises:
    """
    rez = []
    c = c.strip().split(" ")
    for el in c:
        rez.append(int(el))
    return rez

def testTwoCif ():
    assert twoCif(10, 1000) == True
    assert twoCif(1, 22) == False
    assert twoCif(283754, 982983754) == True

def testMaxSequenceTwoCif():
    assert maxSequenceTwoCif([13, 31, 23, 133, 65]) == [0, [13, 31]]
    assert maxSequenceTwoCif([13, 31, 23, 133, 65, 56]) == [0, [13, 31], 4, [65, 56]]
    assert maxSequenceTwoCif([13, 31, 23, 63564, 65, 56]) == [3, [63564, 65, 56]]
    assert maxSequenceTwoCif([12, 34, 56]) == [0, [12], 1, [34], 2, [56]] 

def end_program ():
    print ("Numa bile")
    exit()

def menu():
    
    while True:
        print ("""
        Aplicatie consola care citeste o lista si gaseste secventa cu lungime maxima (sau toate daca sunt mai multe) care:
            14. Oricare doua elemente consecutive au cel putin 2 cifre distincte comune 
            0. exit
        """)

        choice = input("Introduceti cerinta: ")
        try: 
            choice = int (choice)
        except: 
            None

        c = input("Introduceti o lista de numere: ")
        nr_l = parseNumbers(c)


        match choice:
            case 14: 
                rez = maxSequenceTwoCif(nr_l)
                if (len(rez)==2): 
                    print ("Cea mai lunga secventa valida este: ", rez[1])
                else:
                    print ("Secventele valide cu lungime maxima sunt:\n ")
                    for i in range (1,len(rez),2):
                        print (rez[i],'\n') 
            
            case 0: end_program()

            case _: print("Alegere invalida")



testTwoCif()
testMaxSequenceTwoCif()

menu()
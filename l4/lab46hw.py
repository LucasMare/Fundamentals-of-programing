"""
An app that helps clients of tourism agency manage tourism packages
A tourism package consists of start date and end date, destination and price
This app supports:
    1. Adding
        - adding travel package
        - modifying travel package
    2. Deleting
        - deleting all travel packages for a given destination
        - deleting all travel packages shorter than a given number of days
        - deleting all travel packages more expensive than a given sum
    3. Search
        - print all travel packages within a certain time interval 
        - print all travel packages cheaper than a given sum
        - print all travel packages ending on a certain date 
    4. Reports
        - printing all travel packages with a certain destination
        - printing all travel packages available within a certain time frame in ascending price order
        - printing average price price for a given destination
    5. Flirtation 
        - Elimination of travel packages more expensive than a given price and a different destination from the inputted one
        - Elimination of travel packages that include certain days of a month (a number from 1 to 12)
    6. Undo 
        - Undoing the last action (the travel package list goes back to the last version.)

    
First iteration:

    - adding support for storing, adding, modifying travel packages list
        - function for creating new travel packages list
        - function for adding packages to the list
        - function for modifying packages in the list
        - additional methods needed for the implementation
    - adding support for undoing previous operations
        - figuring out a way of storing history of operations
        - implementing an undo function
    
"""

def outputTextForMenu ():
    print ("""
    An app that helps clients of tourism agency manage tourism packages
    A tourism package consists of start date and end date, destination and price
    This app supports:
        1. Adding
            - adding travel package
            - modifying travel package
        2. Deleting
            - deleting all travel packages for a given destination
            - deleting all travel packages shorter than a given number of days
            - deleting all travel packages more expensive than a given sum
        3. Search
            - print all travel packages within a certain time interval 
            - print all travel packages cheaper than a given sum
            - print all travel packages ending on a certain date 
        4. Reports
            - printing all travel packages with a certain destination
            - printing all travel packages available within a certain time frame in ascending price order
            - printing average price price for a given destination
        5. Flirtation 
            - Elimination of travel packages more expensive than a given price and a different destination from the inputted one
            - Elimination of travel packages that include certain days of a month (a number from 1 to 12)
        6. Undo 
            - Undoing the last action (the travel package list goes back to the last version.)
        0. Exit Program
    """)

def intersection(l1,l2):
    """
    Function that outputs the intersection of two lists
    :params: two lists
    :returns: a list
    """
    intersec = []
    for el in l1:
        if el in l2: intersec.append(el)
    return intersec

def testIntersection():
    assert intersection([1,2,3],["a",2,{}]) == [2]

def isLeapYear(x):
    """
    Checks if a year is a leap year
    :Params: an integer
    :Returns: True if a year is a leap year, False if it is not a valid year or a leap year
    :Raises:
    """
    if x % 4 == 0:
        if x % 100 == 0: 
            if x % 400 == 0: return True
            return False
        return True
    return False

def testIsLeapYear():
    assert isLeapYear(2016) == True
    assert isLeapYear(1900) == False
    assert isLeapYear(1600) == True
    assert isLeapYear(1955) == False

def isValidDate(day, month, year):
    """
    Checks if a date is valid
    :params: 3 integers representing the day, month, year
    :returns: True or False
    :Raises:
    """
    days_per_month = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31
    }
    if isLeapYear(year): days_per_month["2"] = 29
    if month > 12 or month < 0: return False
    if 0 > day or day > days_per_month[str(month)]: return False
    return True 

def testIsValidDate():
    assert isValidDate(31,8,2026) == True
    assert isValidDate(29,2,2000) == True
    assert isValidDate(50,15,9999) == False
    assert isValidDate(29,2,1900) == False

def checkDateFormat(date_string):
    """
    Checks if a string is a valid date with the format dd/mm/yyyy
    :params: a string
    :returns: True or False
    :raises:
    """
    split_date = date_string.split("/")
    if len(split_date) != 3: return False
    
    try: day = int(split_date[0])
    except: return False
    
    try: month = int(split_date[1])
    except: return False
    
    try: year = int(split_date[2])
    except: return False

    return isValidDate(day, month, year)

def testCheckDateFormat():
    assert checkDateFormat("19/04/1954") == True
    assert checkDateFormat("akshdf") == False
    assert checkDateFormat("19.7.2026") == False
    assert checkDateFormat("99/18/8375") == False

def parseDate(c):
    """
    Function that gets a string that represents a valid date with the format dd/mm/yyyy and outputs a dictionary with the keys "day", "month", "year" and their respective values 
    :params: a string
    :returns: a dictionary
    :raises:
    """
    date = {}
    c = c.split('/')
    date["day"] = int(c[0])
    date["month"] = int(c[1])
    date["year"] = int(c[2])
    return date

def testParseDate():
    assert parseDate("10/9/2008") == {
        "day": 10,
        "month": 9,
        "year": 2008 
    }

def inputDate():
    """
    Function that gets as input from user a string that represents a date, checks if it is valid and than returns a dictionary with the keys "day", "month", "year" and their respective values
    :params: None
    :returns: a dictionary
    :raises:
    """
    c = input()
    while checkDateFormat(c) == False:
        c = input("Invalid date, please enter a valid date with the format dd/mm/yyyy: ")
    date = parseDate(c)
    return date

def checkIfStringFloat (num_string:str):
    """
    Function that checks whether a string can be converted to a float, and returns True or False accordingly
    :params: a string
    :returns: True or False
    :raises:
    """
    try: 
        fl = float(num_string)
        return True
    except: 
        return False

def testCheckIfStringIsFloat():
    assert checkIfStringFloat("19.20") == True
    assert checkIfStringFloat("1920") == True
    assert checkIfStringFloat("plsajf") == False

def inputPrice():
    """
    Function that deals with inputing a valid price (a number).
    :params: None
    :returns: a float with two decimals
    :raises:
    """
    p = input()
    while checkIfStringFloat(p) == False:
        p = input ("Invalid price value! Enter another one: ")
    return round(float(p), 2)

def inputDestination():
    """
    Function that inputs a string representing a destination and returns it
    """
    c = input()
    return c

def inputTravelPackage():
    """
    Function that deals with inputing a travel package
    :params: None
    :returns: 
    :raises:
    """
    package = createTravelPackage()
    print("Input the start date of the travel (dd/mm/yyyy): ")
    package["start_date"] = inputDate()
    print("Input the end date of the travel (dd/mm/yyyy): ")
    package["end_date"] = inputDate()
    print("Input a destination: ")
    package["destination"] = inputDestination()
    print("Input the price of the travel: ")
    package["price"] = inputPrice()
    return package

def createTravelPackage():
    """
    Creates an dictionary with the following keys: "start_date" = None, "end_date" = None, "destination" = "", "price" = 0
    :params: None
    :returns: a dictionary
    :raises: 
    """
    package = {
        "start_date": None,
        "end_date": None,
        "destination": "",
        "price": 0
    }
    return package

def testCreateTravelPackage():
    assert createTravelPackage() == {
        "start_date": None,
        "end_date": None,
        "destination": "",
        "price": 0
    }

def createTravelPackagesDataStructure():
    """
    Function that creates a dictionary with two keys: "list", with the value an empty list, and "hist", also an empty list
    :params: None
    :returns:
    :raises:
    """
    travel_packages = {
        "list": [],
        "hist": [] 
    }
    return travel_packages

def testCreateTravelPackagesDataStructure():
        assert createTravelPackagesDataStructure () == {
            "list": [],
            "hist": []
        }

def getTravelPackagesList(travel_packages):
    """
    Function that returns the list of travel packages 
    :params: a dictionary
    :returns: a list
    """
    return travel_packages["list"]

def testGetTravelPackagesList():
    assert getTravelPackagesList({"list": [], "hist": []}) == []
    assert getTravelPackagesList({"list": [1,2,33], "hist": []}) == [1,2,33]

def getPrice(travel_package):
    """
    Function that returns the price of a given travel package
    :params: a dictionary representing a travel package
    :returns: a float representing the price
    :raises:
    """
    return travel_package["price"]

def testGetPrice():
    package = createTravelPackage()
    package["price"] = 174.76
    assert getPrice(package) == 174.76

def getDestination(travel_package):
    """
        Function that returns the destination of a given travel package
        :params: a dictionary representing a travel package
        :returns: a string representing the destination
        :raises:
    """
    return travel_package["destination"]

def testGetDestination():
    package = createTravelPackage()
    package["destination"] = "Paris"
    assert getDestination(package) == "Paris"

def appendCurrentListToHist(travel_package_structure):
    """
    Function that appends current travel packages list to history
    :params: a dictionary, corresponding to a travel_package_structure
    :returns:
    :raises:
    """
    travel_package_structure["hist"].append(travel_package_structure["list"].copy())

def testAppendCurrentListToHist():
    travel_packages_structure = createTravelPackagesDataStructure()
    travel_packages_structure["list"] = [1,2,3]
    appendCurrentListToHist(travel_packages_structure)
    assert travel_packages_structure["hist"] == [[1,2,3]]

def addPackageToList(travel_package_list, travel_package):
    """
    Function that appends a travel package to a list
    :params: a dictionary corresponding to a travel_package_structure, a dictionary corresponding to a travel package
    :returns: 
    :raises:
    """
    travel_package_list.append(travel_package)

def testAddPackageToList():
    travel_packages_structure = createTravelPackagesDataStructure()
    addPackageToList (getTravelPackagesList(travel_packages_structure), {})
    assert travel_packages_structure["list"] == [{}]

def filterByPrice(list, price, lowerOrHigher):
    """
    Function that gets a list of travel packages, a float that represents the price and boolean value, than returns a list with all packages more expensive than the price if the boolean is true, or less expensive if the boolean is false
    :params: a list, a float, a boolean
    :returns: a list
    :raises:
    """
    updated_list = []
    for package in list:
        package_price = getPrice(package)
        if (package_price >= price) == lowerOrHigher: addPackageToList(updated_list, package)
    return updated_list

def testFilterByPrice():
    structure = createTravelPackagesDataStructure()
    for i in range(0,4):
        package = createTravelPackage()
        package["price"] = i
        addPackageToList(getTravelPackagesList(structure), package)
    assert filterByPrice (getTravelPackagesList(structure), 2, True) == [{"start_date": None, "end_date": None, "destination": "", "price": 2},{ "start_date": None, "end_date": None, "destination": "", "price": 3}]
    assert filterByPrice (getTravelPackagesList(structure), 2, False) == [{"start_date": None, "end_date": None, "destination": "", "price": 0},{ "start_date": None, "end_date": None, "destination": "", "price": 1}]

def destinationComparator(d1, d2):
    """
    Function that gets two strings representing two destinations and returns True if they are the same (case-insensitive), and False if they are different
    :params: two strings
    :returns: True or False
    :raises:
    """
    return d1.lower() == d2.lower()

def testDestinationComparator():
    assert destinationComparator("paris", "Paris") == True
    assert destinationComparator("paris", "Pari") == False
    assert destinationComparator("paris", "1") == False

def filterByDestination(list, destination, sameOrDifferent):
    """
    Function that gets a list of travel packages, a string that represents a destination and a boolean value, than returns a list of all packages that have the same destination as the one given, if the boolean is true, or a list of all packages with a different destination to the one given, if the boolean value is false
    :params: a list, a string, a boolean
    :returns: a list
    :raises:
    """
    updated_list = []
    for package in list:
        package_destination = getDestination(package)
        if (destinationComparator(package_destination,destination)) == sameOrDifferent: addPackageToList(updated_list, package)
    return updated_list

def testFilterByDestination():
    structure = createTravelPackagesDataStructure()
    places = ["Paris", "France", "baia Mare", "Sasar"]
    for i in range(0,4):
        package = createTravelPackage()
        package["destination"] = places[i]
        addPackageToList(getTravelPackagesList(structure), package)
    assert filterByDestination (getTravelPackagesList(structure), "Paris", True) == [{"start_date": None, "end_date": None, "destination": "Paris", "price": 0}]
    assert filterByDestination (getTravelPackagesList(structure), "Baia Mare", False) == [{"start_date": None, "end_date": None, "destination": "Paris", "price": 0},{ "start_date": None, "end_date": None, "destination": "France", "price": 0},{ "start_date": None, "end_date": None, "destination": "Sasar", "price": 0}]

def endProgram():
    print ("See you later aligator!")
    exit()

def menu():
    """
    Function that deals with the main menu of the app
    """
    travel_packages_structure = createTravelPackagesDataStructure()
    while True:
        outputTextForMenu()
        choice = input ("Input a command: ")
        match choice:
            case "1": addMenu(travel_packages_structure)
            case "5": filtrationMenu(travel_packages_structure)
            case "0": endProgram()
            case _: print ("Invalid command!")

def addMenu(travel_packages_structure):
    """
    Function that deals with the "Adding" submenu of the app
    :params: a travel package structure
    :returns:
    :raises:
    """
    while True:    
        print ("""
        Add menu:
            1. Add a travel package to the list
            2. Modify a travel package from the list 
            0. Go back
        """)
        choice = input ("Input a command: ")
        match choice:
            case "0": return None
            case "1": 
                new_package = inputTravelPackage()
                addPackageToList(getTravelPackagesList(travel_packages_structure), new_package)
                appendCurrentListToHist(travel_packages_structure)
                print (f"Current list of travel packages is:\n {travel_packages_structure["list"]}")
            case _: print ("Invalid command!")

def filtrationMenu(travel_packages_structure):
    while True:
        print ("""
        Filter menu:
            1. Show all entries with a higher price and a different destination from the ones inputed by the user
            2. Show all entries not whithin a month entered by the user
            0. Go back
        """)
        choice = input ("Input a command: ")
        match choice:
            case "1": 
                print ("Enter a price: ")
                price = inputPrice()
                print ("Enter a destination: ")
                destination = inputDestination()
                filtered_by_price = filterByPrice(getTravelPackagesList(travel_packages_structure),price,True)
                filtered_by_destination = filterByDestination(getTravelPackagesList(travel_packages_structure),destination,False)
                filtered_list = intersection(filtered_by_price, filtered_by_destination)
                print(f"Here is the filtered list:\n {filtered_list}")
            

def testFunction ():
    testIntersection()
    testIsLeapYear()
    testIsValidDate()
    testCheckDateFormat()
    testParseDate()
    testCreateTravelPackage()
    testCreateTravelPackagesDataStructure()
    testGetTravelPackagesList()
    testCheckIfStringIsFloat()
    testAppendCurrentListToHist()
    testAddPackageToList()
    testGetPrice()
    testGetDestination()
    testFilterByPrice()
    testGetDestination()
    testFilterByDestination()


testFunction()
menu()




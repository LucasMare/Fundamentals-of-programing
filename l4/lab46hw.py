from domain import createTravelPackage, modifyStartDate, modifyEndDate, modifyDestination, modifyPrice
from service import addPackageToList, filterByPrice, filterByDestination, intersection, parseDate, parsePrice, filterByMonth, createTravelPackagesDataStructure, undo, appendCurrentListToHist, getTravelPackagesList, getStartDate, getEndDate, getDestination, getPrice, modifyPackageFromList, sortByKey, filterByDate, averagePrice
from tests import testFunction


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

    - adding support for storing and adding travel packages list
        - function for creating new travel packages list
        - function for adding packages to the list
        - function for modifying packages in the list
        - additional methods needed for the implementation
    - adding support for undoing previous operations
        - figuring out a way of storing history of operations
        - implementing an undo function
    - adding support for certain filters
        - elimination of travel packages more expensive than a given price and a different destination from the inputed one

Second iteration:
    - refactoring error handling when inputing invalid data for the price and dates of a travel package
    - refactoring date parsing into one method instead of two
    - modularising the code
    - making all methods adhere to the single responsability rule
    - implementing the abilty to modify a travel package
    - implementing further filter options
    - implementing search features
    - rewriting some flawed tests

Third iteration: 
    - moving the travel packages structure logic to service module
    - moving parsePrice to ui module

    
"""

def outputTextForMainMenu ():
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
        5. Filtration 
            - Elimination of travel packages more expensive than a given price and a different destination from the inputed one
            - Elimination of travel packages that include certain days of a month (a number from 1 to 12)
        6. Undo 
            - Undoing the last action (the travel package list goes back to the last version.)
        0. Exit Program
    """)

def outputTextForAddMenu():
    print ("""
    Add menu:
        1. Add a travel package to the list
        2. Modify a travel package from the list 
        0. Go back
    """)

def outputTextForReportMenu():
    print("""
    Report menu:
        1. Give number of travel packages for a given destination
        2. Give all packages available within a certain time period in ascending price order
        3. Give the average price for a given destination
    """)

def outputTextForFilterMenu():
    print ("""
    Filter menu:
        1. Show all entries with a higher price and a different destination from the ones inputed by the user
        2. Show all entries not whithin a month entered by the user
        0. Go back
    """)

def inputDate():
    """
    Function that gets as input from user a string that represents a date, checks if it is valid and than returns a dictionary with the keys "day", "month", "year" and their respective values
    :params: None
    :returns: a dictionary
    :raises: 
    """
    date = False
    while date == False:
        try:
            date = parseDate(input())
        except Exception as error:
                print (error)
    return date

def inputPrice():
    """
    Function that deals with inputing a valid price (a number).
    :params: None
    :returns: a float with two decimals
    :raises:
    """
    price = False
    while price == False:
        try:
            price = parsePrice(input())
        except Exception as error:
            print (error)
    return price

def inputNum(range_low, range_high):
    """
    Function that deals with inputing a number within a certain range.
    :params: None
    :returns: an int
    :raises:
    """
    num = input()
    try:
        num = int(num)
    except:
        raise ValueError("Please enter a number!")
    try:
        assert range_low<=num and num<=range_high
    except:
        raise ValueError("Inavlid number!")
    return num

def inputDestination():
    """
    Function that inputs a string representing a destination and returns it
    """
    return input()

def inputTravelPackage():
    """
    Function that deals with inputing a travel package
    :params: None
    :returns: 
    :raises:
    """
    
    package = createTravelPackage()
    print("Input the start date of the travel (dd/mm/yyyy): ")
    modifyStartDate(package,inputDate())
    
    print("Input the end date of the travel (dd/mm/yyyy): ")
    modifyEndDate(package, inputDate())

    print("Input a destination: ")
    modifyDestination(package, inputDestination())
    
    print("Input the price of the travel: ")
    modifyPrice(package,inputPrice())
    
    return package

def printPackage(travel_package):
    """
    Function that deals with printing a travel package
    """
    print (f"Period: {getStartDate(travel_package)["day"]}/{getStartDate(travel_package)["month"]}/{getStartDate(travel_package)["year"]} - {getEndDate(travel_package)["day"]}/{getEndDate(travel_package)["month"]}/{getEndDate(travel_package)["year"]}")
    print (f"Destination: {getDestination(travel_package)}")
    print (f"Price: {getPrice(travel_package)}")

def printPackageList(travel_package_list):
    """
    Function that deals with printing a travel package list
    """
    for i in range(0,len(travel_package_list)):
        print(f"{i+1}.")
        printPackage(travel_package_list[i])
        print('\n')

def endProgram():
    print ("See you later aligator!")
    exit()

def menu():
    """
    Function that deals with the main menu of the app
    """ 
    travel_packages_structure = createTravelPackagesDataStructure()
    while True:
        outputTextForMainMenu()
        choice = input ("Input a command: ")
        match choice:
            case "1": addMenu(travel_packages_structure)
            case "4": reportMenu(travel_packages_structure)
            case "5": filtrationMenu(travel_packages_structure)
            case "6": 
                try: 
                    undo(travel_packages_structure)
                    print("Undo successful!")
                except Exception as error:
                    print (error)
            case "7": 
                print("Current list is: \n")
                printPackageList(getTravelPackagesList(travel_packages_structure))
            case "0": endProgram()
            case _: print ("Invalid command!")

def addMenu(travel_packages_structure):
    """
    Function that deals with the "Adding" submenu of the app
    :params: a travel package structure
    :returns:
    :raises:
    """
    outputTextForAddMenu()
    while True:    
        choice = input ("Input a command: ")
        match choice:
            case "0": return None
            case "1": 
                new_package = inputTravelPackage()
                appendCurrentListToHist(travel_packages_structure)
                addPackageToList(getTravelPackagesList(travel_packages_structure), new_package)
                print("Current list of travel packages is: \n")
                printPackageList(getTravelPackagesList(travel_packages_structure))
            case "2":
                appendCurrentListToHist(travel_packages_structure)
                printPackageList(getTravelPackagesList(travel_packages_structure))
                print("Enter which package you want to modify: ")
                package_choice = False
                while package_choice == False:
                    try: 
                        package_choice = inputNum(1,len(getTravelPackagesList(travel_packages_structure)))
                        package_choice = package_choice - 1
                    except Exception as error:
                        print(error)
                print("Enter a new package to modify the old one: ") 
                modifyPackageFromList(getTravelPackagesList(travel_packages_structure), inputTravelPackage(), package_choice)
                print("Sucessfully modified travel package")
            case _: print ("Invalid command!")

def deleteMenu():
    while True:
        choice = input ("Input a command: ")
        

def reportMenu(travel_packages_structure):
    outputTextForReportMenu()
    while True: 
        choice = input("Input a command: ")
        match choice:
            case "0": return None
            case "1": 
                print("Input a destination: ") 
                destination = inputDestination()
                print(f"Number of travel packages with the given destination is: {len(filterByDestination(getTravelPackagesList(travel_packages_structure), destination, True))}")
            case "2":
                print ("Please input the start date of the interval: ")
                start_date = inputDate()
                print ("Please input the end date of the interval: ")
                end_date = inputDate()
                print("The list of all packages in this time frame in ascending price order is: \n")
                printPackageList(sortByKey(filterByDate(getTravelPackagesList(travel_packages_structure), start_date, end_date, True), getPrice))
            case "3":
                print ("Enter a destination: ")
                destination = inputDestination()
                print(f"The average price for {destination} is {averagePrice(filterByDestination(getTravelPackagesList(travel_packages_structure), destination, True))}")

def filtrationMenu(travel_packages_structure):
    outputTextForFilterMenu()
    while True:
        choice = input ("Input a command: ")
        match choice:
            case "0": return None
            case "1": 
                print ("Enter a price: ")
                price = inputPrice()
                print ("Enter a destination: ")
                destination = inputDestination()
                filtered_by_price = filterByPrice(getTravelPackagesList(travel_packages_structure),price,True)
                filtered_by_destination = filterByDestination(getTravelPackagesList(travel_packages_structure),destination,False)
                filtered_list = intersection(filtered_by_price, filtered_by_destination)
                print(f"Here is the filtered list:\n {filtered_list}")
            case "2":
                print("Enter a valid month number (1-12): ")
                month = False
                while month == False:
                    try:
                        month = inputNum(1,12)
                    except Exception as error:
                        print(error)
                print ("This is the filtered list:\n")
                printPackageList(filterByMonth(getTravelPackagesList(travel_packages_structure), month))
            

if __name__ == '__main__':
    testFunction()
    menu()




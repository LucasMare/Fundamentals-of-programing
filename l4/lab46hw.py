from domain import createTravelPackage, createTravelPackagesDataStructure, appendCurrentListToHist, getTravelPackagesList, modifyStartDate, modifyEndDate, modifyDestination, modifyPrice
from service import addPackageToList, filterByPrice, filterByDestination, intersection, parseDate, parsePrice
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

    - adding support for storing, adding, modifying travel packages list
        - function for creating new travel packages list
        - function for adding packages to the list
        - function for modifying packages in the list
        - additional methods needed for the implementation
    - adding support for undoing previous operations
        - figuring out a way of storing history of operations
        - implementing an undo function

Second iteration:
    - refactoring error handling when inputing invalid data for the price and dates of a travel package
    - refactoring date parsing into one method instead of two
    - modularising the code
    - making all methods adhere to the single responsability rule
    - implementing the abilty to modify a travel package
    - implementing further filter options
    - implementing search features 
    - rewriting some flawed tests
    
    
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
        5. Filtration 
            - Elimination of travel packages more expensive than a given price and a different destination from the inputted one
            - Elimination of travel packages that include certain days of a month (a number from 1 to 12)
        6. Undo 
            - Undoing the last action (the travel package list goes back to the last version.)
        0. Exit Program
    """)



def inputDate():
    """
    Function that gets as input from user a string that represents a date, checks if it is valid and than returns a dictionary with the keys "day", "month", "year" and their respective values
    :params: None
    :returns: a dictionary
    :raises: 
    """
    date = True
    while date:
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
    price = True
    while price:
        try:
            price = parsePrice(input())
        except Exception as error:
            print (error)
    return price

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
                print (f"Current list of travel packages is:\n {getTravelPackagesList(travel_packages_structure)}")
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
            

if __name__ == '__main__':
    testFunction()
    menu()




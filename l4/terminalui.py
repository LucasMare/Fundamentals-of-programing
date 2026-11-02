"""
Rough draft of a command line like ui
"""
from service import parseCommand, createTravelPackagesDataStructure, parsePrice, parseDate, appendCurrentListToHist, addPackageToList, getTravelPackagesList, undo
from validation import isValidCommand, isValidAddArg, isValidNewArgs
from domain import createTravelPackage, modifyStartDate, modifyEndDate, modifyPrice, modifyDestination, getStartDate, getEndDate, getDestination, getPrice
from tests import testFunction

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

def parseCommand(command_string):
    """
    Function that parses a command into strings 
    """
    return command_string.strip().split()

def main():
    travel_package_structure = createTravelPackagesDataStructure()
    while True:
        try: 
            command = input()
            command = parseCommand(command)
            isValidCommand(command[0])
            match command[0]:
                case "add": addCommand(travel_package_structure, command[1:])
                case "ls": printPackageList(getTravelPackagesList(travel_package_structure))
                case "undo": undo(travel_package_structure)
        except Exception as error:
            print(error)

def addCommand(travel_packages_structure, args:list):
    try:
        isValidAddArg(args[0])
        match args[0]:
            case "--new" | "-n":
                appendCurrentListToHist(travel_packages_structure)
                new_package = createTravelPackage()
                isValidNewArgs(args[1:])
                modifyStartDate(new_package, parseDate(args[1]))
                modifyEndDate(new_package, parseDate(args[2]))
                modifyDestination(new_package, args[3])
                modifyPrice(new_package, parsePrice(args[4]))
                addPackageToList(getTravelPackagesList(travel_packages_structure), new_package)
                print("Successfuly added package to list!")
            case "--help" | "-h": 
                print(
                """
                --new: add new package to list. Requires 4 arguments: two dates, a destination and a price
                """
                )
    except Exception as error:
        print(error)

if __name__ == "__main__":
    testFunction()
    main()


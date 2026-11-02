from domain import getPrice, getDestination, getStartDate, getEndDate, createTravelPackage, modifyDestination, modifyPrice, modifyStartDate, modifyEndDate

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

def getTravelPackagesList(travel_package_structure):
    """
    Function that returns the list of travel packages 
    :params: a dictionary
    :returns: a list
    """
    return travel_package_structure["list"]

def getTravelPackagesHist(travel_package_structure):
    """
    Function that returns the history of the travel packages state
    :params: a dictionary
    :returns: a list
    """
    return travel_package_structure["hist"]

def modifyPackagesList(travel_package_structure, new_list:list):
    """
    Function that modifies the list of a travel package structure. It sets the list to a deepcopy of the list given as param
    :params: a travel package structure, a list
    :returns:
    :raises:
    """
    new_list_copy = []
    for package in new_list:
        new_package = createTravelPackage()
        modifyDestination(new_package, getDestination(package))
        modifyPrice(new_package, getPrice(package))

        if getStartDate(package) == None: modifyStartDate(new_package, None)
        else: modifyStartDate(new_package, getStartDate(package).copy())

        if getEndDate(package) == None: modifyEndDate(new_package, None)
        else: modifyEndDate(new_package, getEndDate(package).copy())

        new_list_copy.append(new_package)
    travel_package_structure["list"] = new_list_copy

def getPackageFromList(travel_package_list, index):
    """
    Function that returns the element with a certain index from a travel package list
    :params: a travel packages list, an index
    :returns: a travel package
    :raises:
    """
    return travel_package_list[index]

def modifyPackageFromList(travel_package_list, new_travel_package, index_to_modify):
    """
    Function that modifies a package with a given index from a given travel package list
    :params: travel package list, travel_package, index to be modified
    :returns:
    :raises:
    """
    travel_package_list[index_to_modify] = new_travel_package

def appendCurrentListToHist(travel_package_structure):
    """
    Function that appends current travel packages list to history
    :params: a dictionary, corresponding to a travel_package_structure
    :returns:
    :raises:
    """
    new_list = []
    for package in getTravelPackagesList(travel_package_structure):
        new_package = createTravelPackage()
        modifyDestination(new_package, getDestination(package))
        modifyPrice(new_package, getPrice(package))

        if getStartDate(package) == None: modifyStartDate(new_package, None)
        else: modifyStartDate(new_package, getStartDate(package).copy())

        if getEndDate(package) == None: modifyEndDate(new_package, None)
        else: modifyEndDate(new_package, getEndDate(package).copy())

        new_list.append(new_package)
    travel_package_structure["hist"].append(new_list)

def undo(travel_package_structure):
    """
    Function that deals with the undo function
    :params: a travel packages structure
    :returns: 
    :raises: ValueError
    """
    try: 
        modifyPackagesList(travel_package_structure, getTravelPackagesHist(travel_package_structure).pop())
    except:
        raise ValueError("Nothing to undo!")

def intersection(l1,l2):
    """
    Function that outputs the intersection of two lists
    :params: two lists
    :returns: a list
    """
    intersec = []
    for el in l1:
        if (el in l2) and (el not in intersec): intersec.append(el)
    return intersec

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

def parseDate(date_string):
    """
    Function that gets a string that represents a valid date with the format dd/mm/yyyy and outputs a dictionary with the keys "day", "month", "year" and their respective values 
    :params: a string
    :returns: a dictionary
    :raises: ValueError if date or date format is invalid
    """
    try:
        split_date = date_string.split("/")
        assert len(split_date) == 3
        
        day = int(split_date[0])
        month = int(split_date[1])
        year = int(split_date[2])

        assert isValidDate(day, month, year)
        date = {}
        date["day"] = int(split_date[0])
        date["month"] = int(split_date[1])
        date["year"] = int(split_date[2])
        return date
    except:
        raise ValueError("Invalid date or date format!")

def parsePrice (num_string:str):
    """
    Function that checks whether a string can be converted to a float
    :params: a string
    :returns: 
    :raises: ValueError if string is not convertable to a float
    """
    try:
        return round(float(num_string), 2)
    except: 
        raise ValueError("Invalid price, please enter a number!")

def addPackageToList(travel_package_list, travel_package):
    """
    Function that appends a travel package to a travel packages list
    :params: a travel package list, a travel package
    :returns: 
    :raises:
    """
    travel_package_list.append(travel_package)

def filterByPrice(travel_packages_list, price, lowerOrHigher):
    """
    Function that gets a list of travel packages, a float that represents the price and boolean value, than returns a list with all packages more expensive than the price if the boolean is true, or less expensive if the boolean is false
    :params: a list, a float, a boolean
    :returns: a list
    :raises:
    """
    updated_list = []
    for package in travel_packages_list:
        package_price = getPrice(package)
        if (package_price >= price) == lowerOrHigher: addPackageToList(updated_list, package)
    return updated_list

def destinationComparator(d1, d2):
    """
    Function that gets two strings representing two destinations and returns True if they are the same (case-insensitive), and False if they are different
    :params: two strings
    :returns: True or False
    :raises:
    """
    return d1.lower() == d2.lower()
    
def filterByDestination(travel_packages_list, destination, sameOrDifferent):
    """
    Function that gets a list of travel packages, a string that represents a destination and a boolean value, than returns a list of all packages that have the same destination as the one given, if the boolean is true, or a list of all packages with a different destination to the one given, if the boolean value is false
    :params: a list, a string, a boolean
    :returns: a list
    :raises:
    """
    updated_list = []
    for package in travel_packages_list:
        package_destination = getDestination(package)
        if (destinationComparator(package_destination,destination)) == sameOrDifferent: addPackageToList(updated_list, package)
    return updated_list

def dateComparator(d1, d2):
    """
    Function that compare two dates
    :params: two dictionaries representing dates
    :returns: 1, if the first is earlier than the second, 2, if they are equal, and 3 otherwise
    :raises:
    """
    if d1["year"] < d2["year"]: return True
    if d1["year"] == d2["year"]:
        if d1["month"] < d2["month"]: return True
        if d1["month"] == d2["month"]:
            if d1["day"] <= d2["day"]: return True
    return False

def filterByDate(travel_packages_list, l_date, r_date, isWithin:bool):
    """
    Function that returns a list of all packages that are within a given time frame, if the bool is true, and a list of all pacakges that aren't within the given time frame, if false
    :params: a travel package list, a date interval, a bool
    :returns: a list
    :raises:
    """
    filteredList = []
    otherFilter = []
    for package in travel_packages_list:
        if (dateComparator(l_date, getStartDate(package)) and dateComparator(getEndDate(package), r_date)):
               filteredList.append(package)
        else: otherFilter.append(package)

    if isWithin: return filteredList
    return otherFilter

def isWithinMonth(start_date:dict, end_date:dict, month):
    """
    Function that gets two dates and returns True if the period overlaps with a month, and false otherwise
    """
    start_month = start_date["month"]
    end_month = end_date["month"]
    start_year = start_date["year"]
    end_year = end_date["year"]
    start_idx = start_year*12 + start_month 
    end_idx = end_year*12 + end_month
    if (abs(start_idx - end_idx) >= 12): return True
    if start_year == end_year: 
        return  start_month <= month and month <= end_month
    return  start_month <= month or month <= end_month

def filterByMonth(travel_packages_list, month:int):
    """
    Functions that filters a travel package list by travels which don't contain a given month
    """
    updated_list = []
    for package in travel_packages_list:
        if (isWithinMonth(getStartDate(package), getEndDate(package), month)) == False: addPackageToList(updated_list, package)
    return updated_list

def sortByKey(travel_package_list, criteria, ascending:bool = True):
    """
    Function that deals with sorting a travel packages list by the given key
    :params: a travel packages list, a criteria function and a bool
    :returns: a list
    :raises:
    """
    return sorted(travel_package_list, key = lambda package: criteria(package), reverse = not ascending)

def averagePrice(travel_package_list):
    """
    Function that returns the average price of the travel packages
    """
    sum = 0
    for package in travel_package_list:
        sum += getPrice(package)
    return round(float(sum/len(travel_package_list)),2)

def deleteByCriteria(travel_packages_list, criteria):
    """
    Function that deletes all packages from the list with the given criteria
    :params: a travel pacakges list, a function representing a criteria
    :returns:
    :raises:
    """
    for package in travel_packages_list:
        if criteria(package):
            travel_packages_list.remove(package)


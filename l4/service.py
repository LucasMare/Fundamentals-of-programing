from domain import getPrice, getDestination

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
    Function that appends a travel package to a list
    :params: a dictionary corresponding to a travel_package_structure, a dictionary corresponding to a travel package
    :returns: 
    :raises:
    """
    travel_package_list.append(travel_package)

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

def destinationComparator(d1, d2):
    """
    Function that gets two strings representing two destinations and returns True if they are the same (case-insensitive), and False if they are different
    :params: two strings
    :returns: True or False
    :raises:
    """
    return d1.lower() == d2.lower()

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
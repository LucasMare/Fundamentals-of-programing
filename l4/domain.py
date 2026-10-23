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

def getTravelPackagesList(travel_packages):
    """
    Function that returns the list of travel packages 
    :params: a dictionary
    :returns: a list
    """
    return travel_packages["list"]

def getStartDate(travel_package):
    """
    Function that returns the start date of a travel package
    :params: a travel_package
    :returns: the value of start_date
    :raises:
    """
    return travel_package["start_date"]

def getEndDate(travel_package):
    """
    Function that returns the end date of a travel package
    :params: a travel_package
    :returns: the value of end_date
    :raises:
    """
    return travel_package["end_date"]

def getPrice(travel_package):
    """
    Function that returns the price of a given travel package
    :params: a dictionary representing a travel package
    :returns: a float representing the price
    :raises:
    """
    return travel_package["price"]

def getDestination(travel_package):
    """
        Function that returns the destination of a given travel package
        :params: a dictionary representing a travel package
        :returns: a string representing the destination
        :raises:
    """
    return travel_package["destination"]

def modifyStartDate(travel_package, new_start_date:dict):
    """
    Function that gets a travel package and a dictionary with the keys "day", "month, "year" and modifies the start date of the package to the given dictionary
    :params: a travel package, a dictionary
    :returns: 
    :raises:
    """
    travel_package["start_date"] = new_start_date

def modifyEndDate(travel_package, new_end_date:dict):
    """
    Function that gets a travel package and a dictionary with the keys "day", "month, "year" and modifies the end date of the package to the given dictionary
    :params: a travel package, a dictionary
    :returns: 
    :raises:
    """
    travel_package["end_date"] = new_end_date

def modifyDestination(travel_package, new_dest:str):
    """
    Function that modifies the destination of a travel package
    :params: a travel package, a string representing a destination
    :returns:
    :raises:
    """
    travel_package["destination"] = new_dest

def modifyPrice(travel_package, new_price:float):
    """
    Function that modifies the price of a travel package
    :params: a travel package, a float representing a price
    :returns:
    :raises:
    """
    travel_package["price"] = new_price

def appendCurrentListToHist(travel_package_structure):
    """
    Function that appends current travel packages list to history
    :params: a dictionary, corresponding to a travel_package_structure
    :returns:
    :raises:
    """
    travel_package_structure["hist"].append(travel_package_structure["list"].copy())


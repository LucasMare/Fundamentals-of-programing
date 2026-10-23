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

def appendCurrentListToHist(travel_package_structure):
    """
    Function that appends current travel packages list to history
    :params: a dictionary, corresponding to a travel_package_structure
    :returns:
    :raises:
    """
    travel_package_structure["hist"].append(travel_package_structure["list"].copy())


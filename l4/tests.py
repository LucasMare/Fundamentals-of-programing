from service import intersection, isLeapYear, isValidDate, parseDate, addPackageToList, filterByDestination, filterByPrice, destinationComparator, parsePrice
from domain import createTravelPackage, createTravelPackagesDataStructure, getTravelPackagesList, getDestination, getPrice, appendCurrentListToHist, getStartDate, getEndDate, modifyStartDate, modifyEndDate, modifyDestination, modifyPrice

def testIntersection():
    assert intersection([1,2,3],["a",2,{}]) == [2]

def testIsLeapYear():
    assert isLeapYear(2016) == True
    assert isLeapYear(1900) == False
    assert isLeapYear(1600) == True
    assert isLeapYear(1955) == False

def testIsValidDate():
    assert isValidDate(31,8,2026) == True
    assert isValidDate(29,2,2000) == True
    assert isValidDate(50,15,9999) == False
    assert isValidDate(29,2,1900) == False

def testParseDate():
    assert parseDate("10/9/2008") == {
        "day": 10,
        "month": 9,
        "year": 2008 
    }
    try:
        parseDate("99/1/2424")
        assert False
    except ValueError:
        assert True

def testParsePrice():
    assert parsePrice("19.20") == 19.20
    assert parsePrice("1920") == 1920
    try:    
        parsePrice("sjkdfh")
        assert False
    except ValueError:
        assert True 

def testCreateTravelPackage():
    assert createTravelPackage() == {
        "start_date": None,
        "end_date": None,
        "destination": "",
        "price": 0
    }

def testCreateTravelPackagesDataStructure():
        assert createTravelPackagesDataStructure () == {
            "list": [],
            "hist": []
        }

def testGetTravelPackagesList():
    assert getTravelPackagesList({"list": [], "hist": []}) == []
    assert getTravelPackagesList({"list": [1,2,33], "hist": []}) == [1,2,33]

def testGetPrice():
    package = createTravelPackage()
    package["price"] = 174.76
    assert getPrice(package) == 174.76

def testGetDestination():
    package = createTravelPackage()
    package["destination"] = "Paris"
    assert getDestination(package) == "Paris"

def testAppendCurrentListToHist():
    travel_packages_structure = createTravelPackagesDataStructure()
    travel_packages_structure["list"] = [1,2,3]
    appendCurrentListToHist(travel_packages_structure)
    assert travel_packages_structure["hist"] == [[1,2,3]]

def testAddPackageToList():
    travel_packages_structure = createTravelPackagesDataStructure()
    addPackageToList (getTravelPackagesList(travel_packages_structure), {})
    assert travel_packages_structure["list"] == [{}]

def testFilterByPrice():
    structure = createTravelPackagesDataStructure()
    for i in range(0,4):
        package = createTravelPackage()
        package["price"] = i
        addPackageToList(getTravelPackagesList(structure), package)
    assert filterByPrice (getTravelPackagesList(structure), 2, True) == [{"start_date": None, "end_date": None, "destination": "", "price": 2},{ "start_date": None, "end_date": None, "destination": "", "price": 3}]
    assert filterByPrice (getTravelPackagesList(structure), 2, False) == [{"start_date": None, "end_date": None, "destination": "", "price": 0},{ "start_date": None, "end_date": None, "destination": "", "price": 1}]

def testDestinationComparator():
    assert destinationComparator("paris", "Paris") == True
    assert destinationComparator("paris", "Pari") == False
    assert destinationComparator("paris", "1") == False

def testFilterByDestination():
    structure = createTravelPackagesDataStructure()
    places = ["Paris", "France", "baia Mare", "Sasar"]
    for i in range(0,4):
        package = createTravelPackage()
        package["destination"] = places[i]
        addPackageToList(getTravelPackagesList(structure), package)
    assert filterByDestination (getTravelPackagesList(structure), "Paris", True) == [{"start_date": None, "end_date": None, "destination": "Paris", "price": 0}]
    assert filterByDestination (getTravelPackagesList(structure), "Baia Mare", False) == [{"start_date": None, "end_date": None, "destination": "Paris", "price": 0},{ "start_date": None, "end_date": None, "destination": "France", "price": 0},{ "start_date": None, "end_date": None, "destination": "Sasar", "price": 0}]

#Incomplete
def testGetStartDate():
    package = createTravelPackage()
    assert getStartDate(package) == None

#Incomplete
def testGetEndDate():
    package = createTravelPackage()
    assert getEndDate(package) == None

#Incomplete
def testModifyStartDate():
    package = createTravelPackage()
    modifyStartDate(package, {"day":3, "month":10, "year":2000})
    assert getStartDate(package) == {"day":3, "month":10, "year":2000}

#Incomplete
def testModifyEndDate():
    package = createTravelPackage()
    modifyEndDate(package, {"day":3, "month":10, "year":2000})
    assert getEndDate(package) == {"day":3, "month":10, "year":2000}

def testModifyDestination():
    package = createTravelPackage()
    modifyDestination(package, "yeahhh")
    assert getDestination(package) == "yeahhh"

def testModifyPrice():
    package = createTravelPackage()
    modifyPrice(package, 1984)
    assert getPrice(package) == 1984

def testFunction():
    testIntersection()
    testIsLeapYear()
    testIsValidDate()
    testParseDate()
    testCreateTravelPackage()
    testCreateTravelPackagesDataStructure()
    testGetTravelPackagesList()
    testParsePrice()
    testAppendCurrentListToHist()
    testAddPackageToList()
    testGetPrice()
    testGetDestination()
    testFilterByPrice()
    testGetDestination()
    testFilterByDestination()
    testGetStartDate()
    testGetEndDate()
    testModifyStartDate()
    testModifyEndDate()
    testModifyDestination()
    testModifyPrice()
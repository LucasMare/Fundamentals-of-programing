from service import intersection, isLeapYear, isValidDate, checkDateFormat, parseDate, checkIfStringFloat, addPackageToList, filterByDestination, filterByPrice, destinationComparator
from domain import createTravelPackage, createTravelPackagesDataStructure, getTravelPackagesList, getDestination, getPrice, appendCurrentListToHist

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

def testCheckDateFormat():
    assert checkDateFormat("19/04/1954") == True
    assert checkDateFormat("akshdf") == False
    assert checkDateFormat("19.7.2026") == False
    assert checkDateFormat("99/18/8375") == False

def testParseDate():
    assert parseDate("10/9/2008") == {
        "day": 10,
        "month": 9,
        "year": 2008 
    }

def testCheckIfStringIsFloat():
    assert checkIfStringFloat("19.20") == True
    assert checkIfStringFloat("1920") == True
    assert checkIfStringFloat("plsajf") == False

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
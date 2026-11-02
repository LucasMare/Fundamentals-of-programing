from service import intersection, isLeapYear, isValidDate, parseDate, addPackageToList, filterByDestination, filterByPrice, destinationComparator, parsePrice, isWithinMonth, filterByMonth, createTravelPackagesDataStructure, getTravelPackagesList, appendCurrentListToHist, getTravelPackagesHist, modifyPackagesList, undo, modifyPackageFromList, getPackageFromList, dateComparator, filterByDate, averagePrice, deleteByCriteria
from domain import createTravelPackage, getDestination, getPrice, getStartDate, getEndDate, modifyStartDate, modifyEndDate, modifyDestination, modifyPrice
from validation import isValidCommand

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
    assert isValidDate(28,2,1900) == True

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
    assert createTravelPackage() == [None, None, "", 0]

def testCreateTravelPackagesDataStructure():
        assert createTravelPackagesDataStructure () == {
            "list": [],
            "hist": []
        }

def testGetTravelPackagesList():
    assert getTravelPackagesList({"list": [], "hist": []}) == []
    assert getTravelPackagesList({"list": [1,2,33], "hist": []}) == [1,2,33]

def testGetTravelPackagesHist():
    assert getTravelPackagesHist({"list": [], "hist": [[]]}) == [[]]
    assert getTravelPackagesHist({"list": [1,2,33], "hist": [2,3,55]}) == [2,3,55]
    

def testGetPrice():
    package = createTravelPackage()
    modifyPrice(package, 174.76)
    assert getPrice(package) == 174.76

def testGetDestination():
    package = createTravelPackage()
    modifyDestination(package, "Paris")
    assert getDestination(package) == "Paris"

def testAppendCurrentListToHist():
    travel_packages_structure = createTravelPackagesDataStructure()
    correct_hist = []
    assert getTravelPackagesHist(travel_packages_structure) == correct_hist
    package = createTravelPackage()
    modifyPrice(package, 1000)
    getTravelPackagesList(travel_packages_structure).append(package)
    correct_hist.append([package])
    appendCurrentListToHist(travel_packages_structure)
    assert getTravelPackagesHist(travel_packages_structure) == correct_hist

def testAddPackageToList():
    travel_packages_structure = createTravelPackagesDataStructure()
    addPackageToList (getTravelPackagesList(travel_packages_structure), {})
    assert getTravelPackagesList(travel_packages_structure) == [{}]

def testFilterByPrice():
    structure = createTravelPackagesDataStructure()
    for i in range(0,4):
        package = createTravelPackage()
        modifyPrice(package, i)
        addPackageToList(getTravelPackagesList(structure), package)
    assert filterByPrice (getTravelPackagesList(structure), 2, True) == [[None, None, "", 2],[None, None, "", 3]]
    assert filterByPrice (getTravelPackagesList(structure), 2, False) == [[None, None, "", 0],[None, None, "", 1]]

def testDestinationComparator():
    assert destinationComparator("paris", "Paris") == True
    assert destinationComparator("paris", "Pari") == False
    assert destinationComparator("paris", "1") == False
    assert destinationComparator("Paris", "paRis") == True

def testFilterByDestination():
    structure = createTravelPackagesDataStructure()
    places = ["Paris", "France", "baia Mare", "Sasar"]
    for i in range(0,4):
        package = createTravelPackage()
        modifyDestination(package, places[i])
        addPackageToList(getTravelPackagesList(structure), package)
    assert filterByDestination (getTravelPackagesList(structure), "Paris", True) == [[None, None, "Paris", 0]]
    assert filterByDestination (getTravelPackagesList(structure), "Baia Mare", False) == [[None, None, "Paris", 0], [None, None, "France", 0], [None, None, "Sasar", 0]]

def testGetStartDate():
    package = createTravelPackage()
    assert getStartDate(package) == None
    modifyStartDate(package, parseDate("10/8/2008"))
    assert getStartDate(package) == {"day": 10, "month": 8, "year": 2008}

def testGetEndDate():
    package = createTravelPackage()
    assert getEndDate(package) == None
    modifyEndDate(package, parseDate("10/8/2008"))
    assert getEndDate(package) == {"day": 10, "month": 8, "year": 2008}

def testModifyStartDate():
    package = createTravelPackage()
    modifyStartDate(package, {"day":3, "month":10, "year":2000})
    assert getStartDate(package) == {"day":3, "month":10, "year":2000}

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

def testModifyPackagesList():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    new_list = [package]
    modifyPackagesList(structure, new_list)
    assert getTravelPackagesList(structure) == [package]

def testUndo():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    appendCurrentListToHist(structure)
    addPackageToList(getTravelPackagesList(structure), package)
    undo(structure)
    assert getTravelPackagesList(structure) == []
    assert getTravelPackagesHist(structure) == [] 
    try: 
        undo(structure)
        assert False
    except: 
        assert True

def testIsWithinMonth():
    assert isWithinMonth(parseDate("10/1/2007"),parseDate("19/8/2007"),4) == True
    assert isWithinMonth(parseDate("10/9/2007"),parseDate("19/3/2008"),5) == False
    assert isWithinMonth(parseDate("10/1/2007"),parseDate("19/8/2007"),10) == False

def testFilterByMonth():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    modifyStartDate(package, parseDate("19/9/2008"))
    modifyEndDate(package, parseDate("5/3/2009"))
    addPackageToList(getTravelPackagesList(structure), package)
    assert filterByMonth(getTravelPackagesList(structure), 11) == []
    assert filterByMonth(getTravelPackagesList(structure), 5) == [package]

def testGetPackageFromList():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    addPackageToList(getTravelPackagesList(structure), package)
    assert getPackageFromList(getTravelPackagesList(structure), 0) == package

def testModifyPackageFromList():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    addPackageToList(getTravelPackagesList(structure),package)
    newPackage = createTravelPackage()
    modifyDestination(newPackage, "frappula")
    try: 
        modifyPackageFromList(getTravelPackagesList(structure), newPackage, 1)
        assert False
    except:
        assert True
    modifyPackageFromList(getTravelPackagesList(structure), newPackage, 0)
    assert getPackageFromList(getTravelPackagesList(structure),0) == newPackage

def testDateComparator():
    assert dateComparator(parseDate("10/9/2007"), parseDate("10/9/2007")) == True
    assert dateComparator(parseDate("1/1/2007"), parseDate("31/12/2006")) == False
    assert dateComparator(parseDate("11/9/2007"), parseDate("1/9/2007")) == False
    assert dateComparator(parseDate("10/8/2026"), parseDate("11/9/2026")) == True

def testFilterByDate():
    structure = createTravelPackagesDataStructure()
    package1 = createTravelPackage()  
    package2 = createTravelPackage()
    modifyStartDate(package1, parseDate("10/11/2025"))  
    modifyEndDate(package1, parseDate("11/12/2025"))  
    modifyStartDate(package2, parseDate("15/8/2013"))  
    modifyEndDate(package2, parseDate("15/9/2013"))
    addPackageToList(getTravelPackagesList(structure), package1)  
    addPackageToList(getTravelPackagesList(structure), package2)
    assert filterByDate(getTravelPackagesList(structure), parseDate("1/6/2025"), parseDate("31/12/2025"), True) == [package1]
    assert filterByDate(getTravelPackagesList(structure), parseDate("11/11/2010"), parseDate("5/12/2025"), True) == [package2]
    assert filterByDate(getTravelPackagesList(structure), parseDate("11/11/2025"), parseDate("31/12/2025"), True) == []
    assert filterByDate(getTravelPackagesList(structure), parseDate("1/6/2016"), parseDate("31/12/2016"), False) == [package1, package2]

def testIsValidCommand():
    try: 
        isValidCommand("klsf")
        assert False
    except: assert True
    isValidCommand("add")

def testAveragePrice():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    package1 = createTravelPackage()
    modifyPrice(package,1000.50)
    modifyPrice(package1,1500)
    addPackageToList(getTravelPackagesList(structure),package)
    addPackageToList(getTravelPackagesList(structure),package1)
    assert averagePrice(getTravelPackagesList(structure)) == 1250.25

def testDeleteByCriteria():
    structure = createTravelPackagesDataStructure()
    package = createTravelPackage()
    package1 = createTravelPackage()
    package2 = createTravelPackage()
    package3 = createTravelPackage()
    package4 = createTravelPackage()
    modifyPrice (package, 1800)

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
    testModifyPackagesList()
    testUndo()
    testIsWithinMonth()
    testFilterByMonth()
    testGetPackageFromList()
    testModifyPackageFromList()
    testDateComparator()
    testFilterByDate()
    testIsValidCommand()
    testAveragePrice()
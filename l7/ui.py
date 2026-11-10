from domain import Person, Event
from service import create_event_list, create_person_list, add_event_to_list, add_person_to_list
from datetime import datetime

def output_text_for_menu():
    print("""
    This is an app for managing a list of people and events. 
        1. Modify the list
    """)

def output_text_for_modify_menu():
    print("""
    Modify menu:
        1. Add a person
        2. Add an event
    """)

def input_person():
    id = input("Please enter the person's ID: ")
    name = input("Please enter the person's name: ")
    address = input("Please enter the person's address: ")
    return Person(id, name, address)

def input_event():
    id = input("Please enter the event's ID: ")
    format = "%d-%m-%Y %H:%M"
    datentime = input("Please enter the date and time: ")
    date = datetime.strptime(datentime, format).date()
    time = datetime.strptime(datentime, format).time()
    desc = input("Please enter a description: ")
    return Event(id, date, time, desc)

def menu():
    person_list = create_person_list()
    event_list = create_event_list()
    try:
        while True:
            output_text_for_menu()
            choice = input()
            match choice:
                case "1": modify_menu(person_list, event_list)
                case _: print("Invalid choice")

    except Exception as error:
        print(error)

def modify_menu(person_list, event_list):
    while True:
        output_text_for_modify_menu()
        choice = input()
        match choice:
            case "1":
                add_person_to_list(person_list, input_person())
                print("Successfully added person!")
            case "2":
                add_event_to_list(event_list, input_event())
                print("Successfully added event!")
            case _:
                6
                print("Invalid choice")


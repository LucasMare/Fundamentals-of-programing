from Domain.domain import Person, Event
from datetime import datetime
from validate import Validation, ValidationError

class UI:
    def __init__ (self, person_service, event_service):
        self.__person_service = person_service
        self.__event_service = event_service

    def get_person_service(self):
        return self.__person_service

    def get_event_service(self):
        return self.__event_service

    @staticmethod
    def output_text():
        print("""
        This is an app for managing a list of people and events. 
            1. Modify the list
        """)

    @staticmethod
    def input_valid_name(message="Input the person's name: "):
        while True:
            print(message)
            name = input()
            try:
                Validation.validate_person_name(name)
                return name
            except ValidationError as error:
                message = str(error) + " Try again:"

    @staticmethod
    def input_valid_date(message = "Input a date with format dd/mm/yyyy:", date_format = "%d/%m/%Y"):
        while True:
            print(message)
            valid_date = input()
            try:
                return datetime.strptime(valid_date, date_format).date()
            except ValueError:
                message = "Invalid date or format, try again:"

    @staticmethod
    def input_valid_time(message = f"Input a time with format {'"'}hh:ss{'"'}: ", time_format = "%H:%M"):
        while True:
            print(message)
            valid_time = input()
            try:
                return datetime.strptime(valid_time, time_format).time()
            except ValueError:
                message = "Invalid time or format, try again:"

    @staticmethod
    def input_person() -> Person:
        person_id = input("Please enter the person's ID:\n")
        name = UI.input_valid_name()
        address = input("Please enter the person's address:\n")
        return Person(person_id, name, address)

    @staticmethod
    def input_event() -> Event:
        event_id = input("Please enter the event's ID:\n")
        date = UI.input_valid_date()
        time = UI.input_valid_time()
        desc = input("Please enter a description:\n")
        return Event(event_id, date, time, desc)

    def run(self):
        while True:
            self.output_text()
            choice = input()
            match choice:
                case "1":
                    modify_ui = ModifyUI(self.get_person_service(), self.get_event_service())
                    modify_ui.run()
                case 'p':
                    print("This is the list of stored people:")
                    for person in self.get_person_service().get_repo().items():
                        print(person)
                case 'e':
                    print("This is the list of stored events:")
                    for event in self.get_event_service().get_repo().items():
                        print(event)
                case _: print("Invalid choice!")

class ModifyUI(UI):
    @staticmethod
    def output_text():
        print("""
        Modify menu:
            1. Add a person
            2. Add an event
            0. Go back
        """)

    def run(self):
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        person = self.input_person()
                        Validation.validate_id_uniqueness(person, self.get_person_service().get_repo())
                        self.get_person_service().add(person)
                        print("Successfully added person!")
                    case "2":
                        event = self.input_event()
                        Validation.validate_id_uniqueness(event, self.get_event_service().get_repo())
                        self.get_event_service().add(event)
                        print("Successfully added event!")
                    case "0":
                        break
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)

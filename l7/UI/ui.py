from Domain.domain import Person, Event, Attendance
from datetime import datetime

from Repository.repository import Repository
from validate import Validation, ValidationError
from Service.service import Service

class GeneralUI:
    def __init__ (self, person_service, event_service, attendance_service):
        self.__person_service = person_service
        self.__event_service = event_service
        self.__attendance_service = attendance_service

    @property
    def person_service(self):
        """
        Person Service getter
        :return:
        """
        return self.__person_service

    @property
    def event_service(self):
        """
        Event service getter
        :return:
        """
        return self.__event_service

    @property
    def attendance_service(self):
        """
        Attendance service getter
        :return:
        """
        return self.__attendance_service

class UI(GeneralUI):
    @staticmethod
    def output_text():
        print("""
            This is an app for managing a list of people and events. 
                1. Add to the lists
                2. Delete from the lists
                3. Search items in the lists
                4. Modify an item in the lists
                5. Mark a person attending an event
                6. Reports
                0. Exit
            """)

    def run(self):
        """
        Method for the general menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            match choice:
                case "1":
                    add_ui = AddUI(self.person_service, self.event_service, self.attendance_service)
                    add_ui.run()
                case "2":
                    delete_ui = DeleteUI(self.person_service, self.event_service, self.attendance_service)
                    delete_ui.run()
                case "3":
                    search_ui = SearchUI(self.person_service, self.event_service, self.attendance_service)
                    search_ui.run()
                case "4":
                    modify_ui = ModifyUI(self.person_service, self.event_service, self.attendance_service)
                    modify_ui.run()
                case "5":
                    attendance_ui = AttendingUI(self.person_service, self.event_service, self.attendance_service)
                    attendance_ui.run()
                case "6":
                    report_ui = ReportUI(self.person_service, self.event_service, self.attendance_service)
                    report_ui.run()
                case 'p':
                    self.print_people_list()
                case 'e':
                    self.print_events_list()
                case 'a':
                    self.print_attendance_list()
                case "0":
                    print("Bye beach!!!!")
                    exit()
                case _:
                    print("Invalid choice!")

    @staticmethod
    def input_valid_id(cservice: Service, message="Input an ID:"):
        while True:
            print(message)
            gotten_id = input()
            try:
                Validation.validate_ids_presence(gotten_id, cservice.repo)
                return gotten_id
            except ValidationError:
                message = "No entry with this id, try again:"

    def print_people_list(self, message="This is the list of all people:"):
        """
        Method for printing all people
        :param message:
        :return:
        """
        print(message)
        for person in self.person_service.items():
            print(person)
        print('\n')

    def print_events_list(self, message="This is the list of stored events:"):
        """
        Method for printing all events
        :param message:
        :return:
        """
        print(message)
        for event in self.event_service.items():
            print(event)
        print('\n')

    def print_attendance_list(self, message="This is the list of all attendances:"):
        """
        Method for printing all attendances
        :param message:
        :return:
        """
        print(message)
        for attendance in self.attendance_service.items():
            print(attendance)
        print('\n')

class AddUI(GeneralUI):
    @staticmethod
    def output_text():
        print("""
        Add menu:
            1. Add a person
            2. Add an event
            0. Go back
        """)

    @staticmethod
    def input_valid_id(message="Input the person's ID: "):
        """
        Method for inputting a valid name
        :param message:
        :return:
        """
        while True:
            print(message)
            new_id = input()
            try:
                Validation.validate_id(new_id)
                return new_id
            except ValidationError as error:
                message = str(error) + " Try again:"

    @staticmethod
    def input_valid_name(message="Input the person's name: "):
        """
        Method for inputting a valid name
        :param message:
        :return:
        """
        while True:
            print(message)
            name = input()
            try:
                Validation.validate_person_name(name)
                return name
            except ValidationError as error:
                message = str(error) + " Try again:"

    @staticmethod
    def input_valid_date(message=f"Input a date with format {'"'}dd/mm/yyyy{'"'}:", date_format="%d/%m/%Y"):
        """
        Method for inputting a valid date
        :param message:
        :param date_format:
        :return:
        """
        while True:
            print(message)
            valid_date = input()
            try:
                return datetime.strptime(valid_date, date_format).date()
            except ValueError:
                message = "Invalid date or format, try again:"

    @staticmethod
    def input_valid_time(message=f"Input a time with format {'"'}hh:ss{'"'}: ", time_format="%H:%M"):
        """
        Method for inputting a valid time
        :param message:
        :param time_format:
        :return:
        """
        while True:
            print(message)
            valid_time = input()
            try:
                return datetime.strptime(valid_time, time_format).time()
            except ValueError:
                message = "Invalid time or format, try again:"

    @staticmethod
    def input_person() -> Person:
        """
        Method for inputting a new person object
        :return:
        """
        person_id = AddUI.input_valid_id()
        name = AddUI.input_valid_name()
        address = input("Please enter the person's address:\n")
        return Person(person_id, name, address)

    @staticmethod
    def input_event() -> Event:
        """
        Method for inputting a new event object
        :return:
        """
        event_id = AddUI.input_valid_id("Input the event's ID: ")
        date = AddUI.input_valid_date()
        time = AddUI.input_valid_time()
        desc = input("Please enter a description:\n")
        return Event(event_id, date, time, desc)

    def run(self):
        """
        Method for the add menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        person = self.input_person()
                        Validation.validate_id_uniqueness(person, self.person_service.repo)
                        self.person_service.add(person)
                        print("Successfully added person!")
                    case "2":
                        event = self.input_event()
                        Validation.validate_id_uniqueness(event, self.event_service.repo)
                        self.event_service.add(event)
                        print("Successfully added event!")
                    case "0":
                        break
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)

class DeleteUI(UI):
    @staticmethod
    def output_text():
        print("""
            Delete menu:
                1. Delete a person
                2. Delete an event
                0. Go Back
            """)

    def run(self):
        """
        Method for the delete menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        self.print_people_list()
                        del_id = self.input_valid_id(self.person_service, "Input the ID of the person you want to delete: ")
                        self.person_service.delete(del_id)
                        self.attendance_service.delete_all_attendances_by_param(del_id)
                        print("Successfully deleted the person!")
                    case "2":
                        self.print_events_list()
                        del_id = self.input_valid_id(self.event_service, "Input the ID of the event you want to delete: ")
                        self.event_service.delete(del_id)
                        self.attendance_service.delete_all_attendances_by_param(del_id, "event")
                        print("Successfully deleted the event!")
                    case "0":
                        break
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)

class SearchUI(UI):
    @staticmethod
    def output_text():
        print("""
            Search menu:
                1. Search a person by id
                2. Search an event by id
                0. Go Back
            """)

    def run(self):
        """
        Method for the search menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        search_id = input("Please enter id to search by: ")
                        Validation.validate_ids_presence(search_id, self.person_service.repo)
                        print("Person with the given ID is:\n", self.person_service.item_by_id(search_id))
                    case "2":
                        search_id = input("Please enter id to search by: ")
                        Validation.validate_ids_presence(search_id, self.event_service.repo)
                        print("Event with the given ID is:\n", self.event_service.item_by_id(search_id))
                    case "0":
                        break
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)

class ModifyUI(UI):
    @staticmethod
    def output_text():
        print("""
        Modify menu:
            1. Modify a person
            2. Modify an event
            0. Go back
        """)

    @staticmethod
    def input_valid_string(message="Input the person's name: "):
        """
        Method for inputting a string and returning None if it is empty
        :param message:
        :return:
        """
        print(message)
        output = input()
        if not output:
            return None
        return output

    @staticmethod
    def input_valid_date(message = f"Input a date with format {'"'}dd/mm/yyyy{'"'}:", date_format = "%d/%m/%Y"):
        """
        Method for inputting a valid date
        :param message:
        :param date_format:
        :return:
        """
        while True:
            print(message)
            valid_date = input()
            if not valid_date:
                return None
            try:
                return datetime.strptime(valid_date, date_format).date()
            except ValueError:
                message = "Invalid date or format, try again:"

    @staticmethod
    def input_valid_time(message=f"Input a time with format {'"'}hh:ss{'"'}: ", time_format="%H:%M"):
        """
        Method for inputting a valid time
        :param message:
        :param time_format:
        :return:
        """
        while True:
            print(message)
            valid_time = input()
            if not valid_time:
                return None
            try:
                return datetime.strptime(valid_time, time_format).time()
            except ValueError:
                message = "Invalid time or format, try again:"

    def run(self):
        """
        Method for the modify menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        self.print_people_list()
                        mod_id = self.input_valid_id(self.person_service,"Input the ID of the person you want to modify: ")
                        modified_person = self.person_service.item_by_id(mod_id)
                        print("Input the data you want to modify (Leave blank to skip):")
                        new_name = self.input_valid_string("Enter a name: ")
                        new_address = self.input_valid_string("Enter an address: ")
                        self.person_service.modify_person(modified_person, new_name, new_address)
                        print("Successfully modified person! Here it is now:\n", modified_person)
                    case "2":
                        self.print_events_list()
                        mod_id = self.input_valid_id(self.event_service,"Input the ID of the event you want to modify: ")
                        modified_event = self.event_service.item_by_id(mod_id)
                        print("Input the data you want to modify to (leave blank to skip):")
                        new_date = self.input_valid_date("Enter a date (dd/mm/yyyy):")
                        new_time = self.input_valid_time("Enter a time (HH:MM):")
                        new_description = self.input_valid_string("Input a description: ")
                        self.event_service.modify_event(modified_event, new_date, new_time, new_description)
                        print("Successfully modified event! Here it is now:\n", modified_event)
                    case "0":
                        break
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)

class AttendingUI(UI):
    @staticmethod
    def output_text():
        print("""
        Attendances menu:
            1. Add attendance
            2. Delete Attendance
            0. Go back
        """)
    def run(self):
        """
        Method for the attendance menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        self.print_people_list()
                        person_id = self.input_valid_id(self.person_service, "Enter the id of a person:")
                        self.print_events_list()
                        event_id = self.input_valid_id(self.event_service, "Enter the id of the event they are attending: :")
                        attendance = Attendance(self.person_service.item_by_id(person_id), self.event_service.item_by_id(event_id))
                        self.attendance_service.add(attendance)
                        print(f"Successfully made person with id:{person_id} attend the event with id:{event_id}")
                    case "2":
                        self.print_events_list()
                        event_id = self.input_valid_id(self.event_service,"Enter the id of the event from which you want to delete an attendance:")
                        attendances = self.attendance_service.attendances_by_param(event_id)
                        temp_repo = Repository()
                        temp_service = Service(temp_repo)
                        if attendances:
                            print("These are the people attending this event:")
                            for at in attendances:
                                print(at.person())
                                temp_service.add(at.person())
                            person_id = self.input_valid_id(temp_service, "Enter the id of the person you want to remove from this event:")
                            self.attendance_service.delete(person_id + event_id)
                            print("Successfully deleted attendance!")
                        else:
                            print("No people are attending this event!")
                    case "0":
                        return
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)

class ReportUI(UI):
    @staticmethod
    def output_text():
        print("""
        Report menu: 
            1. Get all events for a person sorted by description and date
            2. Get people with the most events
            3. Top 20% events by people attending
            4. Which of the top k people attends a top k event
            0. Go back
        """)

    @staticmethod
    def input_valid_int(l = 0, h = 10, message = "Input a number:"):
        while True:
            print(message)
            try:
                p = int(input())
                assert p>=l
                assert p<=h
                return p
            except Exception:
                message = "Invalid choice, try again:"

    def run(self):
        """
        Method for the attendance menu
        :return:
        """
        while True:
            self.output_text()
            choice = input()
            try:
                match choice:
                    case "1":
                        self.print_people_list()
                        person_id = self.input_valid_id(self.person_service)
                        events_for_person = self.attendance_service.report_all_events_for_person_by_description_date(person_id)
                        if not events_for_person:
                            raise ValidationError("No events")
                        print("Events for this person are:\n", events_for_person)
                    case "2":
                        person_max_events = self.attendance_service.first_k_items_by_criteria(self.person_service, "person", 1)[0]
                        print(f"The person with the most events is person with id:{person_max_events.id()} with {self.attendance_service.nr_attendances_by_param(person_max_events.id(), "person")} events")
                    case "3":
                        most_popular_events = self.attendance_service.first_k_items_by_criteria(self.event_service, "event", int(self.event_service.number_of_items()/5)+1)
                        print("Top 20% most popular events are: ")
                        for el in most_popular_events:
                            a_for_person = self.attendance_service.nr_attendances_by_param(el.id(), "event")
                            msg = "people"
                            if a_for_person<=1: msg = "person"
                            print(f"Event with description {'"'}{el.description()}{'"'} with {a_for_person} {msg}")
                    case "4":
                        k = ReportUI.input_valid_int(l = 0, h = int(min(self.person_service.number_of_items(),self.event_service.number_of_items()))-1, message = "Input the k parameter:")
                        attendances = self.attendance_service.top_k_interlacing(self.person_service, self.event_service, k)
                        for a in attendances:
                            print(f"Top {k} person with id:{a.person().id()} attends top k event with id:{a.event().id()}")
                    case "0":
                        return
                    case _:
                        print("Invalid choice!")
            except ValidationError as error:
                print(error)


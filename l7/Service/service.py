from Domain.domain import Person, Event, Attendance
from datetime import date, time, datetime
import random
from validate import Validation, ValidationError


class Service:
    """
    Class for the service of the person and event lists
    """
    def __init__ (self, repository):
        self.__repo = repository

    def get_repo(self):
        """
        Method that returns the repository of the service object
        :return:
        """
        return self.__repo

    def items_by_id(self) -> dict:
        """
        Method that returns a dictionary where the keys are the id's and the values are the objects
        :return:
        """
        return self.get_repo().items_by_id()

    def items(self) -> list:
        """
        Method that returns the list of objects from the services repo
        :return:
        """
        return self.get_repo().items()

    def ids(self) -> list:
        """
        Method that returns a list of all id's of the services repo
        :return:
        """
        return self.get_repo().ids()

    def add(self, person_or_event):
        """
        Method that adds an object to the repository
        :param person_or_event:
        :return:
        """
        self.get_repo().add(person_or_event)

    def delete(self, object_id:str):
        """
        Method for deleting an object with the given id
        :param object_id:
        :return:
        """
        self.get_repo().delete(object_id)

    def item_by_id(self, search_id):
        """
        Method for returning an item given its id
        :param search_id:
        :return:
        """
        return self.get_repo().items_by_id()[search_id]

    @staticmethod
    def generate_rand_string(use_special_characters_and_digits = False, length = 8):
        """
        Function for generating a random string of characters
        :param length:
        :param use_special_characters_and_digits:
        :return:
        """
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if use_special_characters_and_digits:
            characters += '0123456789!@#$%^&*()'
        rand_id = ""
        for i in range(length):
            rand_id += random.choice(characters)
        return rand_id

    def generate_random_id(self):
        """
        Method for generating a unique id
        :return:
        """
        ids = self.get_repo().ids()
        rand_id = self.generate_rand_string(True, 4)

        while rand_id in ids:
            rand_id = self.generate_rand_string(True, 4)

        return rand_id

class PeopleService(Service):
    """
    Class with methods specific to the person list
    """
    @staticmethod
    def modify_person(modified_person:Person, new_name = None, new_address = None):
        """
        Method for modifying a given person
        """
        if new_name is not None:
            modified_person.set_name(new_name)
        if new_address is not None:
            modified_person.set_address(new_address)

    def generate_rand_person(self):
        """
        Method for generating a random person
        :return:
        """
        return Person(self.generate_random_id(), self.generate_rand_string(length=random.randrange(3,30)), self.generate_rand_string(True, random.randrange(1,30)))

class EventService(Service):
    """
    Class with methods specific for the event list
    """
    @staticmethod
    def modify_event(modified_event: Event, new_date:date | None = None, new_time:time | None = None, new_description = None):
        """
        Method for modifying a given person
        """
        if new_date is not None:
            modified_event.set_date(new_date)
        if new_time is not None:
            modified_event.set_time(new_time)
        if new_description is not None:
            modified_event.set_description(new_description)

    @staticmethod
    def generate_random_date(lower = 2000) -> date:
        """
        Method for generating a random
        :param lower:
        :return:
        """
        year = random.randrange(lower, datetime.now().year)
        month = random.randrange(1, 12)
        day = random.randrange(1,31)
        while True:
            try:
                return date(year, month, day)
            except ValueError:
                day = random.randrange(1, 31)

    @staticmethod
    def generate_random_time():
        """
        Method for generating a random time
        :return:
        """
        hour = random.randrange(0,23)
        minute = random.randrange(0,59)
        return time(hour, minute)

    def generate_random_event(self):
        """
        Method for generating a random event
        :return:
        """
        return Event(self.generate_random_id(), self.generate_random_date(), self.generate_random_time(), self.generate_rand_string(length=random.randrange(10, 50)))


class AttendanceService(Service):
    """
    Class for the attendance service
    """

    def attendances_by_param(self, search_id, criteria = "event"):
        """
        Method for getting all attendances by param
        :param search_id:
        :param criteria:
        :return:
        """
        return self.get_repo().attendances_by_param(search_id, criteria)

    def delete_all_attendances_by_param(self, delete_by_id, criteria = "person"):
        """
        Method for deleting all attendances for a person or event
        :param delete_by_id:
        :param criteria:
        :return:
        """
        self.get_repo().delete_all_attendances_by_param(delete_by_id, criteria)

    def generate_random_attendance(self, people_list, event_list):
        """
        Method for generating random attendance
        :param people_list:
        :param event_list:
        :return:
        """
        all_tuples = []
        for p in people_list:
            for e in event_list:
                all_tuples.append((p,e))

        while True:
            rand_tuple = random.choice(all_tuples)
            attendance = Attendance(rand_tuple[0], rand_tuple[1])
            try:
                Validation.validate_id_uniqueness(attendance, self.get_repo())
                return attendance
            except ValidationError:
                pass








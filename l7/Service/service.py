from Domain.domain import Person, Event
from datetime import date, time, datetime
import random

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
        rand_id = self.generate_rand_string(True)

        while rand_id in ids:
            rand_id = self.generate_rand_string(True)

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




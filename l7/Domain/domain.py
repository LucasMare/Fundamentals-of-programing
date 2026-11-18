from datetime import date, time

class Person:
    def __init__(self, personID, name, address):
        self.__attributes = {
            "id": personID,
            "name": name,
            "address": address
        }

    def id(self):
        """
        Returns the person ID
        :return:
        """
        return self.__attributes["id"]

    def name(self):
        """
        Returns the person name
        :return:
        """
        return self.__attributes["name"]

    def address(self):
        """
        Returns the person address
        :return:
        """
        return self.__attributes["address"]

    def set_personID(self, personID):
        """
        Sets the person ID
        :param personID:
        :return:
        """
        self.__attributes["id"] = personID

    def set_name(self, name):
        """
        Sets the person name
        :param name:
        :return:
        """
        self.__attributes["name"] = name

    def set_address(self, address):
        """
        Sets the person address
        :param address:
        :return:
        """
        self.__attributes["address"] = address

    def __str__(self):
        return f"ID: {self.id()}, name: {self.name()}, address: {self.address()}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other:object, /) -> bool:
        return self.name() == other.name() and self.address() == other.address()

class Event:
    def __init__(self, eventID, event_date:date, event_time:time, description):
        self.__attributes = {
            "id": eventID,
            "date": event_date,
            "time": event_time,
            "description": description
        }

    def id(self):
        """
        Returns the event ID
        :return:
        """
        return self.__attributes["id"]

    def date(self):
        """
        Returns the event date
        :return:
        """
        return self.__attributes["date"]

    def time(self):
        """
        Returns the event time
        :return:
        """
        return self.__attributes["time"]

    def description(self):
        """
        Returns the event description
        :return:
        """
        return self.__attributes["description"]

    def set_eventID(self, eventID):
        """
        Sets the event ID
        :param eventID:
        :return:
        """
        self.__attributes["id"] = eventID

    def set_date(self, event_date:date):
        """
        Sets the event date
        :param event_date:
        :return:
        """
        self.__attributes["date"] = event_date

    def set_time(self, event_time:time):
        """
        Sets the event time
        :param event_time:
        :return:
        """
        self.__attributes["time"] = event_time

    def set_description(self, description):
        """
        Sets the event description
        :param description:
        :return:
        """
        self.__attributes["description"] = description

    def __str__(self):
        return f"ID: {self.id()}, date: {self.date()}, time: {self.time()}, description: {self.description()}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other:object, /) -> bool:
        return self.time() == other.time() and self.date() == other.date() and self.description() == other.description()

class Attendance:
    def __init__(self, person:Person, event:Event):
        self.__person = person
        self.__event = event
        self.__id = self.__generate_id()

    def id(self):
        """
        Id getter
        :return:
        """
        return self.__id

    def person(self):
        """
        Getter for the person
        :return:
        """
        return self.__person

    def event(self):
        """
        Getter for the event
        :return:
        """
        return self.__event

    def __generate_id(self) -> str:
        """
        Method for generating a unique id for the attendance using the ids of the person and the event
        :return:
        """
        return self.person().id() + self.event().id()

    def __repr__(self):
        return f"Person with ID: {self.person().id()} attends the event with ID: {self.event().id()}"

    def __eq__(self, other:object, /):
        return self.id() == other.id()



from datetime import date, time

class Person:
    def __init__(self, personID, name, address):
        self.attributes = {
            "id": personID,
            "name": name,
            "address": address
        }
        self.attendances = []

    def id(self):
        """
        Returns the person ID
        :return:
        """
        return self.attributes["id"]

    def name(self):
        """
        Returns the person name
        :return:
        """
        return self.attributes["name"]

    def address(self):
        """
        Returns the person address
        :return:
        """
        return self.attributes["address"]

    def set_personID(self, personID):
        """
        Sets the person ID
        :param personID:
        :return:
        """
        self.attributes["id"] = personID

    def set_name(self, name):
        """
        Sets the person name
        :param name:
        :return:
        """
        self.attributes["name"] = name

    def set_address(self, address):
        """
        Sets the person address
        :param address:
        :return:
        """
        self.attributes["address"] = address

    def add_attendance(self, attendance:'Attendance'):
        """
        Adds an attendance object to the list of attendances
        :param attendance:
        :return:
        """
        self.attendances.append(attendance)

    def new_attendance(self, event:'Event'):
        """
        Adds a new attendance to the person's and event's field
        :param event:
        :return:
        """
        attendance = Attendance(self, event)
        self.add_attendance(attendance)
        event.add_attendance(attendance)

    def __str__(self):
        return f"ID: {self.id()}, name: {self.name()}, address: {self.address()}"

    def __repr__(self):
        return str(self)


class Event:
    def __init__(self, eventID, event_date:date, event_time:time, description):
        self.attributes = {
            "id": eventID,
            "date": event_date,
            "time": event_time,
            "description": description
        }
        self.attendances = []

    def id(self):
        """
        Returns the event ID
        :return:
        """
        return self.attributes["id"]

    def date(self):
        """
        Returns the event date
        :return:
        """
        return self.attributes["date"]

    def time(self):
        """
        Returns the event time
        :return:
        """
        return self.attributes["time"]

    def description(self):
        """
        Returns the event description
        :return:
        """
        return self.attributes["description"]

    def set_eventID(self, eventID):
        """
        Sets the event ID
        :param eventID:
        :return:
        """
        self.attributes["id"] = eventID

    def set_date(self, event_date:date):
        """
        Sets the event date
        :param event_date:
        :return:
        """
        self.attributes["date"] = event_date

    def set_address(self, event_time:time):
        """
        Sets the event time
        :param event_time:
        :return:
        """
        self.attributes["time"] = event_time

    def set_description(self, description):
        """
        Sets the event description
        :param description:
        :return:
        """
        self.attributes["description"] = description

    def add_attendance(self, attendance:'Attendance'):
        """
        Adds an attendance object to the list of attendances
        :param attendance:
        :return:
        """
        self.attendances.append(attendance)

    def __str__(self):
        return f"ID: {self.id()}, date: {self.date()}, time: {self.time()}, description: {self.description()}"

    def __repr__(self):
        return str(self)

class Attendance:
    def __init__(self, person:Person, event:Event):
        self.person = person
        self.event = event

    def __repr__(self):
        return f"Person with ID:{self.person.id()} attends the event with ID:{self.event.id()}"




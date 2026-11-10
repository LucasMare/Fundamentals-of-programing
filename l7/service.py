from domain import Person, Event

def create_person_list():
    """
    Creates a new list of people
    :return:
    """
    return {}

def create_event_list():
    """
    Creates a new list of events
    :return:
    """
    return {}

def add_person_to_list(person_list, person:Person):
    """
    Adds a new person to a list of people
    :param person_list:
    :param person:
    :return:
    """
    person_list[person.id()] = person

def add_event_to_list(event_list, event:Event):
    """
    Adds a new event to a list of events
    :param event_list:
    :param event:
    :return:
    """
    event_list[event.id()] = event

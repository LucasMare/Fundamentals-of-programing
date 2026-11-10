from domain import Person, Event
from datetime import date, time

def test_person_id():
    person = Person("sdlkjf", "Lucas", "sldjkflsd")
    assert person.id() == "sdlkjf"

def test_person_name():
    person = Person("sdlkjf", "Lucas", "sldjkflsd")
    assert person.name() == "Lucas"

def test_person_address():
    person = Person("sdlkjf", "Lucas", "sldjkflsd")
    assert person.address() == "sldjkflsd"

def test_person_set_id():
    person = Person("sdlkjf", "Lucas", "sldjkflsd")
    person.set_personID("ksljdf")
    assert person.id() == "ksljdf"

def test_person_set_name():
    person = Person("sdlkjf", "Lucas", "sldjkflsd")
    person.set_name("Sarah")
    assert person.name() == "Sarah"

def test_person_set_address():
    person = Person("sdlkjf", "Lucas", "sldjkflsd")
    person.set_address("home")
    assert person.address() == "home"

def test_event_id():
    event = Event("ksldfjk", date(2026, 10, 9), time(10, 00), "desc")
    assert event.id() == "ksldfjk"

def test_event_date():
    event = Event("ksldfjk", date(2026, 10, 9), time(10, 00), "desc")
    assert event.date() == date(2026, 10, 9)

def test_function():
    test_person_id()
    test_person_name()
    test_person_address()
    test_person_set_id()
    test_person_set_name()
    test_person_set_address()
    test_event_id()
    test_event_date()
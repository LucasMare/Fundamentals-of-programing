from Domain.domain import Person, Event
from datetime import date, time

class Tests:
    @staticmethod
    def test_person_id():
        person = Person("sdlkjf", "Lucas", "sldjkflsd")
        assert person.id() == "sdlkjf"

    @staticmethod
    def test_person_name():
        person = Person("sdlkjf", "Lucas", "sldjkflsd")
        assert person.name() == "Lucas"

    @staticmethod
    def test_person_address():
        person = Person("sdlkjf", "Lucas", "sldjkflsd")
        assert person.address() == "sldjkflsd"

    @staticmethod
    def test_person_set_id():
        person = Person("sdlkjf", "Lucas", "sldjkflsd")
        person.set_personID("ksljdf")
        assert person.id() == "ksljdf"

    @staticmethod
    def test_person_set_name():
        person = Person("sdlkjf", "Lucas", "sldjkflsd")
        person.set_name("Sarah")
        assert person.name() == "Sarah"

    @staticmethod
    def test_person_set_address():
        person = Person("sdlkjf", "Lucas", "sldjkflsd")
        person.set_address("home")
        assert person.address() == "home"

    @staticmethod
    def test_event_id():
        event = Event("ksldfjk", date(2026, 10, 9), time(10, 00), "desc")
        assert event.id() == "ksldfjk"

    @staticmethod
    def test_event_date():
        event = Event("ksldfjk", date(2026, 10, 9), time(10, 00), "desc")
        assert event.date() == date(2026, 10, 9)

    @staticmethod
    def test_function():
        Tests.test_person_id()
        Tests.test_person_name()
        Tests.test_person_address()
        Tests.test_person_set_id()
        Tests.test_person_set_name()
        Tests.test_person_set_address()
        Tests.test_event_id()
        Tests.test_event_date()
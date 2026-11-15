from Domain.domain import Person, Event
from datetime import date, time
from Repository.repository import Repository
from validate import Validation
from Service.service import PeopleService, EventService


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
    def test_repo_items_by_id():
        repo = Repository()
        assert repo.items_by_id() == {}
        per = Person("24kkl4l", "Lucas", "unnamed road, 38")
        repo.add(per)
        assert repo.items_by_id() == {
            "24kkl4l": per
        }

    @staticmethod
    def test_repo_items():
        repo = Repository()
        assert repo.items() == []
        per = Person("24kkl4l", "Lucas", "unnamed road, 38")
        repo.add(per)
        assert repo.items() == [per]

    @staticmethod
    def test_repo_ids():
        repo = Repository()
        assert repo.ids() == []
        per = Person("24kkl4l", "Lucas", "unnamed road, 38")
        repo.add(per)
        assert repo.ids() == ["24kkl4l"]

    @staticmethod
    def test_repo_add():
        repo = Repository()
        per = Person("24kkl4l", "Lucas", "unnamed road, 38")
        repo.add(per)
        assert repo.items_by_id() == {
            "24kkl4l": per
        }

    @staticmethod
    def test_validate_person_name():
        try:
            Validation.validate_person_name("")
            assert False
        except Exception as e:
            assert str(e) == "Name cannot be empty!"
        try:
            Validation.validate_person_name("Lucas")
        except:
            assert False

    @staticmethod
    def test_validate_id_uniqueness():
        per = Person("lfkj3", "Lucas", "alkjf")
        repo = Repository()
        repo.add(per)
        try:
            Validation.validate_id_uniqueness(per, repo)
            assert False
        except Exception as e:
            assert str(e) == "ID already present!"

    @staticmethod
    def test_validate_ids_presence():
        per = Person("lfkj3", "Lucas", "alkjf")
        repo = Repository()
        repo.add(per)
        try:
            Validation.validate_ids_presence("lfkj4", repo)
            assert False
        except Exception as e:
            assert str(e) == "ID not in list!"
        Validation.validate_ids_presence("lfkj3", repo)

    @staticmethod
    def test_repo_delete():
        per = Person("lfkj3", "Lucas", "alkjf")
        repo = Repository()
        repo.add(per)
        repo.delete(per.id())
        assert repo.items_by_id() == {}

    @staticmethod
    def test_repo_item_by_id():
        per = Person("lfkj3", "Lucas", "alkjf")
        repo = Repository()
        repo.add(per)
        assert repo.item_by_id("lfkj3") == per

    @staticmethod
    def test_modify_person():
        person = Person("skldf", "Lucas", "skdlhf")
        PeopleService.modify_person(person, new_name="Andrei")
        assert person == Person("skldf", "Andrei", "skdlhf")

    @staticmethod
    def test_modify_event():
        event = Event("yes", date(2026, 10, 10), time(10, 00), "yeah")
        EventService.modify_event(event, new_description="nah")
        assert event == Event("yes", date(2026, 10, 10), time(10, 00), "nah")

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
        Tests.test_repo_items_by_id()
        Tests.test_repo_items()
        Tests.test_repo_ids()
        Tests.test_repo_add()
        Tests.test_validate_person_name()
        Tests.test_validate_id_uniqueness()
        Tests.test_validate_ids_presence()
        Tests.test_repo_delete()
        Tests.test_repo_item_by_id()
        Tests.test_modify_person()
        Tests.test_modify_event()
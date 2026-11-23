import random
from Domain.domain import Person, Event, Attendance
from datetime import date, time
from Repository.repository import Repository, AttendanceRepository
from validate import Validation
from Service.service import PeopleService, EventService, AttendanceService


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
    def test_service_item_by_id():
        per = Person("lfkj3", "Lucas", "alkjf")
        repo = Repository()
        service = PeopleService(repo)
        service.add(per)
        assert service.item_by_id("lfkj3") == per

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
    def test_generate_random_string():
        random.seed(123)
        rand_id = PeopleService.generate_rand_string(True)
        random.seed(123)
        assert rand_id == PeopleService.generate_rand_string(True)

    @staticmethod
    def test_attendances_by_param():
        attendance_repo = AttendanceRepository()
        person = Person("1", "Lucas", "Sasar")
        person1 = Person("2", "Lucas", "Sasar")
        event = Event("1", date(2000,3,3), time(11,0), "jskdfh")
        event1 = Event("2", date(2000,3,3), time(11,0), "jskdfh")
        event2 = Event("3", date(2000,3,3), time(11,0), "jskdfh")
        attendance = Attendance(person, event)
        attendance2 = Attendance(person, event2)
        attendance3 = Attendance(person1, event)
        attendance4 = Attendance(person1, event2)
        attendance_repo.add(attendance)
        attendance_repo.add(attendance2)
        attendance_repo.add(attendance3)
        attendance_repo.add(attendance4)
        assert attendance_repo.attendances_by_param("2") == []
        assert attendance_repo.attendances_by_param("1") == [attendance, attendance3]
        assert attendance_repo.attendances_by_param("1", "person") == [attendance, attendance2]

    @staticmethod
    def test_delete_attendance_by_param():
        attendance_repo = AttendanceRepository()
        attendance_service = AttendanceService(attendance_repo)
        person = Person("1", "Lucas", "Sasar")
        person1 = Person("2", "Lucas", "Sasar")
        event = Event("1", date(2000,3,3), time(11,0), "jskdfh")
        event2 = Event("3", date(2000,3,3), time(11,0), "jskdfh")
        attendance = Attendance(person, event)
        attendance2 = Attendance(person, event2)
        attendance3 = Attendance(person1, event)
        attendance4 = Attendance(person1, event2)
        attendance_service.add(attendance)
        attendance_service.add(attendance2)
        attendance_service.add(attendance3)
        attendance_service.add(attendance4)
        attendance_service.delete_all_attendances_by_param("1")
        assert attendance_repo.items() == [attendance3, attendance4]
        attendance_service.delete_all_attendances_by_param("1", "event")
        assert attendance_repo.items() == [attendance4]

    @staticmethod
    def test_report_all_events_for_person_by_description_date():
        attendance_repo = AttendanceRepository()
        attendance_service = AttendanceService(attendance_repo)
        person = Person("1", "Lucas", "Sasar")
        person1 = Person("2", "Lucas", "Sasar")
        event = Event("1", date(2000, 3, 3), time(11, 0), "plm")
        event2 = Event("3", date(2000, 3, 3), time(11, 0), "pla")
        attendance = Attendance(person, event)
        attendance2 = Attendance(person, event2)
        attendance3 = Attendance(person1, event)
        attendance4 = Attendance(person1, event2)
        attendance_service.add(attendance)
        attendance_service.add(attendance2)
        attendance_service.add(attendance3)
        attendance_service.add(attendance4)
        assert attendance_service.report_all_events_for_person_by_description_date("1") == [event2, event]

    @staticmethod
    def test_first_k_items_by_criteria():
        attendance_repo = AttendanceRepository()
        attendance_service = AttendanceService(attendance_repo)
        person_repo = Repository()
        event_repo = Repository()
        person_service = PeopleService(person_repo)
        event_service = EventService(event_repo)
        person = Person("1", "Lucas", "Sasar")
        person1 = Person("2", "Lucas", "Sasar")
        person_service.add(person)
        person_service.add(person1)
        event = Event("1", date(2000, 3, 3), time(11, 0), "plm")
        event1 = Event("2", date(2000, 3, 3), time(11, 0), "plm")
        event2 = Event("3", date(2000, 3, 3), time(11, 0), "pla")
        event_service.add(event)
        event_service.add(event1)
        event_service.add(event2)
        attendance = Attendance(person, event)
        attendance2 = Attendance(person, event2)
        attendance3 = Attendance(person1, event)
        attendance4 = Attendance(person1, event2)
        attendance_service.add(attendance)
        attendance_service.add(attendance2)
        attendance_service.add(attendance3)
        attendance_service.add(attendance4)
        assert attendance_service.first_k_items_by_criteria(person_service, "person", 1) == [person]
        assert attendance_service.first_k_items_by_criteria(person_service, "person", 2) == [person, person1]
        assert attendance_service.first_k_items_by_criteria(event_service, "event", 1) == [event]
        assert attendance_service.first_k_items_by_criteria(event_service, "event", 2) == [event, event2]
        assert attendance_service.first_k_items_by_criteria(event_service, "event", 3) == [event, event2, event1]

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
        Tests.test_service_item_by_id()
        Tests.test_modify_person()
        Tests.test_modify_event()
        Tests.test_generate_random_string()
        Tests.test_attendances_by_param()
        Tests.test_delete_attendance_by_param()
        Tests.test_report_all_events_for_person_by_description_date()
        Tests.test_first_k_items_by_criteria()
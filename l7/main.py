from UI.ui import UI
from Repository.repository import Repository, AttendanceRepository
from Service.service import PeopleService, EventService, AttendanceService
from tests import Tests

if __name__ == "__main__":
    Tests.test_function()

    person_repo = Repository()
    event_repo = Repository()
    attendance_repo = AttendanceRepository()

    person_service = PeopleService(person_repo)
    event_service = EventService(event_repo)
    attendance_service = AttendanceService(attendance_repo)


    for i in range(20):
        person_service.add(person_service.generate_rand_person())
        event_service.add(event_service.generate_random_event())
    for i in range(5):
        attendance_service.add(attendance_service.generate_random_attendance(person_service.items(), event_service.items()))

    ui = UI(person_service, event_service, attendance_service)
    ui.run()


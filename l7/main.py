from UI.ui import UI
from Repository.repository import Repository
from Service.service import PeopleService, EventService
from Domain.domain import Person, Event
from tests import Tests

from datetime import date, time

if __name__ == "__main__":
    Tests.test_function()

    person_repo = Repository()
    event_repo = Repository()

    person_service = PeopleService(person_repo)
    event_service = EventService(event_repo)

    person_service.add(Person("1", "Lucas", "unnamed road, 38"))
    person_service.add(Person("24kkl4m", "Lucas", "unnamed road, 38"))
    person_service.add(Person("24kkl4n", "Lucas", "unnamed road, 38"))
    person_service.add(Person("24kkl4o", "Lucas", "unnamed road, 38"))
    person_service.add(Person("24kkl4p", "Lucas", "unnamed road, 38"))

    event_service.add(Event("skjf23", date(2026, 11, 13), time(10,0), "skdjflksdjf"))
    event_service.add(Event("skjf24", date(2026, 11, 13), time(10,0), "skdjflksdjf"))
    event_service.add(Event("skjf25", date(2026, 11, 13), time(10,0), "skdjflksdjf"))
    event_service.add(Event("skjf26", date(2026, 11, 13), time(10,0), "skdjflksdjf"))
    event_service.add(Event("skjf27", date(2026, 11, 13), time(10,0), "skdjflksdjf"))

    ui = UI(person_service, event_service)
    ui.run()


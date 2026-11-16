from UI.ui import UI
from Repository.repository import Repository
from Service.service import PeopleService, EventService
from tests import Tests

from datetime import date, time

if __name__ == "__main__":
    Tests.test_function()

    person_repo = Repository()
    event_repo = Repository()

    person_service = PeopleService(person_repo)
    event_service = EventService(event_repo)

    for i in range(20):
        person_service.add(person_service.generate_rand_person())
        event_service.add(event_service.generate_random_event())

    ui = UI(person_service, event_service)
    ui.run()


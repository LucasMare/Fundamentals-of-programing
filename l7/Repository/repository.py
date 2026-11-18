from validate import Validation

class Repository:
    """
    Class for the repository of the application
    """
    def __init__(self):
        self.__repo = {}

    def items_by_id(self) -> dict:
        """
        Method that returns a dictionary where the keys are the id's and the values are the objects
        :return:
        """
        return self.__repo

    def items(self) -> list:
        """
        Method that returns the list of objects
        :return:
        """
        return list(self.__repo.values())

    def ids(self) -> list:
        """
        Method that returns a list of all id's
        :return:
        """
        return list(self.__repo.keys())

    def add(self, element):
        """
        Method that adds an instance to the list
        :param element:
        :return:
        """
        Validation.validate_id_uniqueness(element, self, "This person is already attending this event!")
        self.items_by_id()[element.id()] = element

    def delete(self, object_id:str):
        """
        Method that deletes the object with a given id
        :param object_id:
        :return:
        """
        Validation.validate_ids_presence(object_id, self)
        del self.items_by_id()[object_id]

class AttendanceRepository(Repository):
    """
    Class for the attendances repositories
    """
    def attendances_by_param(self, search_id, criteria = "event"):
        """
        Method for getting all attendances with a certain person
        :param search_id:
        :param criteria:
        :return:
        """
        l = []
        for attendance in self.items():
            if criteria == "person":
                if search_id == attendance.person().id():
                    l.append(attendance)
            else:
                if search_id == attendance.event().id():
                    l.append(attendance)
        return l

    def delete_all_attendances_by_param(self, delete_by_id, criteria="person"):
        """
        Method for deleting all attendances for a person or event
        :param delete_by_id:
        :param criteria:
        :return:
        """
        for elem in self.attendances_by_param(delete_by_id, criteria):
            self.delete(elem.id())

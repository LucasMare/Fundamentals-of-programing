class Service:
    """
    Class for the service of the person and event lists
    """
    def __init__ (self, repository):
        self.__repo = repository

    def get_repo(self):
        """
        Method that returns the repository of the service object
        :return:
        """
        return self.__repo

    def add(self, person_or_event):
        """
        Method that adds an object to the repository
        :param person_or_event:
        :return:
        """
        self.get_repo().add(person_or_event)



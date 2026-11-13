class Repository:
    """
    Class for the repository of the application
    """
    def __init__(self):
        self.__list = {}

    def items_by_id(self) -> dict:
        """
        Method that returns a dictionary where the keys are the id's and the values are the objects
        :return:
        """
        return self.__list

    def items(self) -> list:
        """
        Method that returns the list of objects
        :return:
        """
        return list(self.__list.values())

    def ids(self) -> list:
        """
        Method that returns a list of all id's
        :return:
        """
        return list(self.__list.keys())

    def add(self, element):
        """
        Method that adds an instance to the list
        :param element:
        :return:
        """
        self.items_by_id()[element.id()] = element
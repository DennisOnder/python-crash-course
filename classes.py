# Classes & Objects
class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name == name
        self.__email == email
        return

    def set_name(self, name):
        self.__name == name
        return

    def set_email(self, email):
        self.__email == email
        return

    def get_name(self):
        print(self.__name)
        return

    def get_email(self):
        print(self.__email)
        return


dennis = Person('Dennis Onder', 'dennis@gmail.com')

dennis.get_name()

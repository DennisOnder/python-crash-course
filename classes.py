# Classes & Objects
class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name == name
        self.__email == email

    def set_name(self, name):
        self.__name == name

    def set_email(self, email):
        self.__email == email

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email


dennis = Person('Dennis Onder', 'dennis@gmail.com')
print(dennis.get_name())

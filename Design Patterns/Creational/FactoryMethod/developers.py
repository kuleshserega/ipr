from abc import ABCMeta, abstractmethod


class Developer(metaclass=ABCMeta):

    @abstractmethod
    def write_code(self):
        """Returns text with developer actions."""


class PhpDeveloper(Developer):

    def write_code(self):
        print('Php developer writes Php code...')


class PythonDeveloper(Developer):

    def write_code(self):
        print('Python developer writes Python code...')

class JsDeveloper(Developer):

    def write_code(self):
        print('Js developer writes Js code...')

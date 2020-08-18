from abc import ABCMeta, abstractmethod


class Developer(metaclass=ABCMeta):

    @abstractmethod
    def write_code(self):
        """Returns text developer writes code."""


class PhpDeveloper(Developer):

    def write_code(self):
        print('Php developer writes Php code...')


class PythonDeveloper(Developer):

    def write_code(self):
        print('Python developer writes Python code...')


class Tester(metaclass=ABCMeta):

    @abstractmethod
    def test_code(self):
        """Returns text tester tests code."""


class ManualTester(Tester):

    def test_code(self):
        print('Manual tester tests code...')


class AutoTester(Tester):

    def test_code(self):
        print('Auto tester tests code...')


class Manager(metaclass=ABCMeta):

    @abstractmethod
    def manage_project(self):
        """Returns text manager manages project."""


class BankingSiteManager(Manager):

    def manage_project(self):
        print('Banking site manager manages banking site project...')


class CmsSiteManager(Manager):

    def manage_project(self):
        print('Cms site manager manages cms site project...')

from abc import ABCMeta, abstractmethod

from developers import PhpDeveloper, PythonDeveloper, JsDeveloper


class DeveloperFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_developer(self):
        """Returns developer."""


class PhpDeveloperFactory(DeveloperFactory):

    def create_developer(self):
        return PhpDeveloper()


class PythonDeveloperFactory(DeveloperFactory):

    def create_developer(self):
        return PythonDeveloper()


class JsDeveloperFactory(DeveloperFactory):

    def create_developer(self):
        return JsDeveloper()

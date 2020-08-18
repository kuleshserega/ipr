from abc import ABCMeta, abstractmethod

from workers import (PhpDeveloper, PythonDeveloper,
                     ManualTester, AutoTester,
                     BankingSiteManager, CmsSiteManager)


class TeamFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def get_developer(self):
        """Returns developer."""

    @abstractmethod
    def get_tester(self):
        """Returns tester."""

    @abstractmethod
    def get_manager(self):
        """Returns manager."""


class BankingTeamFactory(TeamFactory):

    def get_developer(self):
        return PhpDeveloper()

    def get_tester(self):
        return ManualTester()

    def get_manager(self):
        return BankingSiteManager()


class CmsTeamFactory(TeamFactory):

    def get_developer(self):
        return PythonDeveloper()

    def get_tester(self):
        return AutoTester()

    def get_manager(self):
        return CmsSiteManager()

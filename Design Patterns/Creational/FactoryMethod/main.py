from developer_factories import (PhpDeveloperFactory, PythonDeveloperFactory,
                                 JsDeveloperFactory)


class Website:
    developer = None

    def __init__(self):
        self.developer_factory = self._get_developer_factory('Python1')
        if self.developer_factory:
            self.developer = self.developer_factory.create_developer()

    def _get_developer_factory(self, developer_type):
        return {
            'Php': PhpDeveloperFactory(),
            'Python': PythonDeveloperFactory(),
            'Js': JsDeveloperFactory(),
        }.get(developer_type.lower(), None)

    def run_process(self):
        """Creating site process."""
        if self.developer:
            self.developer.write_code()

        print('There is no such developer type.')


if __name__ == '__main__':
    website = Website()
    website.run_process()

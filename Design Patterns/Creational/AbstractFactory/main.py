from site_factories import BankingTeamFactory, CmsTeamFactory


class WebsiteProject:

	def __init__(self):
		self.team_factory = BankingTeamFactory()

	def development_process(self):
		self.developer = self.team_factory.get_developer()
		self.tester = self.team_factory.get_tester()
		self.manager = self.team_factory.get_manager()

		print('Website creation process...')

		self.developer.write_code()
		self.tester.test_code()
		self.manager.manage_project()


if __name__ == '__main__':
	project = WebsiteProject()
	project.development_process()

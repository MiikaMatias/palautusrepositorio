from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_data = toml.loads(content)


        poetry_data = parsed_data['tool']['poetry']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetry_data['name'], poetry_data['description'], 
                       poetry_data['license'], poetry_data['authors'], 
                       poetry_data['dependencies'],
                       poetry_data['group']['dev']['dependencies'])

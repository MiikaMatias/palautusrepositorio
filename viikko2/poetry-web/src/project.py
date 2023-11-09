class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"


    def __str__(self):
        return f"""
Name: {self.name}
Description: {self.description}
License: {self.license}

Authors:
- {self._stringify_dependencies(self.authors)}

Dependencies: 
- {self._stringify_dependencies(self.dependencies)}

Development dependencies: 
- {self._stringify_dependencies(self.dev_dependencies)}
        """

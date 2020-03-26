from typing import List


class ReferencesDataSource:
    """
    Loads references from a text file
    """

    def __init__(self, path: str):
        self.path = path

    def transform(self) -> List[List[str]]:
        with open(self.path) as file:
            recids = file.readlines()
            recids = [line.strip("\n").split(",") for line in recids]
        return recids
import json
from re import U
import requests

class Creature:
    def __init__(self, json) -> None:
        pass

class Creatures:
    def __init__(self) -> None:
        url = "https://www.dnd5eapi.co/api/monsters"
        r = requests.get(url)
        self.data = json.loads(r.text)
        self.data = self.data["results"]
        url = "https://www.dnd5eapi.co/api/races"
        r = requests.get(url)
        races = json.loads(r.text)
        races = races["results"]

        self.data.extend(races)

    


if __name__ == "__main__":
    c = Creatures()
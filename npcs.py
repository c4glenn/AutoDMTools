import spacy

from fantasyNameGen import FantasyNameGen


gen = FantasyNameGen()

class NPC:
    def __init__(self) -> None:
        pass

class NPCFactory:
    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_trf")
    def generateFromDescription(self, description):
        self.description = description
        doc = self.nlp(self.description)
        for token in doc:
            print(token.text, "|", token.pos_, "|", token.dep_)
        print(self.description)


if __name__ == "__main__":
    descriptions = ["middle aged dwarf", "tall male elf", "goblin fellow who loves gold"]
    factory = NPCFactory()
    for description in descriptions:
        factory.generateFromDescription(description)
from operator import truediv
from random import Random, random
from re import T


class FantasyNameGen:
    def __init__(self) -> None:
        self.symbols = {
            "s":["ach", "ack", "ad", "age", "ald", "ale", "an", "ang", "ar", "ard",
				"as", "ash", "at", "ath", "augh", "aw", "ban", "bel", "bur", "cer",
				"cha", "che", "dan", "dar", "del", "den", "dra", "dyn", "ech", "eld",
				"elm", "em", "en", "end", "eng", "enth", "er", "ess", "est", "et",
				"gar", "gha", "hat", "hin", "hon", "ia", "ight", "ild", "im", "ina",
				"ine", "ing", "ir", "is", "iss", "it", "kal", "kel", "kim", "kin",
				"ler", "lor", "lye", "mor", "mos", "nal", "ny", "nys", "old", "om",
				"on", "or", "orm", "os", "ough", "per", "pol", "qua", "que", "rad",
				"rak", "ran", "ray", "ril", "ris", "rod", "roth", "ryn", "sam",
				"say", "ser", "shy", "skel", "sul", "tai", "tan", "tas", "ther",
				"tia", "tin", "ton", "tor", "tur", "um", "und", "unt", "urn", "usk",
				"ust", "ver", "ves", "vor", "war", "wor", "yer"],
            "v": ["a", "e", "i", "o", "u", "y"],
            "V": ["a", "e", "i", "o", "u", "y", "ae", "ai", "au", "ay", "ea", "ee",
				"ei", "eu", "ey", "ia", "ie", "oe", "oi", "oo", "ou", "ui"],
            "c": ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
				"s", "t", "v", "w", "x", "y", "z"],
            "B": ["b", "bl", "br", "c", "ch", "chr", "cl", "cr", "d", "dr", "f", "g",
				"h", "j", "k", "l", "ll", "m", "n", "p", "ph", "qu", "r", "rh", "s",
				"sch", "sh", "sl", "sm", "sn", "st", "str", "sw", "t", "th", "thr",
				"tr", "v", "w", "wh", "y", "z", "zh"],
            "C": ["b", "c", "ch", "ck", "d", "f", "g", "gh", "h", "k", "l", "ld", "ll",
				"lt", "m", "n", "nd", "nn", "nt", "p", "ph", "q", "r", "rd", "rr",
				"rt", "s", "sh", "ss", "st", "t", "th", "v", "w", "y", "z"],
            "i": ["air", "ankle", "ball", "beef", "bone", "bum", "bumble", "bump",
				"cheese", "clod", "clot", "clown", "corn", "dip", "dolt", "doof",
				"dork", "dumb", "face", "finger", "foot", "fumble", "goof",
				"grumble", "head", "knock", "knocker", "knuckle", "loaf", "lump",
				"lunk", "meat", "muck", "munch", "nit", "numb", "pin", "puff",
				"skull", "snark", "sneeze", "thimble", "twerp", "twit", "wad",
				"wimp", "wipe"],
            "m": ["baby", "booble", "bunker", "cuddle", "cuddly", "cutie", "doodle",
				"foofie", "gooble", "honey", "kissie", "lover", "lovey", "moofie",
				"mooglie", "moopie", "moopsie", "nookum", "poochie", "poof",
				"poofie", "pookie", "schmoopie", "schnoogle", "schnookie",
				"schnookum", "smooch", "smoochie", "smoosh", "snoogle", "snoogy",
				"snookie", "snookum", "snuggy", "sweetie", "woogle", "woogy",
				"wookie", "wookum", "wuddle", "wuddly", "wuggy", "wunny"],
            "M": ["boo", "bunch", "bunny", "cake", "cakes", "cute", "darling",
				"dumpling", "dumplings", "face", "foof", "goo", "head", "kin",
				"kins", "lips", "love", "mush", "pie", "poo", "pooh", "pook", "pums"],
            "D": ["b", "bl", "br", "cl", "d", "f", "fl", "fr", "g", "gh", "gl", "gr",
				"h", "j", "k", "kl", "m", "n", "p", "th", "w"],
            "d": ["elch", "idiot", "ob", "og", "ok", "olph", "olt", "omph", "ong",
				"onk", "oo", "oob", "oof", "oog", "ook", "ooz", "org", "ork", "orm",
				"oron", "ub", "uck", "ug", "ulf", "ult", "um", "umb", "ump", "umph",
				"un", "unb", "ung", "unk", "unph", "unt", "uzz"]
        }

    def literalProcess(self, character, segment, literal):
        if(character == "|"):
            segment.append(segment[0])
            segment[0] = ""
        elif(character == '('):
            literal += 1
            segment.append(segment[0])
            segment[0] = ""
        elif(character != ")"):
            segment[0] += character
        else:
            literal -= 1
            word = Random().choice(segment)
            segment = [word]

        return(segment, literal)
    
    def generate(self, pattern):
        word = ""
        segment = [""]
        literal = 0
        special = 0
        for character in pattern:
            if(special):
                if(literal):
                    (segment, literal) = self.literalProcess(character, segment, literal)
                else:
                    match character:
                        case '(':
                            literal += 1
                        case '|':
                            segment.append(segment[0])
                            segment[0] = ""
                        case '>':
                            special -= 1
                        case _:
                            segment[0] += Random().choice(self.symbols[character])
            else:
                match character:
                    case '(':
                        special += 1
                        literal += 1
                    case '<':
                        special += 1
                    case _:
                        word += Random().choice(self.symbols[character])
        word += segment[0]
        return word

if __name__ == "__main__":
    f = FantasyNameGen()
    patterns = ["<dD|ss>", "<V|VCV|((a|e)i)>", "(r|(s|t))"]
    for pattern in patterns:
        print(f.generate(pattern))
    
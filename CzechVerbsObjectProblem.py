# Verbs have several pieces
# 1. Dictionary entry - být, mít, učít se
# 2. Stripped version - být, mít, učít
# 3. Present base - j, m, uč


class Verb:
    def __init__(self, name):
        self.name = name
        self.reflexivePart = None
        if self.name[-3:] in [' se', ' si']:
            self.stripped = name[0:-3]
            self.reflexivePart = name[-2:]
        else:
            self.stripped = name


    def getConjugation(self, person):
        ending = self.conjugationEndings.get(person, None);
        return self.base + ending if ending else None

    def printConjugation(self):
        for person in ['1s', '2s', '3s', '1p', '2p', '3p']:
            line = person + ' ' + self.getConjugation(person)
            alt = person + 'a'
            if alt in self.conjugationEndings:
                alternateConjugations = []
                for ending in self.conjugationEndings[alt]:
                    alternateConjugations.append(self.base + ending)
                line = line + '[' + ' '.join(alternateConjugations) + ']'
            if self.reflexivePart is not None:
                line = line + ' ' + self.reflexivePart
            print(line)
        print()

    def isReflexive(self):
        if self.reflexivePart is None:
            print('NOT reflexive')
        else:
            print('Reflexive! ' + self.reflexivePart)


class Verb_í_plain(Verb):
    def __init__(self, name, base=None):
        Verb.__init__(self, name)
        if base is None:
            self.base = self.name[:-2]
        else:
            self.base = base
        self.conjugationEndings = {
            '1s': 'ím',
            '2s': 'íš',
            '3s': 'í',
            '1p': 'íme',
            '2p': 'íte',
            '3p': 'í',
        }


class Verb_í(Verb_í_plain):
    def __init__(self, name, base=None):
        Verb_í_plain.__init__(self, name, base)
        self.conjugationEndings['3pa'] = ['éjí']


# "bát se" (to be afraid): bojím se, bojíš se, bojí se, bojíme se, bojíte se, bojí se

verbs = []
verbs.append(Verb_í_plain('spát'))
# "spát" (to sleep): spím, spíš, spí, spíme, spíte, spí
verbs.append(Verb_í_plain('stát', 'stoj'))
# "stát" (to stand, to cost): stojím, stojíš, stojí, stojíme, stojíte, stojí
verbs.append(Verb_í('rozumět'))
verbs.append(Verb_í_plain('bát se', 'boj'))

for verb in verbs:
    verb.print_conjugation()

myVerb6 = Verb_í_plain('bát se', 'boj')
#myVerb6.printConjugation()
#myVerb6.isReflexive()
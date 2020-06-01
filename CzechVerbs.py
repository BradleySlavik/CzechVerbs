# Verbs have several pieces
# 1. Dictionary entry - být, mít, učít se
# 2. Stripped version - být, mít, učít
# 3. Present base - j, m, uč

from abc import ABC

CONSONANTS = 'bcčdďfghklmnňprřsštťvwxzž'

# Conjugate verb from base and endings, pre-conjugated forms take precedence


class Verb(ABC):
    """ This is an abstract class. Do NOT try to instantiate it."""

    def __init__(self, name, base):
        self.name = name
        self.base = base
        self.conjugated = False
        self.conjugation = {}
        self.endings = None
        self.imperative = {}
        self.imperative_with_háček = False
        self.reflexivePart = None
        if self.name[-3:] in [' se', ' si']:
            self.stripped = name[0:-3]
            self.reflexivePart = name[-2:]
        else:
            self.stripped = name

    def conjugate_present(self):
        base = getattr(self, 'base_present_tense', self.base)
        for person in ['1s', '2s', '3s', '1p', '2p', '3p']:
            line = None
            if person not in self.conjugation:
                self.conjugation[person] = ''
                if person in self.endings:
                    self.conjugation[person] = base + self.endings[person]
            alt_person = person + 'a'
            if alt_person not in self.conjugation and alt_person in self.endings:
                self.conjugation[alt_person] = base + self.endings[alt_person]

    def conjugate_imperative(self):
        print('Imperative')
        if self.base[:-1] in CONSONANTS:
            if self.base[-2:-1] in CONSONANTS:
                self.imperative['2s'] = self.base + 'i'
                if self.imperative_with_háček:
                    self.imperative['1p'] = self.base + 'ěme'
                    self.imperative['2p'] = self.base + 'ěte'
                else:
                    self.imperative['1p'] = self.base + 'eme'
                    self.imperative['2p'] = self.base + 'ete'
            else:
                imp_base = self.base
                if self.base[-1:] == 'd':
                    imp_base = self.base[:-1] + 'ď'
                elif self.base[-1:] == 'n':
                    imp_base = self.base[:-1] + 'ň'
                elif self.base[-1:] == 't':
                    imp_base = self.base[:-1] + 'ť'
                self.imperative['1p'] = imp_base
                self.imperative['1p'] = imp_base + 'me'
                self.imperative['2p'] = imp_base + 'te'
        else:
            print('How to conjugate base ending in vowel?')

    def print_imperative(self):
        print('Imperative')
        for person in ['2s', '1p', '2p']:
            print('{}: {}'.format(person, self.imperative[person]))

    def print_conjugation(self):
        print(self.name)
        for person in ['1s', '2s', '3s', '1p', '2p', '3p']:
            line = person + ' ' + self.conjugation[person]
            alt = person + 'a'
            if alt in self.conjugation:
                line = line + '[' + self.conjugation[alt] + ']'
            if self.reflexivePart is not None:
                line = line + ' ' + self.reflexivePart
            print(line)
        print()

    def is_reflexive(self):
        if self.reflexivePart is None:
            print('NOT reflexive')
        else:
            print('Reflexive! ' + self.reflexivePart)


class Verb_a(Verb):
    """-A verbs (dĕlat, , , mít)"""
    def __init__(self, name, base=None):
        Verb.__init__(self, name, base)
        if base is None:
            self.base = self.name[:-2]
        self.endings = {
            '1s': 'ám',
            '2s': 'áš',
            '3s': 'á',
            '1p': 'áme',
            '2p': 'áte',
            '3p': 'ají',
        }
        self.conjugate()

    def print_imperative(self):
        print('Imperative')
        print('2s:{}'.format(self.base + 'ej'))
        print('1p:{}'.format(self.base + 'ejme'))
        print('2p:{}'.format(self.base + 'ejte'))


class Verb_i(Verb):
    """These are the í verbs"""

    def __init__(self, name, base=None):
        Verb.__init__(self, name, base)
        if base is None:
            self.base = self.name[:-2]
        self.endings = {
            '1s': 'ím',
            '2s': 'íš',
            '3s': 'í',
            '1p': 'íme',
            '2p': 'íte',
            '3p': 'í',
        }
        self.conjugate()

class Verb_i2(Verb_i):
    def __init__(self, name, base=None):
        Verb_i.__init__(self, name, base)
        self.endings['3pa'] = 'ějí'
        self.conjugate()


class Verb_ovat(Verb):
    """-ovat verbs"""
    def __init__(self, name, base=None):
        Verb.__init__(self, name, base)
        if base is None:
            self.base = self.name[:-4]
        self.endings = {
            '1s': 'uju',
            '1sa': 'uji',
            '2s': 'uješ',
            '3s': 'uje',
            '1p': 'ujeme',
            '2p': 'ujete',
            '3p': 'ujou',
            '3pa': 'ují',
        }
        self.conjugate()


class Verb_e(Verb):
    def __init__(self, name, base):
        Verb.__init__(self, name, base)
        self.endings = {
            '1s': 'u',
            '2s': 'eš',
            '3s': 'e',
            '1p': 'eme',
            '2p': 'ete',
            '3p': 'ou',
        }
        self.conjugate()


class Verb_nout(Verb_e):
    def __init__(self, name, base=None):
        if base is None:
            self.base = self.name[:-3]
        Verb_e.__init__(self, name, base)


class Verb_brát(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'brát', 'ber')


class Verb_číst(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'číst', 'čt')
        self.conjugate()


class Verb_krást(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'krást', 'krad')
        self.conjugate()


class Verb_nést(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'nést', 'nes')
        self.conjugate()


class Verb_vést(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'vést', 'ved')
        self.conjugate()


class Verb_vézt(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'vézt', 'vez')
        self.conjugate()


class Verb_jet(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'jet', 'jed')
        self.conjugate()


class Verb_jít(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'jít', 'jd')
        self.conjugate()


class Verb_moci(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'moci[moct]', 'muž')
        self.conjugation['1sa'] = 'mohu'
        self.conjugation['3pa'] = 'mohou'


class Verb_péci(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'péci', 'peč')


class Verb_přemoci(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'přemoci[přemoct]', 'přemuž')
        self.conjugation['1sa'] = 'přemohu'
        self.conjugation['3pa'] = 'přemohou'


class Verb_hnát(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'hnát', 'žen')


class Verb_lhat(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'lhat', 'lž')


class Verb_mlít(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'mlít', 'mel')


class Verb_plakat(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'plakat', 'plač')


class Verb_poslat(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'poslat', 'pošl')


class Verb_třít(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'třít', 'tř')


class Verb_vázat(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'vázat', 'váž')


class Verb_zvát(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'brát', 'zv')


class Verb_česat(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'česat', 'češ')
        # Need to account for BOTH conjugations


class Verb_minout(Verb_nout):
    def __init__(self):
        Verb_e.__init__(self, 'minout', 'min')


class Verb_stihnout(Verb_nout):
    def __init__(self):
        Verb_e.__init__(self, 'stihnout', 'stihn')


class Verb_tisknout(Verb_nout):
    def __init__(self):
        Verb_e.__init__(self, 'tisknout', 'tiskn')


class Verb_zapomenout(Verb_nout):
    def __init__(self):
        Verb_e.__init__(self, 'zapomenout', 'zapom')
        # add en before basic conjugation
        self.base_present_tense = 'zapomen'


class Verb_říci(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'říci', 'řekn')


class Verb_dostat(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'dostat', 'dostan')


class Verb_vstát(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'vstát', 'vstan')


class Verb_začít(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'začít', 'začn')


class Verb_najmout(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'najmout', 'najm')


class Verb_vzít(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'vzít', 'vezm')

class Verb_krýt(Verb_e):
    def __init__(self):
        Verb_e.__init__(self, 'krýt', 'kryj')



class Verb2(Verb):
    def __init__(self, name, base=None):
        super(Verb2, self).__init__(name, base)
        if base is None:
            self.base = self.name[:-3]
        self.endings = {
            '1s': 'u',
            '2s': 'eš',
            '3s': 'e',
            '1p': 'eme',
            '1pa': 'em',
            '2p': 'ete',
            '3p': 'ou',
        }
        self.conjugate()


# "bát se" (to be afraid): bojím se, bojíš se, bojí se, bojíme se, bojíte se, bojí se


class Verb_být(Verb):
    """být has its own pattern"""

    def __init__(self, name):
        Verb.__init__(self, name, None)
        self.base = 'j'
        self.endings = {
            '1s': 'sem',
            '2s': 'si',
            '2sa': 'seš',
            '3s': 'e',
            '1p': 'sme',
            '2p': 'ste',
            '3p': 'sou',
        }
        self.conjugate()


class Verb_chtít(Verb):
    def __init__(self, name):
        Verb.__init__(self, name, None)
        self.base = 'chc'
        self.endings = {
            '1s': 'i',
            '2s': 'eš',
            '3s': 'e',
            '1p': 'eme',
            '1pa': 'em',
            '2p': 'ete',
            '3p': 'ějí',
        }
        self.conjugate()


class Verb_jíst(Verb):
    """jíst (to eat): jím, jíš, jí, jíme, jíte, jí (or jedí)"""

    def __init__(self, name):
        Verb.__init__(self, name, None)
        self.name = name
        self.base = 'j'
        self.endings = {
            '1s': 'ím',
            '2s': 'iš',
            '3s': 'í',
            '1p': 'íme',
            '2p': 'íte',
            '3p': 'edí',
            '3pa': 'í',
        }
        self.conjugate()


class Verb_mýt(Verb):
    def __init__(self, name, base):
        Verb.__init__(self, name, base)
        # self.base = 'myj'
        self.endings = {
            '1s': 'i',
            '1sa': 'u',
            '2s': 'eš',
            '3s': 'e',
            '1p': 'eme',
            '2p': 'ete',
            '3p': 'í',
            '3pa': 'ou',
        }
        self.conjugate()


class Verb_pít(Verb):
    def __init__(self, name):
        Verb.__init__(self, name, None)
        self.base = 'pij'
        self.endings = {
            '1s': 'u',
            '1sa': 'i',
            '2s': 'eš',
            '3s': 'e',
            '1p': 'eme',
            '2p': 'ete',
            '3p': 'ou',
            '3pa': 'í',
        }
        self.conjugate()
        # Add the i's in as a mixin for limited verbs


class Verb_psát(Verb):
    def __init__(self, name):
        Verb.__init__(self, name, None)
        self.base = 'píš'
        self.endings = {
            '1s': 'u',
            '1sa': 'i',
            '2s': 'eš',
            '3s': 'e',
            '1p': 'eme',
            '2p': 'ete',
            '3p': 'ou',
            '3pa': 'í',
        }
        self.conjugate()


class Verb_vědět(Verb):
    def __init__(self, name):
        Verb.__init__(self, name, None)
        self.base = 'v'
        self.endings = {
            '1s': 'ím',
            '2s': 'iš',
            '3s': 'í',
            '1p': 'íme',
            '2p': 'íte',
            '3p': 'í',
            '3pa': 'ědí',
        }
        self.conjugate()




# Can be combined with correct initialization



myVerb5a = Verb_být('být')
myVerb5b = Verb_chtít('chtít')
myVerb5c = Verb_e('číst', 'čt')
myVerb5d = Verb_pít('pít')

i_verbs = []

verbs = []
verbs.append(Verb_a('dělát'))
verbs.append(Verb_i('rozumět'))
verbs.append(Verb_ovat('tancovat'))

verbs.append(Verb_i2('bát se', 'boj'))
verbs.append(Verb_i2('spát'))
# "spát" (to sleep): spím, spíš, spí, spíme, spíte, spí
verbs.append(Verb_i2('stát', 'stoj'))
# "stát" (to stand, to cost): stojím, stojíš, stojí, stojíme, stojíte, stojí

verbs.append(Verb_e('brát', 'ber'))
verbs.append(Verb_e('hrát', 'hraj'))
verbs.append(Verb_e('jít', 'jd'))
verbs.append(Verb_e('jet', 'jed'))
verbs.append(Verb_e('lhát', 'lž'))
verbs.append(Verb_e('lít', 'lej'))
verbs.append(Verb_moci())
verbs.append(Verb_mýt('mýt', 'myj'))
verbs.append(Verb_e('nést', 'nes'))
verbs.append(Verb_e('plavat', 'plav'))
verbs.append(Verb_e('řít', 'řekn'))
verbs.append(Verb_e('růst', 'rost'))
verbs.append(Verb_i('sedět', 'sed'))
verbs.append(Verb_e('stát se', 'stan'))
verbs.append(Verb_e('vzít', 'vezm'))
verbs.append(Verb_mýt('žít', 'žij'))

for verb in verbs:
    verb.print_conjugation()


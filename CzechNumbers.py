# Cardinal numbers
# Ordinal numbers
# Clock time
#   Digital clock
#   24 hr by quarters
#   Starts at
# Dates

rod = {
    'mz': 'mužské životné',
    'mn': 'mužské neživotné',
    'f': 'femininum',
    'n': 'neutrum'
}

pád = {
    1: 'nominativ',
    2: 'genitiv',
    3: 'dativ',
    4: 'akusativ',
    5: 'vokativ',
    6: 'lokál',
    7: 'instrumentál'
}

# jednotné číslo, množné číslo
číslo = [ 'singulár', 'plurál']

one = {
    'singulár':
        {
            'rod': ['mz', 'mn', 'n', 'f'],
            1: ['jeden', 'jeden', 'jedno', 'jedna'],
            2: ['jednoho'] * 3 + ['jedné'],
            3: ['jednomu'] * 3 + ['jedné'],
            4: ['jednoho', 'jeden', 'jedno', 'jednu'],
            6: ['jednom'] * 3 + ['jedné'],
            7: ['jedním'] * 3 + ['jednou']
        },
    'plurál':
        {
            'rod': ['mz', 'mn', 'f', 'n'],
            1: ['jedni', 'jedny', 'jedny', 'jedna'],
            2: ['jedněch'] * 4,
            3: ['jedněm'] * 4,
            4: ['jedny'] * 3 + ['jedna'],
            6: ['jedněch'] * 4,
            7: ['jedněmi'] * 4,
        }
}


def decline_one(one_dict):
    one_declined = {}
    for number in one_dict:
        one_declined[number] = {}
        genders = one_dict[number]['rod']
        for case in one_dict[number]:
            if 'rod' == case:
                continue
            # for gender in genders:
            one_declined[number][case] = {}
            for i, form in enumerate(one_dict[number][case]):
                # print('N:{} G:{} i:{} Case:{} form:{}'.format(number, genders[i], i, case, form))
                one_declined[number][case][genders[i]] = form
    return one_declined


two = {
    'rod': ['mz', 'mn', 'n', 'f'],
    1: ['dva'] * 2 + ['dvě'] * 2,
    2: ['dvou'] * 4,
    3: ['dvěma'] * 4,
    4: ['dva'] * 2 + ['dvě'] * 2,
    6: ['dvou'] * 4,
    7: ['dvěma'] * 4,
}

three = {
    1: 'tři',
    2: 'tři',
    3: 'třem',
    4: 'tři',
    6: 'třech',
    7: 'třemi',
}

four = {
    1: 'čtyři',
    2: 'čtyř',
    3: 'čtyřem',
    4: 'čtyři',
    6: 'čtyřech',
    7: 'čtyřmi',
}

usual_suffix = {
    1: '',
    2: 'i',
    3: 'i',
    4: '',
    6: 'i',
    7: 'i',
}

hundred = {
    'čislo': {'singulár', 'plurál', 'dual'},
    1: ['sto', 'sta', 'stě'],
    2: ['sta', 'set', 'set'],
    3: ['stu', 'stům', 'stům'],
    4: ['sto', 'sta', 'stě'],
    6: ['stu', 'stech', 'stech'],
    7: ['stem', 'sty', 'sty'],
}

# MI - used for tisic
stroj = {
    1: ['', 'e'],
    2: ['e', 'ů'],
    3: ['i', 'ům'],
    4: ['', 'e'],
    5: ['i', 'e'],
    6: ['i', 'ich'],
    7: ['em', 'i']
}

# MI used for milion and milliard
telefon = {
    1: ['', 'y'],
    2: ['u', 'ů'],
    3: ['u', 'ům'],
    4: ['', 'y'],
    5: ['e', 'y'],
    6: ['u', 'ech'],
    7: ['em', 'y']
}


def construct_numer():
    pass


def decline_noun():
    pass


card_one_declined = decline_one(one)
print(card_one_declined)

from LanguageUtilities import *
import unicodedata
import math

#  Format the text ( uppercase, accents, ... )
def format(text):
    global alphabet
    try:
        str(text)
        text = remove_accents(text)
        text = text.upper()
        ntext = ""
        for letter in text:
            if letter not in alphabet:
                continue
            ntext += letter
        return ntext.upper()
    except:
        return False

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


#  Output a bloc of data with spaces
def output_encoded(encoded, letterblock=16, lignblock=8, maxlines=6):
    maximum = letterblock * lignblock * maxlines
    for index, letter in enumerate(encoded):
        if index == 0:
            print("\n" + letter, end="")
            continue
        if index % maximum == 0:
            print("\nReached max characters output ({0}), {1} chars left\n".format(maximum, len(encoded) - maximum))
            return
        if index % (letterblock * lignblock) == 0:
            print("")
        elif index % letterblock == 0:
            print(" ", end="")
        print(letter, end="")
    print("")


#  Find the next letter in the alphabet
def next_letter(letter, step):
    global alphabet
    ind = alphabet.index(letter)
    if ind + step >= len(alphabet):
        ind -= len(alphabet)
    elif ind + step < 0:
        ind += len(alphabet)
    return alphabet[ind + step]
    

# Add two letters in the alpahbet to make a new one
def add_letters(l1, l2, add=True):
    global alphabet
    index1, index2 = alphabet.find(l1), alphabet.find(l2)
    if add:
        index = (index1 + index2) % 26
    else:
        index = (index1 - index2 + 26) % 26
    return alphabet[index]


#  Find all repeated sequences in the given text
def find_double(message, len_min=4):
    positions = {}
    doubles = {}
    
    for mess_pos, char in enumerate(message):
        cut_part = message[mess_pos:mess_pos + len_min]
        if cut_part in positions.keys():
            positions[cut_part].append(mess_pos)
        else:
            positions[cut_part] = [mess_pos]
    for position in positions:
        if len(positions[position]) >= 2:
            doubles[position] = positions[position]
    return doubles


#  Returns all factors of a number
def all_factors(n):
    maximum = round(math.sqrt(n))
    factors = []
    for number in range(1, maximum+1):
        if n % number == 0:
            factors += [number, n // number]
    highests = list(filter(lambda x: x < maximum and not x == 1, factors))
    if len(highests) > 1:
        factors += [highests[-1]]
    return factors


#  Automatically find the offset of a text with its language
def find_decal(message, language_code="fr"):
    global alphabet
    if language_code not in letters_presence.keys():
        raise ValueError('Language requested not in array.')
    most_common = letters_presence[language_code]
    frequences = {}
    for index, letter in enumerate(message):
        if letter in frequences.keys():
            frequences[letter] += 1
        else:
            frequences[letter] = 1
    max_key = max(frequences, key=frequences.get)
    pourcentage_presence = round(frequences[max_key] / sum([frequences[i] for i in frequences]) * 100, 2) 
    verified = pourcentage_presence > most_common[1]
    return (alphabet.index(max_key) + len(alphabet) - alphabet.index(most_common[0])) % len(alphabet), verified
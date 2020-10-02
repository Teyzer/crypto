import unicodedata
import EncodeUtilities
from LanguageUtilities import *

first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

class Cesar:
    
    @staticmethod
    def encode(text, step):
        text = EncodeUtilities.format(text)
        encoded = ""
        for letter in text:
            encoded += EncodeUtilities.next_letter(letter, step)
        return encoded
        
    
    @staticmethod
    def decode(text, step=False):
        if not step:
            return Cracker.cesar(text)
        return Cesar.encode(text, step * -1)


class Vigenere:
    
    @staticmethod
    def encode(text, key):
        text = EncodeUtilities.format(text)
        nkey = EncodeUtilities.format(Vigenere.fit_key_len(len(text), key))
        ntext = ""
        for index in range(len(text)):
            ntext += EncodeUtilities.add_letters(text[index], nkey[index])
        return ntext
        
        
    @staticmethod
    def fit_key_len(textlen, key):
        up_to = textlen // len(key)
        end = textlen % len(key)
        if up_to < 0:
            up_to = 0
        return key * up_to + key[:end]
        
        
    @staticmethod
    def decode(text, key=False, language_targetted="fr", output=False):
        text = EncodeUtilities.format(text)
        if not key: # if not any key is given, calls the crack method
            return Cracker.vigenere(text, language_targetted, output)
        nkey = EncodeUtilities.format(Vigenere.fit_key_len(len(text), key))
        ntext = ""
        for index in range(len(text)):
            ntext += EncodeUtilities.add_letters(text[index], nkey[index], False)
        return ntext


class Cracker:

    @staticmethod
    def cesar(encrypted, language="fr"):
        offset = EncodeUtilities.find_decal(encrypted, language)
        return Cesar.decode(encrypted, offset[0])

    @staticmethod
    def vigenere(encrypted, language_targetted, output=False):

        global alphabet
        if output:
            print("Language choosed : {0}".format(language_targetted.upper()))

        doubles = EncodeUtilities.find_double(encrypted) #  Find all repeated sequences
        key_len = Cracker.find_key_len(doubles) #  Deduce the len of the key

        splitted = Cracker.split_message(encrypted, key_len) #  Split the message in {key_len} parts
        key = ""
        for index, split in enumerate(splitted):
            result = EncodeUtilities.find_decal(split, language_targetted) #  Perform a cesar attack on each one of these splitted parts
            if output:
                if (result[1]):
                    print("Obtained {0} with a rate in the normal range for choosen language".format(alphabet[result[0]]))
                else:
                    print("Obtained {0} with a rate sligthy smaller than the one of the chossen language".format(alphabet[result[0]]))
            key += alphabet[result[0]]

        if output:
            print("\nKey : {0}".format(key))

        return Vigenere.decode(encrypted, key), key


    @staticmethod
    def find_key_len(array_doubles, max_key_len=30):
        global first_primes
        factors = {}
        for double in array_doubles:
            for factor in EncodeUtilities.all_factors(array_doubles[double][1] - array_doubles[double][0]):
                if factor <= 1 or factor > max_key_len:
                    continue
                if not factor in factors.keys():
                    factors[factor] = 1
                else:
                    factors[factor] += 1
        return max(factors, key=factors.get)

    
    @staticmethod
    def split_message(message, key_len):
        splitted = []
        for index, char in enumerate(message):
            if len(splitted) <= index % key_len:
                splitted.append(char)
            else:
                splitted[index % key_len] += char
        return splitted
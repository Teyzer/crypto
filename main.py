from crypt import *

""" 
FROMAGER PACOME
NSI @2020 - MR LEROY
SAINTE MARIE CAEN
"""

if __name__ == "__main__":

    discours = "".join(open("examples/discours-fr.txt", "r").readlines())
    
    key = "HELLOTOUTLEMONDEDOINGWELL"

    encrypted = Vigenere.encode(discours, key)
    EncodeUtilities.output_encoded(encrypted)

    decrypted, key_result = Vigenere.decode(encrypted, key=False, language_targetted="fr", output=True)

    EncodeUtilities.output_encoded(decrypted, 128, 1)
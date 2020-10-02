# Crypto

This project is based on the Vigenere and Cesar methods of cryptography. You can both encrypt and decrypt message with the givens function in this project. You can also crack encrypted messages, as long as you have a sufficient amount of text to provide. It can work in English, French, Spanish and German. It was made for a NSI course. (Sainte Marie highschool, Mr Leroy)

## Table of contents
* [Technology](#technology)
* [Functions](#Functions)
* [Example](#example)

## Technology
The project is built with Python `3.8.1` and will basically work with all versions of python `3.X.X`

## Functions

If you want to use them in another script just use `from crypt import *`

The mains functions are
```
Cesar.encode(message_to_crypt, offset_in_alphabet)
Cesar.decode(encrypted_message, <offset_in_alphabet>, <language_targetted>)
Vigenere.encode(message_to_crypt, key)
Vigenere.decode(encrypted_message, <key>, <language_targetted>, <print_steps_of_crack>)
```
<arguments> are optionnal arguments.
If not any key is provided to Cesar.decode() and Vigenere.decode() the program will crack the key by itself.

## Example

In the givens file ( especially `main.py` , the example is made from a french political speech of 24 886 characters, and is encrypted with Vigenere.encode() with the key `HELLOTOUTLEMONDEDOINGWELL` ( 26 characters ) and is perfectly decrypted by Vigenere.decode(), without the key.

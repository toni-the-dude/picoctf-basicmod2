# picoctf-basicmod2

The file "decrypt.py" holds the solution to a challenge on PicoCTF involving a straightforward decryption scheme.

The URL for the challenge is: https://play.picoctf.org/practice/challenge/254

There are 2 functions used to calculate the modular inverse of a number at the top of the script.

The script then reads from the "message.txt" file, slightly cleans the input before processing and then decodes the message according to the rules of the challenge.
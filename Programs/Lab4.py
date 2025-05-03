'''Read a multi-digit number (as chars) from the console. Develop a program to print the frequency of
each digit with suitable message.'''

import pprint
message = input("Enter a multi-digit number:")
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
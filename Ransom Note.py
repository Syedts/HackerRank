#Hash Table Ransom Note
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    magazine = sorted(magazine)
    note = sorted(note)
    while True:
        if not note:
            print("Yes")
            break
        word = note[0]
        if word in magazine:
            note.remove(word)
            magazine.remove(word)
        else:
            print("No")
            break

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)


from collections import Counter


characterMap = {' ': 0, 'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

file1 = open('Dictionary1-2.txt', 'rb')
file2 = open('Dictionary2-1.txt', 'rb')

# key = input("Enter your the value of keylength")
#
# cipherText = raw_input("Enter the cipher text").strip().lower()
# cipherMap = map(lambda x: characterMap[x], cipherText)

def dictionary1():

    for line in file1:
        line = str(line).rstrip('\r\n')
        plainTextMap = map(lambda x: characterMap[x], line)
        frequencyMap = [abs(a_i - b_i) for a_i, b_i in zip(cipherMap, plainTextMap)]
        print len(Counter(frequencyMap))

def dictionary2():

    plaintext = []

    for line in file2:
        plaintext.append(line.rstrip('\r\n'))

    print len(" ".join(plaintext))

dictionary2()











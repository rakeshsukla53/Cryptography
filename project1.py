
from collections import Counter
from collections import defaultdict
import time


characterMap = {' ': 0, 'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

sentenceMap = defaultdict()

file1 = open('Dictionary1-2.txt', 'rb')
file2 = open('Dictionary2-1.txt', 'rb')

plaintext = []

for line in file2:
    plaintext.append(line.rstrip('\r\n'))

key = input("Enter your the value of keylength")

cipherText = raw_input("Enter the cipher text").strip().lower()
cipherMap = map(lambda x: characterMap[x], cipherText)

for i in range(len(plaintext)):
    #creating mapping for dictionary 2
    sentenceMap[plaintext[i]] = plaintext[0:i] + plaintext[i+1:]

def dictionary1():
    '''
    Find the plaintext from dictionary 1, by checking the number of unique shifts
    '''

    for line in file1:
        line = str(line).rstrip('\r\n')
        plainTextMap = map(lambda x: characterMap[x], line)
        frequencyMap = [a_i - b_i if a_i - b_i > 0 else a_i - b_i + 27 for a_i, b_i in zip(cipherMap, plainTextMap)]
        if len(Counter(frequencyMap).keys()) == 5:
            print line

def dictionary2(graph, start, path=[]):
        '''
        First generate a sentence using backtracking, and then check whether it is our possible plaintext candidate
        '''
        path = path + [start]
        if len(" ".join(path)) >= 100:
            return " ".join(path)[0:100]
        plainTextMap = map(lambda x: characterMap[x], " ".join(path))
        frequencyMap = [a_i - b_i for a_i, b_i in zip(cipherMap, plainTextMap)]
        if len(Counter(frequencyMap).keys()) <= key:
            for node in graph[start]:
                if node not in path:
                    result = dictionary2(graph, node, path)
                    if result:
                        print Counter(frequencyMap).values()
                        if Counter(frequencyMap).values().count(5) == 20:
                            print result, len(Counter(frequencyMap).keys())
                            print Counter(frequencyMap)
        else:
            return

# for i in plaintext:
#     dictionary2(sentenceMap, i)

dictionary1()


__author__ = 'rakesh'

characterMap = {' ': 0, 'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

inv_map = {v: k for k, v in characterMap.items()}

plaintext = 'and may not be limited to installing tools but may involve training staff members on operational pro'

t = [1, 2, 3, 4, 5]

rotatedArray = (map(lambda x: characterMap[x], plaintext))

for i in range(len(rotatedArray)):

    rotatedArray[i] = (t[i%5] + rotatedArray[i]) % 27

rotatedText = map(lambda x: inv_map[x], rotatedArray)


print "".join(rotatedText)

'''
icymshbgi fnrtjebpiyiqgwegqudrfcvywjpjdyigchfuccelbkqwyavksxfbuyqfucwybihdkjxhdfmnr xavkieecweerwdmq
having developed methods for measuring the data against those rules stage five allows the data quail
'''




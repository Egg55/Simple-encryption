##################################
##COOL ENCRYPTION SYSTEM I THINK##
##################################
###############
##~~EGG2021~~##
###############

import string
import random
import os
import re

global PASS
def encrypt(PASS):
    lis1 = []
    lis2 = []
    for letter in PASS:
        lis1.append(letter)

    new_dict = {}
    for x in range(len(string.printable[:95])):
       new_dict[string.printable[:95][x]] = ''.join(str(list(find(PASS, string.printable[x]))))

    for letter in ''.join(string.printable[:95]):
        if new_dict.get(letter) == '[]':
            new_dict.pop(letter)

    new_dict = {k: eval(new_dict[k]) for k in new_dict}

    for letter in string.printable[:95]:
        try:
            for x in range(len(new_dict[letter])+1):
                if str(new_dict[letter][x]).isdigit() == True and str(new_dict[letter][x+1]).isdigit() == True:
                    new_dict[letter].insert(x+1, '¶')
        except: pass

    for letter in string.printable[:95]:
        try: new_dict[letter].append('≠')
        except: pass

    x=0
    for letter in string.printable[:95]:
        if letter in string.digits:
            try:
                new_dict[string.printable[x]].insert(0, '¢')
            except: pass
            x += 1


    var = ''
    for k,v in new_dict.items():
        v = "".join(str(i) for i in v)
        var += f"{k}{v}"
    
    return var
    



def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


def decrypt(encoded):
    l1 = []
    for letter in encoded:
        l1.append(letter)
    global d
    d = {}
    for i in range(len(l1)):
        if l1[i].isalpha() or l1[i] == ' ':
            key = i
        if l1[i] == "≠":
            d[l1[key]] = l1[key+1:i+1]    

    l2 = []
    for i in range(len(d)*10):
        for key in d.keys():
            for x in range(len(d[key])):
                if str(i) in d[key][x]:
                    l2.append(''.join(key))

    return ''.join(l2)

def fullencrypt(fullencrypt):
    n = 10
    l5 = []
    line = fullencrypt

    val = [line[i:i+n] for i in range(0, len(line), n)]
    for item in val: 
        l5.append(encrypt(item)+'±')

    return ''.join(l5)

def fulldecrypt(fulldecrypt):
    l5 = []
    val = fulldecrypt.split('±')
    for item in val:
        l5.append(decrypt(item))
    return ''.join(l5)

#<3
print(fullencrypt('MY PASSWORD IS ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE AND TEN'))
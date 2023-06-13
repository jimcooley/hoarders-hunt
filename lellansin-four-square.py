# -*- coding: utf-8 -*-
#
# Four-Square Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
# @author Jim Cooley <jimcooley@gmail.com>
# modified for horders hunt
import re

table = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 

def generate_table(key = ''):
    # wiki：usually omitting "Q" or putting both "I" and "J" in the same location to reduce the alphabet to fit
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key = re.sub(r'[\W]', '', key).upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key.replace(key[0], '')
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]
    return table

def encrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L  = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += mangle(R, L, digraphs)
    return ciphertext


def mangle(R, L, digraphs):
    a = position(table, digraphs[0])
    b = position(table, digraphs[1])
    return R[a[0]][b[1]] + L[b[0]][a[1]]

def decrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper()
    TL = generate_table(keys[0])
    TR = generate_table(keys[1])
    BL = generate_table(keys[2])
    BR = generate_table(keys[3])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += unmangle(TL, TR, BL, BR, digraphs)
    return ciphertext.lower()

def unmangle(TL, TR, BL, BR, digraphs):
    a = position(TR, digraphs[0])
    b = position(BL, digraphs[1])
    
    return TL[a[0]][b[1]] + BR[b[0]][a[1]]

# todo
def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return (row, col)
    return (None, None)


if __name__ == '__main__':
    # http://en.wikipedia.org/wiki/Four-square_cipher

    ciphertext = 'rinrqekw'

    keys = ['outcast', 'twofaced', 'grudge', '']

    print(f'ciphertext: {ciphertext}')
    print(f'keys: {keys}')

    plaintext = decrypt(keys, ciphertext)

    print(f'plaintext: {plaintext}')

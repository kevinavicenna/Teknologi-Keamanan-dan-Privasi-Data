#Substitution Cipher

import random
def substitution_cipher(plaintext):
    # Buat daftar huruf acak
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(alphabet)

    # Membuat dict substitusi huruf asli ke huruf acak
    substitution_dict = {}
    for i in range(len(alphabet)):
        substitution_dict[chr(i + 65)] = alphabet[i]

    # Mengenkripsi plaintext 
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ciphertext += substitution_dict[char]
        else:
            ciphertext += char

    return ciphertext

plaintext = 'kevin avicenna widiarto'
ciphertext = substitution_cipher(plaintext)
print(ciphertext) 

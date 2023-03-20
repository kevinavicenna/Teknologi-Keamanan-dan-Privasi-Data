#Vigenere Chiper

def vigenere_cipher(key, plaintext):
    # Konversi kunci dan plaintext ke huruf besar
    key = key.upper()
    plaintext = plaintext.upper()
    
    ciphertext = ''
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Convert karakter plaintext menjadi indeks 0-25
            plaintext_index = ord(char) - 65
            # Convert karakter kunci menjadi indeks 0-25
            key_char = key[key_index % len(key)]
            key_index += 1

            # enkripsi menggunakan rumus Vigenere Cipher
            ciphertext_index = (plaintext_index + ord(key_char) - 130) % 26
            ciphertext += chr(ciphertext_index + 65)
        else:
            ciphertext += char

    return ciphertext

key = '183'
plaintext = 'test'
ciphertext = vigenere_cipher(key, plaintext)
print(ciphertext) 
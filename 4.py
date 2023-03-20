# Transposition Cipher 

def transposition_cipher(text, key):
    
    result = []
    plaintext_ascii = []
    result_ascii = []
    key_ascii = []
    sorted_key_ascii = []
    sorted_key_index = []
    sorted_result_ascii = []
    
    for char in text:
        plaintext_ascii.append(ord(char))
    for char in key:
        key_ascii.append(ord(char))
    # Mengurutkan key
    sorted_key_ascii = sorted(key_ascii)
    # Mencari index dari key yang sudah diurutkan
    for i in range(len(sorted_key_ascii)):
        sorted_key_index.append(key_ascii.index(sorted_key_ascii[i]))
    # Melakukan enkripsi dengan rumus Transposition Cipher
    for i in range(len(plaintext_ascii)):
        # Mengubah nilai ASCII plaintext menjadi nilai 0-25
        plaintext_ascii[i] -= 65
        # Melakukan operasi enkripsi
        result_ascii.append((plaintext_ascii[i] + key_ascii[i]) % 26)
        # Mengubah nilai ASCII hasil enkripsi menjadi nilai 65-90
        result_ascii[i] += 65
    # Mengurutkan hasil enkripsi berdasarkan index key yang sudah diurutkan
    for i in range(len(sorted_key_index)):
        sorted_result_ascii.append(result_ascii[sorted_key_index[i]])
    # Mengubah nilai ASCII hasil enkripsi menjadi karakter
    for i in range(len(sorted_result_ascii)):
        result.append(chr(sorted_result_ascii[i]))
    # Menggabungkan list hasil enkripsi menjadi string
    result = ''.join(result)
    return result


def main():
    text = input('Masukkan teks: ')
    key = input('Masukkan key: ')
    print('Hasil enkripsi: ', transposition_cipher(text, key))

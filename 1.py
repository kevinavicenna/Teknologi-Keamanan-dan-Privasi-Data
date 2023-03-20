#Shift Chiper

def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        # hanya akan diproses jika karakter adalah angka
        if char.isnumeric():
            # ubah karakter menjadi integer
            num = int(char)
            # melakukan operasi shift dengan menggunakan kunci
            num = (num + shift) % 10
            # tambah karakter terenkripsi ke dalam ciphertext
            ciphertext += str(num)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        # hanya akan diproses jika karakter adalah angka
        if char.isnumeric():
            # mengubah karakter menjadi integer
            num = int(char)
            # melakukan operasi shift dengan menggunakan kunci
            num = (num - shift) % 10
            # tambah karakter terdekripsi ke dalam plaintext
            plaintext += str(num)
        else:
            plaintext += char
    return plaintext

# Penggunaan 2 digit NIM L200200183 untuk Shift Chiper
plaintext = "83" #L200200183
shift = 83 #menggunakan shift 83

ciphertext = encrypt(plaintext, shift)
print("Ciphertext:", ciphertext)

decrypted_plaintext = decrypt(ciphertext, shift)
print("Decrypted plaintext:", decrypted_plaintext)


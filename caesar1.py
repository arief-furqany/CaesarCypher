plaintext = input("masukkan nama : ")
shift = 5

def encrypt(plainteks,shift):
    encrypted_text = " "

    for char in plaintext:
        # Cek apakah karakter adalah huruf
        if char.isalpha():

            #offset 65 = huruf besar, huruf kecil, dan simbol (modulus)
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            # Tambahkan karakter non-huruf tanpa diubah
            encrypted_text += char

    return encrypted_text


#decrypt pake Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


# Call encrypt
ciphertext = encrypt(plaintext, shift)
print("Encrypted text:", ciphertext)

# CAll Decrypt
decrypted_text = caesar_decrypt(ciphertext, shift)
print("Decrypted text:", decrypted_text)
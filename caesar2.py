def encrypt(plain_text, shift):
    cipher_text = ""

    for char in plain_text:
        # Huruf besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)

        # Huruf kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            # Karakter selain huruf tetap
            cipher_text += char

    return cipher_text


def decrypt(cipher_text, shift):
    plain_text = ""

    for char in cipher_text:
        # Huruf besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)

        # Huruf kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)

        else:
            # Karakter selain huruf tetap
            plain_text += char

    return plain_text


def main():
    print("Welcome dawgs")
    plain_text = input("Input teks dawgs: ")
    shift = int(input("Masukin key-nya dawg: "))

    # Panggil fungsi encrypt
    cipher_text = encrypt(plain_text, shift)
    print("Encrypted text:", cipher_text)

    # Panggil fungsi decrypt
    decrypted_text = decrypt(cipher_text, shift)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()

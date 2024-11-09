from pydoc import plain


def encrypt(plain_text, shift):
    cipher_text = ""

    for char in plain_text:

        # huruf besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)

        #huruf kecil
        elif char.isupper():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            # karakter selain huruf tetap
            cipher_text += char

    return cipher_text

def decrypt(cipher_text, shift):
    plain_text = ""

    for char in cipher_text:

        #HurufBesar
        if char.islower():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)

        # huruf kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)

        else:
        # karakter selain huruf tetap
            plain_text += char

    return plain_text


def main():
    print("Welcome dawgs")
    plain_text = input("input teks dawgs : ")
    shift = int(input("masukin key-nya dawg : "))

    # call function encrypt
    cipher_text = encrypt(plain_text, shift)
    print("encrypt :", cipher_text)

    #call function decrypt
    decrypted = decrypt(cipher_text, shift)
    print("decrypted text:", decrypted)

if __name__ == "__main__":
    main()
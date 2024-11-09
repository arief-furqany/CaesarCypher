cipherinput = input("Masukkan text : ")

# map subtitusi
substitution_map = {
    'a': '@', 'b': '8', 'c': '(', 'd': '6', 'e': '3', 'f': '#', 'g': '9',
    'h': '!', 'i': '1', 'j': ';', 'k': '<', 'l': '|', 'm': '^^', 'n': '^',
    'o': '0', 'p': '?', 'q': '/', 'r': '7', 's': '$', 't': '+', 'u': '%',
    'v': '>', 'w': '*', 'x': '}', 'y': '=', 'z': '&', ' ': '_'
}

#encrypt subtitusi
def subtitute(cipherinput):
    encrypted_text = ""

#mengganti input ke subtitution map
    for char in cipherinput.lower():
        encrypted_text += substitution_map.get(char, char)
    return encrypted_text

cipherasal = subtitute(cipherinput)
print("hasil encrypt : ", cipherasal)

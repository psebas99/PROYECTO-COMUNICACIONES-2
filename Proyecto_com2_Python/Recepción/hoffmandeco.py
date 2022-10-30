
def deco(tren):

    codigo_morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '\'': '· − − − − ·',
        '!': '− · − · − −',
        '/': '− · · − ·',
        '(': '− · − − ·',
        ')': '− · − − · −',
        '&': '· − · · ·',
        ':': '− − − · · ·',
        ';': '− · − · − ·',
        '=': '− · · · −',
        '+': '· − · − ·',
        '-': '− · · · · −',
        '_': '· · − − · −',
        '"': '· − · · − ·',
        '$': '· · · − · · −',
        '@': '· − − · − ·',
    }

    texto_codificado = ""


    for c in codigo_morse:
        if c != " " and c.lower() in codigo_morse:
            texto_codificado += codigo_morse[c.lower()]
        else:
            texto_codificado += c

    texto_binario = ""
    print("Texto codificado: {}".format(texto_codificado))

    for d in texto_codificado:

        if d!=  "-" :
            texto_binario += "1"
        else:
            texto_binario += "0"
    print("Texto codificado en binario: {}".format(texto_binario))

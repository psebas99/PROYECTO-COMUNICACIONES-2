def hoffman(texto):
    import math
    # dictionary for mapping characters to morse code
    CHARS_TO_MORSE_CODE_MAPPING = {
        'A': '-----.',
        'B': '----.-',
        'C': '----..',
        'D': '---.--',
        'E': '---.-.',
        'F': '---..-',
        'G': '---...',
        'H': '--.---',
        'I': '--.--.',
        'J': '--.-.-',
        'K': '--.-..',
        'L': '--..--',
        'M': '--..-.',
        'N': '--...-',
        'O': '--....',
        'P': '-.----',
        'Q': '-.---.',
        'R': '-.--.-',
        'S': '-.--..',
        'T': '-.-.--',
        'U': '-.-.-.',
        'V': '-.-..-',
        'W': '-.-...',
        'X': '-..---',
        'Y': '-..--.',
        'Z': '-..-.-',
        '1': '-..-..',
        '2': '-...--',
        '3': '-...-.',
        '4': '-....-',
        '5': '-.....',
        '6': '.-----',
        '7': '.----.',
        '8': '.---.-',
        '9': '.---..',
        '0': '.--.--',
        '.': '.--.-.',
        ',': '.--..-',
        '?': '.--...',
        ' ': '.-....',
    }

    # function to encode plain English text to morse code
    def to_morse_code(english_plain_text):
        morse_code = ''
        for char in english_plain_text:
            # checking for space
            # to add single space after every character and double space after every word
            #if char == ' ':
               # morse_code += '  '
            #else:
                # adding encoded morse code to the result
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
        return morse_code

    morse_code = to_morse_code(texto)
    print(morse_code)


    #CODIFICAVION A BINARIO
    texto_binario = ""
    texto_codificado = morse_code

    for d in texto_codificado:

        if d==  "-" :
            texto_binario += "0"
        elif d==  "." :
            texto_binario += "1"
        else:
            texto_binario += ""
    print("Texto codificado en binario: {}".format(texto_binario))

    #SEPARACIÓN DE SEGMENTOS 

    n= len(texto_binario)
    #print(n)
    m = (n/4)
    m= math.ceil(m)
    #print(m)
    int(texto_binario)
    archivo = []

    for i in range(0, m):
        p = 4*i
        archivo.append(texto_binario[p:p+4])
    
    #print(archivo)   
    return archivo

def decoder(palabra):
    def decode_morse(mapping):
        reversed = {}
        for key, value in mapping.items():
            reversed[value] = key
        return reversed  

    CHARS_TO_MORSE_CODE_MAPPING ={
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

    MORSE_CODE_TO_CHARS_MAPPING = decode_morse(CHARS_TO_MORSE_CODE_MAPPING)

    def texto_plano(palabra):
        english_plain_text = ''

        current_char_morse_code = ''
        i = 0
        while i < len(palabra) - 1:
            # checking for each character
            if palabra[i] == ' ':
                # checking for word
                if len(current_char_morse_code) == 0 and palabra[i + 1] == ' ':
                    english_plain_text += ' '
                    i += 1
                else:
                    # adding decoded character to the result
                    english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
                        current_char_morse_code]
                    current_char_morse_code = ''
            else:
                # adding morse code char to the current character
                current_char_morse_code += palabra[i]
            i += 1

        # adding last character to the result
        if len(current_char_morse_code) > 0:
            english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
                current_char_morse_code]

        return english_plain_text
    english_plain_text = texto_plano(palabra)

    
    print(english_plain_text)
    return english_plain_text

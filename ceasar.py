alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

again = 1


def bruteforce(text):
    global again
    plain_text = text
    cipher_text = ''
    if direction == "brute":
        for i in range(1, 26):
            cipher_text = ''
            for letter in plain_text:
                if letter in alphabet:
                    x = alphabet.index(letter)
                    x -= i
                    if x < 0:
                      x += 26
                cipher_text += alphabet[x]
            print(f"Shift of {i}: {cipher_text}")
        checker = input("Do you want to go again? Y/N\n")
        if checker == "N" or checker =="n":
            again = 0

def ceaser(text, shift, cipherdirection):
    plain_text = text
    global again
    cipher_text = ''
    if direction == "brute":
        for i in range(1, 26):
            cipher_text = ''
            for letter in plain_text:
                if letter in alphabet:
                    x = alphabet.index(letter)
                    x -= i
                    if x < 0:
                        x += 26
                cipher_text += alphabet[x]
            print(f"Shift of {i}: {cipher_text}")
    else:
        if shift > 26:
            shift = shift % 26
        for letter in plain_text:
            if letter in alphabet:
                x = alphabet.index(letter)
                if direction == "encode":
                    x += shift
                    if x > 25:
                        x -= 26
                elif direction == "decode":
                    x -= shift
                    if x < 0:
                        x += 26
                cipher_text += alphabet[x]

            else:
                cipher_text += letter
        print(f"The {cipherdirection}d text is {cipher_text}")
        checker = input("Do you want to go again? Y/N\n")
        if checker == "N":
            again = 0


while again == 1:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, or type 'brute' to bruteforce a piece of text:\n"
    )
    

    text = input("Type your message:\n").lower()
    if direction == "brute":
        bruteforce(text)
    else:
      shift = int(input("Type the shift number:\n"))

      ceaser(text, shift, direction)
else:
    print("Goodbye")

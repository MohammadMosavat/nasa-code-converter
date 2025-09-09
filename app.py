import base64
import sys

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def to_morse(text):
    return " ".join(MORSE_CODE.get(ch.upper(), '') for ch in text)

def to_binary(text):
    return " ".join(format(ord(ch), "08b") for ch in text)

def to_ascii(text):
    return " ".join(str(ord(ch)) for ch in text)

def to_hex(text):
    return " ".join(format(ord(ch), "02x") for ch in text)


def main():
    while True:
        print("\n NASA Code Converter ")
        print("1 - Morse Code")
        print("2 - Binary Code")
        print("3 - ASCII Code")
        print("4 - Hexadecimal Code")
        print("(:exit to quit)")

        choice = input("\nChoose code type (1-8): ").strip()
        
        if choice == ":exit":
            print("\ Exiting NASA Code Converter. Goodbye!")
            sys.exit(0)

        if choice not in [str(i) for i in range(1, 9)]:
            print("\n Invalid choice, try again.")
            continue

        while True:
            text = input("Enter text (letters/numbers, :back to menu, :exit to quit): ").strip()
            
            if text == ":exit":
                print("\n Exiting NASA Code Converter. Goodbye!")
                sys.exit(0)
            if text == ":back":
                print("\n Returning to main menu...")
                break 

            if choice == "1":
                print("\nMorse Code:", to_morse(text))
            elif choice == "2":
                print("\nBinary Code:", to_binary(text))
            elif choice == "3":
                print("\nASCII Code:", to_ascii(text))
            elif choice == "4":
                print("\nHexadecimal Code:", to_hex(text))
            elif choice == "5":
                print("\nGray Code:", to_gray(text))
            elif choice == "6":
                print("\nNumbers Only:", to_numbers(text))
            elif choice == "7":
                print("\nOctal Code:", to_octal(text))
            elif choice == "8":
                print("\nBase64 Encoding:", to_base64(text))

if __name__ == "__main__":
    main()

import string
import random
from deep_translator import GoogleTranslator

# Генерация случайного ключа
def generate_random_key(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Шифр Цезаря
def caesar_cipher(text, shift, decrypt=False):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    shift = -shift if decrypt else shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

# Азбука Морзе
def text_to_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }
    return ' '.join(morse_dict[char] for char in text.upper() if char in morse_dict)

def morse_to_text(morse):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
        '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
    }
    words = morse.split(' ')
    return ''.join(morse_dict[word] for word in words if word in morse_dict)

# Перевод текста (исправлено через deep_translator)
def translate_to_english(text):
    try:
        return GoogleTranslator(source='ru', target='en').translate(text)
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text  # Возвращаем исходный текст при ошибке

def translate_to_russian(text):
    try:
        return GoogleTranslator(source='en', target='ru').translate(text)
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text  # Возвращаем исходный текст при ошибке

# Шифр Вернама
def vernam_cipher(binary_text, binary_key):
    encrypted = ''.join(
        str(int(b) ^ int(k)) for b, k in zip(binary_text, binary_key * len(binary_text))
    )
    return encrypted

# Преобразование в группы цифр
def binary_to_digits(binary, group_size=3):
    groups = [binary[i:i + group_size] for i in range(0, len(binary), group_size)]
    return ''.join(str(int(group, 2)) for group in groups)

def digits_to_binary(digits, group_size=3):
    binary_groups = [format(int(digit), f'0{group_size}b') for digit in digits]
    return ''.join(binary_groups)

def main():
    # Ввод данных
    russian_text = input("Введите слово на русском: ")

    # Генерация ключа или ввод вручную
    key_choice = input("Вы хотите ввести свой ключ или сгенерировать случайный? (введите 'свой' или 'сгенерировать'): ").strip().lower()
    if key_choice == 'сгенерировать':
        key_length = int(input("Укажите длину ключа: "))
        key = generate_random_key(key_length)
        print("Сгенерированный ключ:", key)
    else:
        key = input("Введите ключ для шифрования: ")

    # Выбор сдвига для шифра Цезаря
    shift = int(input("Введите сдвиг для шифра Цезаря (целое число): "))

    # Перевод текста на английский
    english_text = translate_to_english(russian_text)
    print("Перевод на английский:", english_text)

    # Применение шифра Цезаря
    caesar_encrypted = caesar_cipher(english_text, shift)
    print("Шифр Цезаря:", caesar_encrypted)

    # Преобразование в азбуку Морзе
    morse_code = text_to_morse(caesar_encrypted)
    print("Азбука Морзе:", morse_code)

    # Шифр Вернама
    binary_key = ''.join(format(ord(char), '08b') for char in key)
    morse_binary = ''.join(format(ord(char), '08b') for char in morse_code)
    vernam_encrypted = vernam_cipher(morse_binary, binary_key)
    digit_groups = binary_to_digits(vernam_encrypted)

    print("Зашифрованный текст (цифры):", digit_groups)

    # Расшифровка
    decrypted_binary = digits_to_binary(digit_groups)
    decrypted_morse_binary = vernam_cipher(decrypted_binary, binary_key)
    decrypted_morse = ''.join(chr(int(decrypted_morse_binary[i:i+8], 2)) for i in range(0, len(decrypted_morse_binary), 8))
    caesar_decrypted = caesar_cipher(morse_to_text(decrypted_morse), shift, decrypt=True)
    russian_decrypted = translate_to_russian(caesar_decrypted)

    print("Расшифрованный текст:", russian_decrypted)

if __name__== "__main__":
    main()

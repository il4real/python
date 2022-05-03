purpose = input("What's your purpose -  Encryption(e) or Decryption(d)? Type 'e' or 'd': ")
language = input('Choose language: English(en) or Russian(ru)? Type "en" or "ru": ')
shift = int(input("Choose code's shift in numbers (For example - 7): "))
text = input('Enter your text: ')


def caesars_encrypt_en(text_inp, shift_inp):
    encrypted_text = ''
    for c in text_inp:
        encrypted_letter = c
        if c.isalpha():
            if c.isupper():
                encrypted_letter = ord(c) + shift_inp
                if 90 < encrypted_letter < 97:
                    encrypted_letter -= 26
            elif c.islower():
                encrypted_letter = ord(c) + shift_inp
                if encrypted_letter > 122:
                    encrypted_letter -= 26
            encrypted_letter = chr(encrypted_letter)
        encrypted_text += encrypted_letter
    return encrypted_text


def caesars_decrypt_en(text_inp, shift_inp):
    decrypted_text = ''
    for c in text_inp:
        decrypted_letter = c
        if c.isalpha():
            if c.isupper():
                decrypted_letter = ord(c) - shift_inp
                if decrypted_letter < 65:
                    decrypted_letter += 26
            elif c.islower():
                decrypted_letter = ord(c) - shift_inp
                if decrypted_letter < 97:
                    decrypted_letter += 26
            decrypted_letter = chr(decrypted_letter)
        decrypted_text += decrypted_letter
    return decrypted_text


#  Русский сделан только для прописных букв. Нужно дополнить!


def caesars_encrypt_ru(text_inp, shift_inp):
    encrypted_text = ''
    for c in text_inp:
        encrypted_letter = c
        if c.isalpha():
            encrypted_letter = ord(c) + shift_inp
            if encrypted_letter > 1103:
                encrypted_letter -= 32
            encrypted_letter = chr(encrypted_letter)
        encrypted_text += encrypted_letter
    return encrypted_text


def caesars_decrypt_ru(text_inp, shift_inp):
    decrypted_text = ''
    for c in text_inp:
        decrypted_letter = c
        if c.isalpha():
            decrypted_letter = ord(c) - shift_inp
            if decrypted_letter < 1072:
                decrypted_letter += 32
            decrypted_letter = chr(decrypted_letter)
        decrypted_text += decrypted_letter
    return decrypted_text


if purpose == 'e' and language == 'en':
    print(caesars_encrypt_en(text, shift))
if purpose == 'd' and language == 'en':
    print(caesars_decrypt_en(text, shift))
if purpose == 'e' and language == 'ru':
    print(caesars_encrypt_ru(text, shift))
if purpose == 'd' and language == 'ru':
    print(caesars_decrypt_ru(text, shift))

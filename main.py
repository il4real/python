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


text = input().split()
new_text = []
for i in range(len(text)):
    code_len = 0
    prepin = 0
    if text[i].isalpha():
        code_len = len(text[i])
    if not text[i].isalpha():
        for j in range(len(text[i])):
            if not text[i][j].isalpha():
                prepin += 1
        code_len = len(text[i]) - prepin
    new_text.append(caesars_encrypt_en(text[i], code_len))
print(*new_text)

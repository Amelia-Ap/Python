# import string
# lowercase_alphabet = string.ascii_lowercase
klartext = "hallo z"
key = 3
ciphertext_list = []

for symbol in klartext:
    ascii_val = ord(symbol)
    # ord("a") = 97, ord("z") = 122 ("A" and "Z" would correspond to 65 and 90)
    if (ascii_val > 96 and ascii_val < 123):
        if ascii_val + key > 123:
            print(f"bigger than 123: {ascii_val + key} \nnew_ascii_val: {96 + (ascii_val + key) % 123}")
            new_letter = chr(96 + (ascii_val + key) % 123)
        else:
            print(ascii_val, end=" ")
            new_letter = chr(ascii_val + key)
    else:
        print(symbol, end="")
        new_letter = symbol
    ciphertext_list.append(new_letter)

for letter in ciphertext_list:
    print(letter, end="")


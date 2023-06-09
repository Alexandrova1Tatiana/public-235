def xor_cipher(str, key):
    encript_str = ""
    for letter in str:
        encript_str += chr(ord(letter) ^ key)
    return encript_str


strg = input()
key = 8
print("original:\n", strg)
encr_strg = xor_cipher(strg, key)
print("encript:\n", encr_strg)
print("decript:\n", xor_cipher(encr_strg, key))
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from stegano import lsb

def extract_text(image_path):
    secret = lsb.reveal(image_path)
    return secret


def decrypt_aes(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), 16).decode('utf-8')
    return decrypted_text


# extracted_text = extract_text("123.png")
#
# key_file_path = "key.bin"
# with open(key_file_path, "rb") as key_file:
#     key = key_file.read()
#
# decrypted_text = decrypt_aes(extracted_text, key)
#
# print("Extracted decrypted text:", decrypted_text)

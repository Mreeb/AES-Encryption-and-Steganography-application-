from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from stegano import lsb
from Crypto.Random import get_random_bytes


def encrypt_aes(text, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(text.encode('utf-8'), 16)
    ciphertext = cipher.encrypt(padded_text)
    encrypted_data = base64.b64encode(iv + ciphertext).decode('utf-8')
    return encrypted_data


def hide_text(image_path, text_to_hide, output_path):
    secret = lsb.hide(image_path, text_to_hide)
    secret.save(output_path)


# input_text = "Hello world!"
#
# key_file_path = "key.bin"
# with open(key_file_path, "rb") as key_file:
#     key = key_file.read()
#
# cipher_text = encrypt_aes(input_text, key)
# print("Encryption Successful")
# hide_text("image.jpg", cipher_text, "123.png")
# print("Steganography Successful")

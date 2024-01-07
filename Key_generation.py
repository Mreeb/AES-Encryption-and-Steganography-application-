from Crypto.Random import get_random_bytes


def key_generation():
    key = get_random_bytes(32)
    key_file_path = "key.bin"
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
    print(f"Key Generation Successful file saved at {key_file_path}")


key_generation()

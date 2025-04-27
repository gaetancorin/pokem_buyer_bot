import hashlib
import json

# Where you write general functions
def change_uppercase(text):
    return text.upper()

def test_hash_md5():
    texte = "Balignon-XY Poings Furieux-006"
    hash_md5 = hashlib.md5(texte.encode()).hexdigest()

    print(hash_md5)

if __name__ == "__main__":
    test_hash_md5()

    # 64dae11f202d1a86caa063966112b980
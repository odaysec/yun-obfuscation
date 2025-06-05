# decrypt.py
from mapping import greek_to_latin

def decrypt(text):
    return ''.join(greek_to_latin.get(char, char) for char in text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <filename>")
        exit()

    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as f:
        encoded = f.read()
    decrypted = decrypt(encoded)

    output_file = filename + ".decoded"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted)

    print(f"[+] Decrypted file saved to {output_file}")

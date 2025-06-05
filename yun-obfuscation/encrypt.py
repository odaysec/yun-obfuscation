# encrypt.py
from mapping import latin_to_greek

def encrypt(text):
    return ''.join(latin_to_greek.get(char, char) for char in text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python encrypt.py <filename>")
        exit()

    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as f:
        original = f.read()
    encrypted = encrypt(original)

    output_file = filename + ".greek"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted)

    print(f"[+] Encrypted file saved to {output_file}")

# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from mapping import latin_to_greek, greek_to_latin

def encrypt(text):
    return ''.join(latin_to_greek.get(c, c) for c in text)

def decrypt(text):
    return ''.join(greek_to_latin.get(c, c) for c in text)

def load_file():
    path = filedialog.askopenfilename(filetypes=[("Text or Python Files", "*.txt *.py")])
    if path:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, content)

def save_output():
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path:
        content = output_text.get("1.0", tk.END)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        messagebox.showinfo("Saved", f"Output saved to:\n{path}")

def do_encrypt():
    raw = input_text.get("1.0", tk.END)
    result = encrypt(raw)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def do_decrypt():
    raw = input_text.get("1.0", tk.END)
    result = decrypt(raw)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# GUI setup
root = tk.Tk()
root.title("Greek Symbol Encryptor")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady=10)

# Input
tk.Label(frame, text="Input Text").grid(row=0, column=0)
input_text = tk.Text(frame, height=15, width=90)
input_text.grid(row=1, column=0, padx=10, pady=5)

# Output
tk.Label(frame, text="Output").grid(row=2, column=0)
output_text = tk.Text(frame, height=15, width=90)
output_text.grid(row=3, column=0, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="🔓 Decrypt", command=do_decrypt, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="🔐 Encrypt", command=do_encrypt, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="📂 Load File", command=load_file, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="💾 Save Output", command=save_output, width=15).pack(side=tk.LEFT, padx=5)

root.mainloop()

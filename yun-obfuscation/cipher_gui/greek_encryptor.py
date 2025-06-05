import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import tkinter as tk

class GreekSymbolEncryptorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("🧿 Greek Symbol Encryptor - Modern Edition")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.style = tb.Style("darkly")  # theme: darkly, cyborg, flatly, journal, solar, etc

        # Frames
        self.frame = tb.Frame(self.root, padding=20)
        self.frame.pack(fill=BOTH, expand=True)

        # Title
        tb.Label(self.frame, text="Greek Symbol Encryptor", font=("Segoe UI", 24, "bold")).pack(pady=10)

        # Input Text Area
        tb.Label(self.frame, text="🔤 Input Text:", font=("Segoe UI", 12)).pack(anchor=W)
        self.input_text = tb.Text(self.frame, height=6, wrap=WORD, font=("Consolas", 11))
        self.input_text.pack(fill=X, pady=5)

        # Output Area
        tb.Label(self.frame, text="📦 Output:", font=("Segoe UI", 12)).pack(anchor=W)
        self.output_text = tb.Text(self.frame, height=6, wrap=WORD, font=("Consolas", 11), state=DISABLED)
        self.output_text.pack(fill=X, pady=5)

        # Buttons
        self.button_frame = tb.Frame(self.frame)
        self.button_frame.pack(pady=10)

        tb.Button(self.button_frame, text="🔐 Encrypt", command=self.encrypt).pack(side=LEFT, padx=5)
        tb.Button(self.button_frame, text="🔓 Decrypt", command=self.decrypt).pack(side=LEFT, padx=5)
        tb.Button(self.button_frame, text="📂 Load File", command=self.load_file).pack(side=LEFT, padx=5)
        tb.Button(self.button_frame, text="💾 Save Output", command=self.save_output).pack(side=LEFT, padx=5)

        # Theme Switcher
        self.theme_chooser = tb.Combobox(self.frame, values=self.style.theme_names(), bootstyle=INFO)
        self.theme_chooser.set(self.style.theme.name)
        self.theme_chooser.pack(pady=5)
        self.theme_chooser.bind("<<ComboboxSelected>>", self.change_theme)

        # Footer
        tb.Label(self.frame, text="🔧 Developed by Pwn0sec Technologies", font=("Segoe UI", 9)).pack(pady=10)

    def change_theme(self, event):
        selected = self.theme_chooser.get()
        self.style.theme_use(selected)

    def encrypt(self):
        raw = self.input_text.get("1.0", END).strip()
        encrypted = self.simple_encrypt(raw)
        self.output_text.config(state=NORMAL)
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, encrypted)
        self.output_text.config(state=DISABLED)

    def decrypt(self):
        encrypted = self.input_text.get("1.0", END).strip()
        decrypted = self.simple_decrypt(encrypted)
        self.output_text.config(state=NORMAL)
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, decrypted)
        self.output_text.config(state=DISABLED)

    def simple_encrypt(self, text):
        greek_map = {"a": "α", "b": "β", "c": "γ", "d": "δ", "e": "ε",
                     "f": "φ", "g": "γ", "h": "η", "i": "ι", "j": "ξ",
                     "k": "κ", "l": "λ", "m": "μ", "n": "ν", "o": "ο",
                     "p": "π", "q": "θ", "r": "ρ", "s": "σ", "t": "τ",
                     "u": "υ", "v": "ϝ", "w": "ω", "x": "χ", "y": "ψ", "z": "ζ"}
        return ''.join(greek_map.get(c.lower(), c) for c in text)

    def simple_decrypt(self, text):
        reverse_map = {v: k for k, v in self.simple_encrypt("abcdefghijklmnopqrstuvwxyz").items()}
        return ''.join(reverse_map.get(c, c) for c in text)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.input_text.delete("1.0", END)
                self.input_text.insert(END, content)

    def save_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.output_text.get("1.0", END).strip())

if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    app = GreekSymbolEncryptorApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Entry, Button, Frame, Label, Combobox

# GUNAKAN Text dari tkinter, BUKAN ttkbootstrap
from tkinter import Text


class GreekSymbolEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚛ Greek Symbol Encryptor - Modern Edition")
        self.root.geometry("800x600")
        self.style = Style("darkly")

        # Frame utama
        main_frame = Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Input Label dan Textbox
        Label(main_frame, text="🔐 Input Text:", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.input_text = Text(main_frame, height=7, font=("Consolas", 10))
        self.input_text.pack(fill=X, pady=(0, 10))

        # Output Label dan Textbox
        Label(main_frame, text="🧮 Output:", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.output_text = Text(main_frame, height=7, font=("Consolas", 10), bg="#2a2a2a", fg="#00ff00")
        self.output_text.pack(fill=X, pady=(0, 10))

        # Tombol-tombol
        btn_frame = Frame(main_frame)
        btn_frame.pack(pady=10)

        Button(btn_frame, text="🔒 Encrypt", bootstyle="primary", command=self.encrypt).pack(side=LEFT, padx=5)
        Button(btn_frame, text="🔓 Decrypt", bootstyle="info", command=self.decrypt).pack(side=LEFT, padx=5)
        Button(btn_frame, text="📂 Load File", bootstyle="warning", command=self.load_file).pack(side=LEFT, padx=5)
        Button(btn_frame, text="💾 Save Output", bootstyle="success", command=self.save_output).pack(side=LEFT, padx=5)

        # Theme selector
        self.theme_combo = Combobox(main_frame, values=Style().theme_names(), width=20)
        self.theme_combo.set("darkly")
        self.theme_combo.pack(pady=5)
        self.theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

        # Footer
        Label(main_frame, text="© Developed by odaysec | github.com/odaysec — All rights reversed", font=("Segoe UI", 9), foreground="#888").pack(side=BOTTOM, pady=10)

    def encrypt(self):
        text = self.input_text.get("1.0", tk.END).strip()
        encrypted = ''.join(chr(ord(c) + 0x0370) for c in text)  # simbol Yunani
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted)

    def decrypt(self):
        text = self.input_text.get("1.0", tk.END).strip()
        try:
            decrypted = ''.join(chr(ord(c) - 0x0370) for c in text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, decrypted)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt:\n{e}")

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Open Text File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, content)

    def save_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Output", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                content = self.output_text.get("1.0", tk.END).strip()
                f.write(content)

    def change_theme(self, event=None):
        new_theme = self.theme_combo.get()
        self.style.theme_use(new_theme)


if __name__ == "__main__":
    root = tk.Tk()
    app = GreekSymbolEncryptorApp(root)
    root.mainloop()

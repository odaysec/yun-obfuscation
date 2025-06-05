# yun-obfuscation
Ancient Greece as a form of “visual encryption” or obfuscation for both plain text and source code. It's not strong cryptographic encryption, but it's enough to disguise the contents of the text from being read immediately



# ⚛ Greek Symbol Encryptor - Modern Edition
> A modern encryption tool using Greek Unicode transformation built with a stylish graphical interface using `ttkbootstrap`.  
> Developed by [odaysec](https://github.com/odaysec) | All rights reversed


## 🧩 What is This?
This project is a **fun encryption/decryption tool** that converts text into **Greek symbol-like characters** using Unicode transformations. It's not meant for military-grade encryption, but for educational, obfuscation, and novelty use cases. The GUI is built using Python's `tkinter` and enhanced with `ttkbootstrap` for a modern look and feel.



## 🚀 Features

- 🔐 Encrypt any text into Greek-style symbols using Unicode offsets.
- 🔓 Decrypt encrypted text back to its original.
- 📂 Load text from a `.txt` file.
- 💾 Save encrypted/decrypted output to a file.
- 🎨 Change GUI theme (Dark, Light, Cosmo, Morph, etc.)
- ✅ Built with Python 3.12+ and `ttkbootstrap`



## 🖥️ Preview
https://github.com/user-attachments/assets/910adf79-82c6-4277-b885-f26f5526ed3f

## Installation Guide
### 1. Requirements
- Python 3.10+ (recommended 3.12+)
- `pip` (Python package installer)
- OS: Linux / Windows / macOS

### 2. 🧰 Install Python (if not installed)

**For Debian/Ubuntu/Linux Mint:**
```bash
sudo apt update
sudo apt install python3 python3-pip -y
````

**For Windows:**
Download Python from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
Ensure “Add to PATH” is checked during installation.



### 3. 📥 Clone the Repository

```bash
git clone https://github.com/odaysec/greek-symbol-encryptor.git
cd greek-symbol-encryptor
```

### 4. 🧪 Create Virtual Environment (Recommended)

```bash
python3 -m venv cipher_gui
source cipher_gui/bin/activate  # On Windows: cipher_gui\Scripts\activate
```

### 5. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔓 Start the Application
```bash
python3 main.py
```


## 🖼️ Application Interface
* 🔐 **Input Text**: Paste or type your original message.
* ✅ Click **Encrypt** to convert it to Greek-style characters.
* 🔄 Click **Decrypt** to decode back to original text.
* 📂 **Load File**: Load `.txt` file content to input area.
* 💾 **Save Output**: Save encrypted result to `.txt` file.
* 🎨 **Theme Selector**: Pick from various modern themes (darkly, morph, flatly, etc.).

## ⚠️ Notes
* This is **not** secure cryptography. It uses character shifting for novelty, educational or obfuscation purposes.
* Unicode symbols used are derived from the **Greek and Coptic** block (U+0370 to U+03FF).
* It’s great for hiding strings, generating pseudo-obfuscated text, or just fun with friends!


## 📄 License
MIT License © 2025
Developed by [odaysec](https://github.com/odaysec)
**All rights reversed** 🙃

## 🤝 Contribute
Feel free to fork and modify. Pull requests are welcome. You can also:

* 🌟 Star the repo
* 🐛 Report issues
* 🔧 Suggest features


## 📬 Contact
**GitHub**: [@odaysec](https://github.com/odaysec)

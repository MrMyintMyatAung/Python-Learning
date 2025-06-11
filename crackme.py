from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import tkinter as tk
from tkinter import messagebox

def calculate_md5(input_str):
    """Calculate MD5 hash of ASCII-encoded input string"""
    return hashlib.md5(input_str.encode('ascii')).hexdigest().upper()

def decrypt_aes(ciphertext, key, iv):
    """Decrypt AES-CBC with PKCS7 padding"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('ascii')

def check_decryption():
    # AES parameters
    key = b"TESTAAAABBBBCCCC"
    iv = b"TESTAAAABBBBCCCC"
    
    # Ciphertext bytes (same as C# byte array)
    ciphertext = bytes([0xd2, 0xf0, 0x77, 0xa9, 0x9a, 0xa7, 0x2d, 0x76,
                       0x4c, 70, 0x72, 14, 0x6a, 0x3f, 0x2f, 0x85])
    
    # Get user input
    user_input = textbox.get()
    
    # Verify MD5 hash
    if calculate_md5(user_input) == "6136C2A666EABC25A3B6A6348473A7C7":
        # Decrypt and show message
        decrypted = decrypt_aes(ciphertext, key, iv)
        messagebox.showinfo("Success", decrypted)
    else:
        messagebox.showerror("Failure", "FAIL!")

# Create GUI
root = tk.Tk()
root.title("AES Decryption Challenge")

tk.Label(root, text="Enter the secret key:").pack(pady=5)
textbox = tk.Entry(root, width=40)
textbox.pack(pady=5)

tk.Button(root, text="Decrypt", command=check_decryption).pack(pady=10)

root.mainloop()
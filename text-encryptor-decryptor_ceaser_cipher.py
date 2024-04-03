import tkinter as tk

def encrypt(text, key):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    
    return result

def decrypt(text, decryptkey):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) - decryptkey - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - decryptkey - 97) % 26 + 97)
        else:
            result += char
    
    return result

def encrypt_command():
    text = input_text.get("1.0", "end-1c")
    key = int(key_entry.get())
    result = encrypt(text, key)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

def decrypt_command():
    text = input_text.get("1.0", "end-1c")
    decryptkey = int(key_entry.get())
    result = decrypt(text, decryptkey)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

# Create main application window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Labels
input_label = tk.Label(root, text="Input Text:")
input_label.grid(row=0, column=0, padx=10, pady=5)

key_label = tk.Label(root, text="Key:")
key_label.grid(row=1, column=0, padx=10, pady=5)

output_label = tk.Label(root, text="Output Text:")
output_label.grid(row=2, column=0, padx=10, pady=5)

# Text Entry
input_text = tk.Text(root, height=5, width=30)
input_text.grid(row=0, column=1, padx=10, pady=5)

key_entry = tk.Entry(root, width=10)
key_entry.grid(row=1, column=1, padx=10, pady=5)

output_text = tk.Text(root, height=5, width=30)
output_text.grid(row=2, column=1, padx=10, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_command)
encrypt_button.grid(row=3, column=0, padx=10, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_command)
decrypt_button.grid(row=3, column=1, padx=10, pady=5)

# Run the tkinter event loop
root.mainloop()

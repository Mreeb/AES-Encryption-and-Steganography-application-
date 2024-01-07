import tkinter as tk
from tkinter import ttk, simpledialog, filedialog
from ttkthemes import ThemedStyle
from Sender import encrypt_aes, hide_text
from Receiver import decrypt_aes, extract_text


class CustomInputDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Input Text")
        self.geometry('400x200')
        self.configure(bg='#111111')

        ttk.Label(master, text="Enter the text to encrypt:", background='#111111', foreground='#00FF00').pack(pady=10)
        self.input_text = ttk.Entry(master, font=('Arial', 12), background='#111111', foreground='#00FF00')
        self.input_text.pack()

    def apply(self):
        self.result = self.input_text.get()


class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Crypto GUI')
        self.geometry('600x400')
        self.configure(bg='#111111')  # Set background color to black

        style = ThemedStyle(self)
        style.set_theme('equilux')  # Use the 'equilux' theme with black and green colors

        self.mode_label = ttk.Label(self, text='Select Mode:', background='#111111',
                                    foreground='#00FF00')  # Set text color to green
        self.encrypt_button = ttk.Button(self, text='Encryption', command=self.encryptClicked, style='TButton')
        self.decrypt_button = ttk.Button(self, text='Decryption', command=self.decryptClicked, style='TButton')

        self.result_text = tk.Text(self, wrap=tk.WORD, height=10, width=50, state=tk.DISABLED, bg='#111111',
                                   fg='#00FF00')  # Set text box colors

        self.mode_label.pack(pady=10)
        self.result_text.pack(pady=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        self.encrypt_button.pack(side=tk.LEFT, padx=125)
        self.decrypt_button.pack(side=tk.LEFT, padx=5)

    def encryptClicked(self):
        input_text_dialog = CustomInputDialog(self)
        input_text = input_text_dialog.result
        if input_text:
            key_file_path = "key.bin"
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()

            cipher_text = encrypt_aes(input_text, key)
            print("Encryption Successful")

            file_name = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")])
            if file_name:
                hide_text(file_name, cipher_text, "output_image.png")
                result = "Encryption and Steganography Successful"
                self.update_result(result)

    def decryptClicked(self):
        file_name = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("Images", "*.png;*.jpg;*.jpeg")])
        if file_name:
            extracted_text = extract_text(file_name)

            key_file_path = "key.bin"
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()

            decrypted_text = decrypt_aes(extracted_text, key)
            result = f"{decrypted_text}"
            self.update_result(result)

    def update_result(self, result):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)


if __name__ == '__main__':
    app = CryptoApp()
    app.mainloop()


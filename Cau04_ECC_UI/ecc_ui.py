import tkinter as tk
from tkinter import messagebox
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt

private_key_hex = ""
public_key_hex = ""

def tao_khoa():
    global private_key_hex, public_key_hex
    try:
        eth_k = generate_eth_key()
        private_key_hex = eth_k.to_hex()
        public_key_hex = eth_k.public_key.to_hex()

        txt_private.delete("1.0", tk.END)
        txt_private.insert(tk.END, private_key_hex)

        txt_public.delete("1.0", tk.END)
        txt_public.insert(tk.END, public_key_hex)

        messagebox.showinfo("Thông báo", "Đã tạo cặp khóa ECC")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def ma_hoa():
    try:
        if public_key_hex == "":
            messagebox.showwarning("Thông báo", "Vui lòng tạo khóa trước")
            return

        plaintext = txt_input.get("1.0", tk.END).strip()
        if plaintext == "":
            messagebox.showwarning("Thông báo", "Vui lòng nhập nội dung cần mã hóa")
            return

        encrypted = encrypt(public_key_hex, plaintext.encode("utf-8"))
        cipher_hex = encrypted.hex()

        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, cipher_hex)
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def giai_ma():
    try:
        if private_key_hex == "":
            messagebox.showwarning("Thông báo", "Vui lòng tạo khóa trước")
            return

        cipher_hex = txt_input.get("1.0", tk.END).strip()
        if cipher_hex == "":
            messagebox.showwarning("Thông báo", "Vui lòng nhập nội dung cần giải mã")
            return

        cipher_bytes = bytes.fromhex(cipher_hex)
        decrypted = decrypt(private_key_hex, cipher_bytes).decode("utf-8")

        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, decrypted)
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def xoa_trang():
    txt_input.delete("1.0", tk.END)
    txt_output.delete("1.0", tk.END)

root = tk.Tk()
root.title("UI Mã hóa và Giải mã ECC")
root.geometry("750x600")
root.resizable(False, False)

lbl_title = tk.Label(root, text="CHƯƠNG TRÌNH MÃ HÓA / GIẢI MÃ ECC", font=("Arial", 14, "bold"))
lbl_title.pack(pady=10)

btn_key = tk.Button(root, text="Tạo khóa ECC", width=20, command=tao_khoa)
btn_key.pack(pady=5)

lbl_public = tk.Label(root, text="Public Key:", font=("Arial", 11))
lbl_public.pack(anchor="w", padx=20)

txt_public = tk.Text(root, height=4, width=85)
txt_public.pack(padx=20, pady=5)

lbl_private = tk.Label(root, text="Private Key:", font=("Arial", 11))
lbl_private.pack(anchor="w", padx=20)

txt_private = tk.Text(root, height=4, width=85)
txt_private.pack(padx=20, pady=5)

lbl_input = tk.Label(root, text="Nhập dữ liệu:", font=("Arial", 11))
lbl_input.pack(anchor="w", padx=20)

txt_input = tk.Text(root, height=6, width=85)
txt_input.pack(padx=20, pady=5)

frame_button = tk.Frame(root)
frame_button.pack(pady=10)

btn_encrypt = tk.Button(frame_button, text="Mã hóa", width=15, command=ma_hoa)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_button, text="Giải mã", width=15, command=giai_ma)
btn_decrypt.grid(row=0, column=1, padx=10)

btn_clear = tk.Button(frame_button, text="Xóa trắng", width=15, command=xoa_trang)
btn_clear.grid(row=0, column=2, padx=10)

lbl_output = tk.Label(root, text="Kết quả:", font=("Arial", 11))
lbl_output.pack(anchor="w", padx=20)

txt_output = tk.Text(root, height=8, width=85)
txt_output.pack(padx=20, pady=5)

root.mainloop()
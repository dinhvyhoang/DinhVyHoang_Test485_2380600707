import tkinter as tk
from tkinter import messagebox
from transposition_cipher import TranspositionCipher

cipher = TranspositionCipher()

def ma_hoa():
    try:
        text = txt_input.get("1.0", tk.END).strip()
        key = int(entry_key.get().strip())

        if text == "":
            messagebox.showwarning("Thông báo", "Vui lòng nhập chuỗi cần mã hoá")
            return

        result = cipher.encrypt(text, key)
        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Lỗi", "Key phải là số nguyên")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def giai_ma():
    try:
        text = txt_input.get("1.0", tk.END).strip()
        key = int(entry_key.get().strip())

        if text == "":
            messagebox.showwarning("Thông báo", "Vui lòng nhập chuỗi cần giải mã")
            return

        result = cipher.decrypt(text, key)
        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Lỗi", "Key phải là số nguyên")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def xoa_trang():
    txt_input.delete("1.0", tk.END)
    entry_key.delete(0, tk.END)
    txt_output.delete("1.0", tk.END)

root = tk.Tk()
root.title("UI Mã hoá và Giải mã Transposition")
root.geometry("600x450")
root.resizable(False, False)

lbl_title = tk.Label(
    root,
    text="CHƯƠNG TRÌNH MÃ HOÁ / GIẢI MÃ TRANSPOSITION",
    font=("Arial", 14, "bold")
)
lbl_title.pack(pady=10)

lbl_input = tk.Label(root, text="Nhập chuỗi:", font=("Arial", 11))
lbl_input.pack(anchor="w", padx=20)

txt_input = tk.Text(root, height=6, width=65)
txt_input.pack(padx=20, pady=5)

frame_key = tk.Frame(root)
frame_key.pack(pady=10)

lbl_key = tk.Label(frame_key, text="Nhập key:", font=("Arial", 11))
lbl_key.grid(row=0, column=0, padx=5)

entry_key = tk.Entry(frame_key, width=15)
entry_key.grid(row=0, column=1, padx=5)

frame_button = tk.Frame(root)
frame_button.pack(pady=10)

btn_encrypt = tk.Button(frame_button, text="Mã hoá", width=15, command=ma_hoa)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_button, text="Giải mã", width=15, command=giai_ma)
btn_decrypt.grid(row=0, column=1, padx=10)

btn_clear = tk.Button(frame_button, text="Xoá trắng", width=15, command=xoa_trang)
btn_clear.grid(row=0, column=2, padx=10)

lbl_output = tk.Label(root, text="Kết quả:", font=("Arial", 11))
lbl_output.pack(anchor="w", padx=20)

txt_output = tk.Text(root, height=6, width=65)
txt_output.pack(padx=20, pady=5)

root.mainloop()
import tkinter as tk
import winsound  # Modul untuk memainkan suara di Windows

# Fungsi untuk menangani tombol yang ditekan
def on_button_click(value):
    # Memainkan suara klik
    winsound.Beep(1000, 100)  # Frekuensi 1000 Hz, durasi 100 ms

    if value == "=":
        try:
            result = eval(entry.get())  # Menghitung hasil ekspresi matematika
            entry.delete(0, tk.END)     # Menghapus teks di kotak input
            entry.insert(tk.END, str(result))  # Menampilkan hasil
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)  # Menghapus semua teks di kotak input
    else:
        entry.insert(tk.END, value)  # Menambahkan karakter ke kotak input

# Fungsi untuk efek hover (mouse masuk ke tombol)
def on_enter(event, button):
    button.config(bg="#FFD700")  # Warna kuning saat hover

# Fungsi untuk efek hover (mouse keluar dari tombol)
def on_leave(event, button):
    button.config(bg=button.original_bg)  # Kembalikan ke warna asli

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("500x600")  # Ukuran jendela diperbesar
root.resizable(False, False)

# Kotak input untuk menampilkan angka dan hasil
entry = tk.Entry(root, font=("Arial", 30), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="nsew")

# Daftar tombol pada kalkulator
buttons = [
    "7", "8", "9", "\u00F7",  # Simbol bagi (÷)
    "4", "5", "6", "\u00D7",  # Simbol kali (×)
    "1", "2", "3", "\u2212",  # Simbol kurang (−)
    "C", "0", "=", "\u002B"   # Simbol tambah (+)
]

# Menempatkan tombol-tombol di grid
row = 1
col = 0
for button_text in buttons:
    # Memberikan warna berbeda untuk tombol operasi matematika
    if button_text in {"\u00F7", "\u00D7", "\u2212", "\u002B"}:
        btn = tk.Button(
            root,
            text=button_text,
            font=("Arial", 24, "bold"),
            width=8,       # Lebar tombol diperbesar
            height=2,      # Tinggi tombol diperbesar
            bg="#FFA500",  # Warna oranye untuk tombol operasi
            fg="white",    # Warna teks putih
            command=lambda x=button_text: on_button_click(x.replace("\u00F7", "/").replace("\u00D7", "*").replace("\u2212", "-").replace("\u002B", "+"))
        )
    elif button_text == "=":
        btn = tk.Button(
            root,
            text=button_text,
            font=("Arial", 24, "bold"),
            width=8,
            height=2,
            bg="#4CAF50",  # Warna hijau untuk tombol sama dengan
            fg="white",
            command=lambda x=button_text: on_button_click(x)
        )
    elif button_text == "C":
        btn = tk.Button(
            root,
            text=button_text,
            font=("Arial", 24, "bold"),
            width=8,
            height=2,
            bg="#F44336",  # Warna merah untuk tombol clear
            fg="white",
            command=lambda x=button_text: on_button_click(x)
        )
    else:
        btn = tk.Button(
            root,
            text=button_text,
            font=("Arial", 24),
            width=8,
            height=2,
            bg="#E0E0E0",  # Warna abu-abu muda untuk tombol angka
            command=lambda x=button_text: on_button_click(x)
        )
    
    # Menyimpan warna asli tombol sebagai atribut Python
    btn.original_bg = btn["bg"]

    # Menambahkan efek hover
    btn.bind("<Enter>", lambda event, b=btn: on_enter(event, b))
    btn.bind("<Leave>", lambda event, b=btn: on_leave(event, b))

    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")  # Padding diperbesar
    col += 1
    if col > 3:
        col = 0
        row += 1

# Konfigurasi grid agar tombol dapat menyesuaikan ukuran jendela
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Menjalankan loop utama GUI
root.mainloop()
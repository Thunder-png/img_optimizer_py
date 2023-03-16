import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image

# Yeniden boyutlandırma fonksiyonu


def resize(size, file):
    # Resizing
    im = PIL.Image.open(file)
    im = im.resize(size)
    im.save("Image_resize.jpg")
    messagebox.showinfo("Başarılı", "Dosya Yeniden Boyutlandırıldı.")


def compress(file_path, quality):
    # Compressing
    im = PIL.Image.open(file_path)
    im.save(file_path, optimize=True, quality=quality)
    messagebox.showinfo("Başarılı", "Dosya sıkıştırıldı.")

# Kullanıcıdan dosya almak için open file fonksiyonu oluşturdum(tkinter-filedialog özelliği)


def open_file():
    file_path = filedialog.askopenfilename()
    print("Seçilen dosya:", file_path)
    size = (int(width_entry.get()), int(height_entry.get()))
    resize(size, file_path)


def open_compress():
    file_path = filedialog.askopenfilename()
    print("Seçilen dosya:", file_path)
    quality = quality_var.get()
    compress(file_path, quality)


# Uygulama Başlığı
root = tk.Tk()
root.title("Resim Düzenleme Uygulaması")
header_label = tk.Label(
    root, text="Resim Düzenleme Uygulaması", font=("Arial", 16))
header_label.pack(pady=10)
# Pencer Boyutu
width = 600
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
# Kalite Label'i
quality_label = tk.Label(root, text="Kalite (%0-100):", font=("Arial", 12))
quality_label.pack(pady=10)

quality_var = tk.IntVar()
quality_scale = tk.Scale(root, from_=0, to=100,
                         variable=quality_var, orient=tk.HORIZONTAL)
quality_scale.pack(pady=10)


# Genişlik Label'i
width_label = tk.Label(root, text="Genişlik:", font=("Arial", 12))
width_label.pack(pady=5)

width_entry = tk.Entry(root, font=("Arial", 12), bg="#F0F0F0")
width_entry.pack(pady=5)
# Yükseklik Label'i
height_label = tk.Label(root, text="Yükseklik:", font=("Arial", 12))
height_label.pack()

height_entry = tk.Entry(root, font=("Arial", 12), bg="#F0F0F0")
height_entry.pack(pady=5)
# Button oluşturulması ve Dosya aç(open_file) fonksiyonunun çağırılmasın
button_resize = tk.Button(root, text="Yeniden Boyutlandır",
                          command=open_file, bg="green", fg="white", font=("Arial", 12), relief="groove")
button_resize.pack(pady=10)

button_compress = tk.Button(
    root, text="Sıkıştır", command=open_compress, bg="blue", fg="white", font=("Arial", 12), relief="groove")
button_compress.pack(pady=10)


root.mainloop()

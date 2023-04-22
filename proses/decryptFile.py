from tkinter import *
from tkinter import filedialog
root = Tk()
class WindowDraggable():
    def __init__(self, label):
        self.label = label
        label.bind('<ButtonPress-1>', self.StartMove)
        label.bind('<ButtonRelease-1>', self.StopMove)
        label.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
        y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
        root.geometry("+%s+%s" %(x, y))

class DecryptFile:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOWS", self.tutup)
        lebar = 660
        tinggi = 250
        setTengahX = (self.parent.winfo_screenwidth() - lebar) // 2
        setTengahY = (self.parent.winfo_screenheight() - tinggi) // 2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        self.parent.overrideredirect(1)
        self.parent.configure(bg = "#75a3a3")
        self.aturKomponen()

    def tutup(self, event = None):
        self.parent.withdraw()
 
    def buka(self, event = None):
        self.deiconify()
 
    def proses(self, event = None):
        try:
            # mengambil path file dari entryDecryptFile yang ada di fungsi aturKomponen
            path = self.entryDecryptFile.get()
            
            # mengambil decryption key dari entryKeyFile yang ada di fungsi aturKomponen
            key = int(self.entryKeyFile.get())
            
            # print path file dan decryption key itu
            # kita menggunakan
            print('The path of file : ', path)
            print('Key for decryption : ', key)
            
            # buka file untuk tujuan reading (membaca)
            fin = open(path, 'rb')

            # menyimpan data file dalam variable "file"
            file = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            file = bytearray(file)

            # melakukan operasi XOR pada setiap nilai bytearray
            for index, values in enumerate(file):
                file[index] = values ^ key

            # membuka file dengan tujuan writing (menulis)
            fin = open(path, 'wb')
            
            # menulis data terenkripsi dalam file
            fin.write(file)
            fin.close()
            print('Decryption Done...')

        except Exception:
            print('Error caught : ', Exception.__name__)

    def browse_file(self):
        filetypes = (
            ('all files', '*.*'),
            ('text files', '*.txt'),
            ('Python files', '*.py'),
            ('Image files', '*.jpg;*.png'),
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )

        if filename:
            self.entryDecryptFile.delete(0, END)
            self.entryDecryptFile.insert(0, filename)

    def pro(self, event):
        self.proses()

    def aturKomponen(self):
        frameUtama = Frame(root, width=400, height=300, bg="#75a3a3")
        frameUtama.grid(row=0, column=1)
        WindowDraggable(frameUtama)
        self.buttonX = Button(frameUtama, text="X", fg="white", bg="#ff0000", width=6, height=2, bd=0, activebackground="#fb8072", activeforeground="white", command=self.tutup, relief=FLAT)
        self.buttonX.grid(row=0, column=0)

        self.labelDecryptFile = Label(frameUtama, text="Encrypt File: ", bg="#c2d6d6", fg="black", font=("Helvetica", 12), width=12, height=2)
        self.labelDecryptFile.grid(row=1, column=1, pady=6)

        self.fileButton = Button(frameUtama, text="Browse", command=self.browse_file, fg="white", bg="#0066ff", width=10, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.fileButton.grid(row=1, column=3, pady=6, sticky="w")

        self.labelKeyFile = Label(frameUtama, text="Key Encrypt: ", bg="#c2d6d6", fg="black", font=("Helvetica", 12), width=12, height=2)
        self.labelKeyFile.grid(row=2, column=1, )

        self.labelNote = Label(frameUtama, text="Note: ", bg="#75a3a3", fg="red", font=("Helvetica", 12), width=12, height=2)
        self.labelNote.grid(row=3, column=1)

        self.entryDecryptFile = Entry(frameUtama, fg="black", bg="#c2d6d6", font=("Helvetica", 12), width=40, bd=11, relief=FLAT)
        self.entryDecryptFile.grid(row=1, column=2)
        self.entryDecryptFile.focus_set()

        self.entryKeyFile = Entry(frameUtama, show="*", fg="black", bg="#c2d6d6", font=("Helvetica", 12), width=40, bd=11, relief=FLAT)
        self.entryKeyFile.grid(row=2, column=2)
        self.entryKeyFile.bind('<Return>', self.pro)

        self.labelNote = Label(frameUtama, text="Key Decrypt will be same from Key Encrypt", fg="red", bg="#75a3a3", font=("Helvetica", 12), width=40, bd=11, relief=FLAT)
        self.labelNote.grid(row=3, column=2, pady=6)

        self.buttonDecryptFile = Button(frameUtama, text="Encrypt File", command=self.proses, fg="white", bg="#0066ff", width=10, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.buttonDecryptFile.grid(row=4, column=2, pady=6, sticky="e")

def main():
    DecryptFile(root, ":: Encrypt & Decrypt ::")
    DecryptFile.buka(root)
    root.mainloop()
main()
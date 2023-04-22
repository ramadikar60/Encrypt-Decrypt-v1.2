from tkinter import *
from tkinter import filedialog
import os
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

class DecryptFolder:
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
        pathdir = self.entryDecryptFolder.get()
        
        key = int(self.entryKeyFolder.get())

        files = []
        
        print('The path of file : ', pathdir)
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)

        obj = os.scandir(pathdir)
        for item in obj:
            if item.is_file():
                files.append(item.path)
            
        try:
            for item in files:
                print(item)

                path = item
                
                fin = open(path, 'rb')
                
                image = fin.read()
                fin.close()
                
                image = bytearray(image)

                for index, values in enumerate(image):
                    image[index] = values ^ key

                fin = open(path, 'wb')
                
                fin.write(image)
                fin.close()
            print('Decryption Done...')

        except Exception:
            print('Error caught : ', Exception.__name__)

    def browse_folder(self):
        foldername = filedialog.askdirectory(
            title='Select a folder',
            initialdir='/'
        )

        if foldername:
            self.entryDecryptFolder.delete(0, END)
            self.entryDecryptFolder.insert(0, foldername)

    def pro(self, event):
        self.proses()

    def aturKomponen(self):
        frameUtama = Frame(root, width=400, height=300, bg="#75a3a3")
        frameUtama.grid(row=0, column=1)
        WindowDraggable(frameUtama)
        self.buttonX = Button(frameUtama, text="X", fg="white", bg="#ff0000", width=6, height=2, bd=0, activebackground="#fb8072", activeforeground="white", command=self.tutup, relief=FLAT)
        self.buttonX.grid(row=0, column=0)
        self.labelDecryptFolder = Label(frameUtama, text="Decrypt Folder: ", bg="#c2d6d6", fg="black", font=("Helvetica", 12), width=12, height=2)
        self.labelDecryptFolder.grid(row=1, column=1, pady=6)

        self.fileButton = Button(frameUtama, text="Browse", command=self.browse_folder, fg="white", bg="#0066ff", width=10, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.fileButton.grid(row=1, column=3, pady=6, sticky="w")

        self.labelKeyFolder = Label(frameUtama, text="Key Decrypt: ", bg="#c2d6d6", fg="black", font=("Helvetica", 12), width=12, height=2)
        self.labelKeyFolder.grid(row=2, column=1, )

        self.labelNote = Label(frameUtama, text="Note: ", bg="#75a3a3", fg="red", font=("Helvetica", 12), width=12, height=2)
        self.labelNote.grid(row=3, column=1)

        self.entryDecryptFolder = Entry(frameUtama, fg="black", bg="#c2d6d6", font=("Helvetica", 12), width=40, bd=11, relief=FLAT)
        self.entryDecryptFolder.grid(row=1, column=2)
        self.entryDecryptFolder.focus_set()

        self.entryKeyFolder = Entry(frameUtama, show="*", fg="black", bg="#c2d6d6", font=("Helvetica", 12), width=40, bd=11, relief=FLAT)
        self.entryKeyFolder.grid(row=2, column=2)
        self.entryKeyFolder.bind('<Return>', self.pro)

        self.labelNote = Label(frameUtama, text="Key Decrypt will be same from Key Encrypt", fg="red", bg="#75a3a3", font=("Helvetica", 12), width=40, bd=11, relief=FLAT)
        self.labelNote.grid(row=3, column=2, pady=6)

        self.buttonDecryptFolder = Button(frameUtama, text="Decrypt Folder", command=self.proses, fg="white", bg="#0066ff", width=12, height=2, bd=0, activebackground="whitesmoke", activeforeground="#444")
        self.buttonDecryptFolder.grid(row=4, column=2, pady=6, sticky="e")

def main():
    DecryptFolder(root, ":: Encrypt & Decrypt ::")
    DecryptFolder.buka(root)
    root.mainloop()
main()
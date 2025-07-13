from tkinter import *
from tkinter import filedialog,messagebox
t=Tk()
class My_Notepad:
    global current_open_file
    def new_file(self):
        self.x = self.txt_area.get(1.0, END)
        if self.x.strip() == '':
            pass
        else:
            print(self.x)
            self.res = messagebox.askyesnocancel("Save File Confirmation", 'Do you want to Save this file?')
            if self.res == True:
                self.saveAs_file()
            elif self.res == False:
                self.txt_area.delete(1.0, END)
    def new_window(self):
        new_root = Tk()
        My_Notepad(new_root)

    def open_file(self):
        self.x = self.txt_area.get(1.0, END)
        if self.x.strip() == '':
            global current_open_file
            f = filedialog.askopenfile(initialdir="/",
                                       filetypes=[('All Files', '*.*'), ('Text File', '*.txt')])
            self.current_open_file = f
            for data in f:
                self.txt_area.insert(INSERT, data)
        else:
            print(self.x)
            self.res = messagebox.askyesnocancel("Save File Confirmation", 'Do you want to Save this file?')
            if self.res == True:
                self.saveAs_file()
            elif self.res == False:
                self.txt_area.delete(1.0, END)
    def save_file(self):
        if self.current_open_file == 'no file selected':
            self.saveAs_file()
        else:
            self.s = open(self.current_open_file.name, mode='w')
            self.data = self.txt_area.get(1.0, END)
            self.s.write(self.data)
    def saveAs_file(self):
        self.d = filedialog.asksaveasfile(defaultextension=".txt", mode='w')
        self.data = self.txt_area.get(1.0, END)
        self.d.write(self.data)
    def exit(self):
        pass


    def __init__(self,screen):
        self.screen=screen
        screen.title("My Notepad")
        screen.wm_iconbitmap(r'C:\Users\Aniket\Desktop\installer\icon.ico')
        self.txt_area=Text(screen,padx=10,pady=10,wrap=WORD,font=('Arial',10,'normal'))
        self.txt_area.pack(fill=BOTH,expand=1)

        self.main_menu=Menu()
        self.screen.config(menu=self.main_menu)
        self.file_menu=Menu(self.main_menu,tearoff=0)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label='New',accelerator='Ctrl+N',command=self.new_file)
        self.file_menu.add_command(label='New Window',accelerator='Ctrl+Shift+N',command=self.new_window)
        self.file_menu.add_command(label='Open',accelerator='Ctrl+O',command=self.open_file)
        self.file_menu.add_command(label='Save',accelerator='Ctrl+S',command=self.save_file)
        self.file_menu.add_command(label='Save As',accelerator='Ctrl+Shift+S',command=self.saveAs_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.exit)

        self.edit_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo',accelerator='Ctrl+Z')
        self.edit_menu.add_command(label='Redo',accelerator='Ctrl+Y')
        self.edit_menu.add_command(label='Cut',accelerator='Ctrl+C')
        self.edit_menu.add_command(label='Paste',accelerator='Ctrl+V')
        self.edit_menu.add_command(label='Delete',accelerator='Ctrl+D')
        self.edit_menu.add_command(label='Select All',accelerator='Ctrl+A')

        self.search_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Search",menu=self.search_menu)
        self.search_menu.add_command(label='Find',accelerator='Ctrl+F')
        self.search_menu.add_command(label='Replace',accelerator='Ctrl+R')


m=My_Notepad(t)
t.mainloop()


# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, font
# from tkinter.scrolledtext import ScrolledText
#
# class Notepad:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Python Notepad")
#         self.root.geometry("800x600")
#         self.filename = None
#
#         self.create_widgets()
#         self.create_menu()
#         self.bind_shortcuts()
#         self.update_status()
#
#     def create_widgets(self):
#         self.text_area = ScrolledText(self.root, undo=True, wrap="word")
#         self.text_area.pack(fill="both", expand=1)
#         self.text_area.bind("<<Modified>>", lambda e: self.update_status())
#
#         self.status = tk.StringVar()
#         self.status_bar = tk.Label(self.root, textvariable=self.status, anchor="w")
#         self.status_bar.pack(side="bottom", fill="x")
#
#     def create_menu(self):
#         menu_bar = tk.Menu(self.root)
#         self.root.config(menu=menu_bar)
#
#         # File menu
#         file_menu = tk.Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="File", menu=file_menu)
#         file_menu.add_command(label="New Window", command=self.new_window, accelerator="Ctrl+Shift+N")
#         file_menu.add_command(label="New File", command=self.new_file, accelerator="Ctrl+N")
#         file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
#         file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
#         file_menu.add_command(label="Save As", command=self.save_as)
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", command=self.root.quit)
#
#         # Edit menu
#         edit_menu = tk.Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="Edit", menu=edit_menu)
#         edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
#         edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
#         edit_menu.add_separator()
#         edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
#         edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
#         edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
#         edit_menu.add_command(label="Delete", command=self.delete_text)
#         edit_menu.add_command(label="Select All", command=lambda: self.text_area.tag_add("sel", "1.0", "end"), accelerator="Ctrl+A")
#
#         # Search menu
#         search_menu = tk.Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="Search", menu=search_menu)
#         search_menu.add_command(label="Find", command=self.find_text, accelerator="Ctrl+F")
#         search_menu.add_command(label="Replace", command=self.replace_text, accelerator="Ctrl+H")
#
#         # Format menu
#         format_menu = tk.Menu(menu_bar, tearoff=0)
#         menu_bar.add_cascade(label="Format", menu=format_menu)
#         format_menu.add_command(label="Font", command=self.choose_font)
#
#     def new_window(self):
#         new_root = tk.Tk()
#         Notepad(new_root)
#
#     def new_file(self):
#         self.x =self.text_area.get(1.0, tk.END)
#         if self.x.strip() == '':
#             pass
#         else:
#             print(self.x)
#             res = messagebox.askyesnocancel("Save File Confirmation", 'Do you want to Save this file?')
#             if res == True:
#                 self.save_as()
#             elif res == False:
#                 self.text_area.delete(1.0, tk.END)
#
#     def open_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#         if file_path:
#             with open(file_path, "r", encoding="utf-8") as file:
#                 self.text_area.delete(1.0, tk.END)
#                 self.text_area.insert(tk.END, file.read())
#             self.filename = file_path
#
#     def save_file(self):
#         if not self.filename:
#             self.save_as()
#         else:
#             with open(self.filename, "w", encoding="utf-8") as file:
#                 file.write(self.text_area.get(1.0, tk.END))
#
#     def save_as(self):
#         file_path = filedialog.asksaveasfilename(defaultextension=".txt",
#                                                  filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#         if file_path:
#             with open(file_path, "w", encoding="utf-8") as file:
#                 file.write(self.text_area.get(1.0, tk.END))
#             self.filename = file_path
#
#     def delete_text(self):
#         try:
#             self.text_area.delete("sel.first", "sel.last")
#         except tk.TclError:
#             pass
#
#     def find_text(self):
#         find = simpledialog.askstring("Find", "Enter text to find:")
#         if find:
#             start = "1.0"
#             while True:
#                 start = self.text_area.search(find, start, stopindex=tk.END)
#                 if not start:
#                     break
#                 end = f"{start}+{len(find)}c"
#                 self.text_area.tag_add("found", start, end)
#                 self.text_area.tag_config("found", background="yellow")
#                 start = end
#
#     def replace_text(self):
#         find = simpledialog.askstring("Replace", "Find:")
#         replace = simpledialog.askstring("Replace", "Replace with:")
#         if find and replace is not None:
#             content = self.text_area.get(1.0, tk.END)
#             new_content = content.replace(find, replace)
#             self.text_area.delete(1.0, tk.END)
#             self.text_area.insert(1.0, new_content)
#
#     def choose_font(self):
#         font_name = simpledialog.askstring("Font", "Enter font family (e.g., Arial):")
#         font_size = simpledialog.askinteger("Size", "Enter font size:", minvalue=6, maxvalue=100)
#         if font_name and font_size:
#             new_font = font.Font(family=font_name, size=font_size)
#             self.text_area.configure(font=new_font)
#
#     def update_status(self):
#         text = self.text_area.get(1.0, tk.END)
#         chars = len(text) - 1
#         words = len(text.split())
#         self.status.set(f"Words: {words}   Characters: {chars}")
#         self.text_area.edit_modified(False)
#
#     def bind_shortcuts(self):
#         self.root.bind("<Control-n>", lambda e: self.new_file())               # New File
#         self.root.bind("<Control-N>", lambda e: self.new_window())             # New Window (Shift+N)
#         self.root.bind("<Control-o>", lambda e: self.open_file())
#         self.root.bind("<Control-s>", lambda e: self.save_file())
#         self.root.bind("<Control-f>", lambda e: self.find_text())
#         self.root.bind("<Control-h>", lambda e: self.replace_text())
#         self.root.bind("<Control-a>", lambda e: self.text_area.tag_add("sel", "1.0", "end"))
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Notepad(root)
#     root.mainloop()


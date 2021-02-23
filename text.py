import tkinter as tk
from tkinter import filedialog

class Menubar:
    def __init__(self,parent):
        font_specs = ("ubuntu", 14)
        menubar = tk.Menu(parent.master,font=font_specs)
        parent.master.config(menu=menubar)



        file_dropdown = tk.Menu(menubar,font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File",accelerator="Ctrl  +N",command=parent.new_file)
        file_dropdown.add_command(label="Open File",accelerator="Ctrl  +O",command=parent.open_file)
        file_dropdown.add_command(label="Save",accelerator="Ctrl  +S",command=parent.save_file)
        file_dropdown.add_command(label="Save As",accelerator="Ctrl+Shift+S",command=parent.save_as)

        file_dropdown.add_separator()


        file_dropdown.add_command(label="Exit",command=parent.master.destroy)

        menubar.add_cascade(label="File" , menu=file_dropdown)



class Statusbar:
    def __init__(self, parent):

        font_specs = ("ubuntu", 12)

        self.status = tk.StringVar()
        self.status.set("PyText -0.1 Gutenberg")
        label = tk.Label(parent.textarea, textvariable=self.status, fg="black", anchor='sw', font=font_specs)

        label.pack(side=tk.BOTTOM, fill=tk.BOTH)


class PyText:
    def __init__(self, master):

       master.title("Untitled - PyText")
       master.geometry("1200x700")

       font_specs = ("ubuntu", 18)

       self.master = master
       self.filename = None

       self.textarea = tk.Text(master ,font=font_specs)
       self.scroll = tk.Scrollbar(master,command=self.textarea.yview)
       self.textarea.configure(yscrollcommand=self.scroll.set)
       self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       self.scroll.pack(side=tk.RIGHT, fill=tk.Y)



       self.menubar = Menubar(self)
       self.statusbar = Statusbar(self)
       self.bind_shortcuts()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name +"-PyText")
        else:
            self.master.title("Untitled PyText")



    def new_file(self, *args):
       self.textarea.delete(1.0, tk.END)
       self.filename = None
       self.set_window_title(self.filename)


    def open_file(self,*args):
       self.filename = filedialog.askopenfilename(defaultextention = ".txt", filetypes=[("All Files", "*.*"),("Text File", "*.txt"),("Python File", "*.py"),("Markdown", "*.md"),("JavaScript", "*.js"),("HTML Documents", "*.html"),("Css Documnets", "*.css")])
       if self.filename:
           self.textarea.delete(1.0, tk.END)
           with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
           self.set_window_title(self.filename)



    def save_file(self,*args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename,"w") as f:
                    f.write(textarea_content)
            except Exception as e:
               print(e)
        else:
            self.save_as()


    def save_as(self):
        try:
            new_file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextention = ".txt", filetypes=[("All Files", "*.*"),("Text File", "*.txt"),("Python File", "*.py"),("Markdown", "*.md"),("JavaScript", "*.js"),("HTML Documents", "*.html"),("Css Documnets", "*.css")] )
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
           print(e)

    def exit_file(self):
        pass

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        #self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)






if __name__=="__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()

from tkinter import filedialog
from tkinter import *
from test import test


class Application:

    def __init__(self, master):
        master.title("Image - SerialN")
        master.minsize(width=800, height=400)
        master.config(padx=50, pady=50)
        
        
        def browse_button():
            # Allow user to select a directory and store it in global var
            # called folder_path
            self.folder_path = filedialog.askdirectory()
            self.entry.config(state="normal")
            self.entry.delete(0, END)
            self.entry.insert(0, self.folder_path)
            self.entry.config(state="disabled")
            

        def on_click(event):
            event.widget.delete(0, END)

        self.div_canvas0 = Canvas(width=100, height=70, bd=0, highlightthickness=0)
        self.div_canvas0.grid(row=0, column=1)

        self.hint = Label(text="Please provide a path to a folder", font=("Arial", 18, "bold"))
        self.hint.grid(row=1, column=1)

        self.entry = Entry(width=50)
        self.entry.insert(END, string="Please browse for a folder", )
        self.entry.config(state="disabled")
        self.entry.bind("<Button-1>", on_click)
        self.entry.grid(row=2, column=1, padx='10', pady='10',)

        self.browse = Button(text="Browse", command=browse_button)
        self.browse.grid(row=2, column=2, padx='5', pady='10',)

        self.folder_path = self.entry.get()

        self.run_button = Button(text="Stamp Serials", command=lambda: test(self.folder_path))
        self.run_button.grid(row=3, column=3, padx='5', pady='10')


# Initialize the app
root = Tk()
app = Application(root)

# Keep start menu open
root.mainloop()
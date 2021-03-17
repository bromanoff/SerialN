from tkinter import filedialog
from tkinter import *
from serial import stamp


class Application:
    # Create the window
    def __init__(self, master):
        master.title("Image - SerialN")
        master.minsize(width=800, height=400)
        master.config(padx=50, pady=50)
        
        # Button functionality
        def browse_button():
            self.folder_path = filedialog.askdirectory()
            self.entry.config(state="normal")
            self.entry.delete(0, END)
            self.entry.insert(0, self.folder_path)
            self.entry.config(state="disabled")
            print(f"Folder path {self.folder_path}")
            
        # Get the starting number for the serial stamping
        def get_start():
            self.starting_number = self.spinbox.get()
            # print(f"Starting num: {self.starting_number}")


        self.div_canvas0 = Canvas(width=100, height=70, bd=0, highlightthickness=0)
        self.div_canvas0.grid(row=0, column=1)

        # Path call to action
        self.path_hint = Label(text="Please provide a path to a folder", font=("Arial", 14))
        self.path_hint.grid(row=1, column=1)

        # Uneditable entry showing the folder path
        self.entry = Entry(width=50)
        self.entry.insert(END, string="Browse for a folder")
        self.entry.config(state="disabled")
        self.entry.grid(row=2, column=1, padx='10', pady='10',)
        self.folder_path = ""

        self.browse = Button(text="Browse", command=browse_button)
        self.browse.grid(row=2, column=2, padx='5', pady='10',)

        # Spinbox call to action
        self.spinbox_hint = Label(text="Enter a starting number. Leave empty to continue on last number.", font=("Arial", 14))
        self.spinbox_hint.grid(row=3, column=1)

        self.spinbox = Spinbox(from_=0, to=99999, width=5)
        self.spinbox.delete(0)
        self.spinbox.grid(row=3, column=2)

        self.status = Label(text="Status: Ready", font=("Arial", 14))
        self.status.grid(row=4, column=1)
        
        def set_status(status):
            self.status.config(text=f"Status: {status}")

        # Run button calling set_status and the stamping function that creates the serial numbers
        self.run_button = Button(text="Stamp Serials", command=lambda: [get_start(), set_status(stamp(self.folder_path, self.starting_number))])
        self.run_button.grid(row=4, column=3, padx='5', pady='10')

from customtkinter import *
from tkinter import filedialog

Window = CTk()
Window.geometry('380x520')
Window.title('Simple Notes')
Window.resizable(False, False)

set_default_color_theme('blue')

def theme_change():
    if get_appearance_mode() == "Dark":
        set_appearance_mode("light")
    else:
        set_appearance_mode("dark")

def create_note():
    TabNames = Tabview._tab_dict.keys()
    NumericTabNames = [int(name) for name in TabNames if name.isdigit()]

    if len(NumericTabNames) >= 10:
        return

    if NumericTabNames:
        NextNote = max(NumericTabNames) + 1
    else:
        NextNote = 1

    Tabview.add(str(NextNote))
    CTkTextbox(master = Tabview.tab(str(NextNote)), font = ('Dubai', 12), width = 320, height = 420, wrap = WORD).pack()

def close_note():
    if Tabview.get() != '🏠':
        Tabview.delete(Tabview.get())

def save_note():
    if Tabview.get() != '🏠':
        content = Tabview.tab(Tabview.get()).winfo_children()[0].get("1.0", "end-1c").strip()
        if content:
            with open(filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")]), 'w') as file:
                file.write(content)
            show_saved_message()
        else:
            show_error_message()

def show_saved_message():
    SavedLabel = CTkLabel(master = ContainerFrame, text = "Note Saved", font = ('Dubai', 12, 'bold'), text_color = 'green')
    SavedLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    Window.after(5000, SavedLabel.destroy)

def show_error_message():
    ErrorLabel = CTkLabel(master = ContainerFrame, text = "Error: Empty Note", font = ('Dubai', 12, 'bold'), text_color = 'red')
    ErrorLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    Window.after(5000, ErrorLabel.destroy)

def open_note():
    if Tabview.get() !=  '🏠':
        file = open(filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Text files", "*.txt")]), 'r')

        next((tb for tb in Tabview.tab(Tabview.get()).winfo_children() if isinstance(tb, CTkTextbox)), None).delete("1.0", "end")
        next((tb for tb in Tabview.tab(Tabview.get()).winfo_children() if isinstance(tb, CTkTextbox)), None).insert("1.0", file.read())

Tabview = CTkTabview(master = Window)
Tabview.add('🏠')
Tabview.pack()

CTkLabel(master = Tabview.tab('🏠'), text = 'Simple Notes', font = ('Dubai', 24, 'bold'), text_color = '#1F6AA9').pack(side = TOP)
CTkLabel(master = Tabview.tab('🏠'), text = 'Welcome To Simple Notes!', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = Tabview.tab('🏠'), text = 'Press 🎨 to change between light and dark mode.', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = Tabview.tab('🏠'), text = 'Press ➕ to create a new note.', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = Tabview.tab('🏠'), text = 'Press ❌ to delete a note.', font = ('Dubai', 12)).pack(side = TOP)

CTkLabel(master = Tabview.tab('🏠'), text = 'Press 💾 to save a note.', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = Tabview.tab('🏠'), text = 'Press 📂 to open a note.', font = ('Dubai', 12)).pack(side = TOP)

ContainerFrame = CTkFrame(master = Window)
ContainerFrame.pack(pady = 5)

NoteFrame  =  CTkFrame(master = ContainerFrame)

CTkButton(master = NoteFrame, text = '🎨', font = ('Dubai', 10), width = 20, height = 20, command = theme_change).pack(side = 'left', padx = 3, pady = 3)
CTkButton(master = NoteFrame, text = '➕', font = ('Dubai', 8), width = 22, height = 22, command = create_note).pack(side = 'left')
CTkButton(master = NoteFrame, text = '❌', font = ('Dubai', 8), width = 22, height = 22, command = close_note).pack(side = 'left', padx = 3, pady = 3)

NoteFrame.pack(side = 'left', padx = 5, pady = 5)

SpaceFrame = CTkFrame(master = ContainerFrame, width = 0, height = 0)
SpaceFrame.pack(side = 'left', padx = 60)

FileFrame = CTkFrame(master = ContainerFrame)

CTkButton(master = FileFrame, text = '💾', font = ('Dubai', 10), width = 20, height = 20, command = save_note).pack(side = 'left', padx = 3, pady = 3)
CTkButton(master = FileFrame, text = '📂', font = ('Dubai', 10), width = 22, height = 22, command = open_note).pack(side = 'left')

FileFrame.pack(side = 'left', padx = 5, pady = 5)

Window.mainloop()

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
def openfile():
    filepath = askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,tk.END)
    with open(filepath,"r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END,text)
        window.title(f"HandalTextEditor-{filepath}")
def savefile():
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text = txt_edit.get(1.0,tk.END)
        output_file.write(text)
        window.title(f"HandalTextEditor-{filepath}")
window = tk.Tk()
window.title("Handal-TextEditor")
window.rowconfigure(0,minsize=600)
window.columnconfigure(1,minsize=800)
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window,relief=tk.RAISED)
open_button = tk.Button(frame_buttons,text="Open File",command=openfile)
save_button = tk.Button(frame_buttons,text="Save As",command=savefile)
open_button.grid(column=0, row=0, sticky="ew",padx=5,pady=5)
save_button.grid(column=0, row=1, sticky="ew",padx=5,pady=5)
frame_buttons.grid(column=0, row=0,sticky="ns")
txt_edit.grid(column=1,row=0,sticky="nsew")
window.mainloop()
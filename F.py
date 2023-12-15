import os
import shutil
import lang
import torch
from torch import tensor
from tensorflow import keras
import scipy
from scipy import special
import tkinter as tk
from tkinter import filedialog

class Path(lang.Class):
    
    @staticmethod
    def start(fname):
        return Path(os.path.dirname(os.path.abspath(fname)))
    
    def __init__(self, p):
        self.p = os.path.abspath(p)
    
    def __str__(self):
        return self.p
    
    def __eq__(self, other):
        other_path = os.path.abspath(other) if isinstance(other, str) else other.p
        return self.p == other_path
    
    def __add__(self, p):
        new_path = os.path.join(self.p, os.path.normpath(p))
        return Path(new_path)
    
    def isfile(self):
        return os.path.isfile(self.p)
    
    def isdir(self):
        return os.path.isdir(self.p)
    
    def mkdir(self):
        os.makedirs(self.p, exist_ok=True)
    
    def rm(self):
        os.remove(self.p)
    
    def rmdir(self):
        shutil.rmtree(self.p)


tensor_example = tensor([1, 2, 3])
print(tensor_example)


model = keras.Sequential()
model.add(keras.layers.Dense(10, activation='relu', input_shape=(10,)))
print(model.summary())


print(special.exp10(2))

class GUIApp:
    def __init__(self, master):
        self.master = master
        master.title("File Operations")

        self.label = tk.Label(master, text="Enter File Path:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Check File Existence", command=self.check_existence)
        self.button.pack()

    def check_existence(self):
        file_path = self.entry.get()
        path_obj = Path(file_path)
        if path_obj.isfile():
            result = f"{file_path} exists and is a file."
        elif path_obj.isdir():
            result = f"{file_path} exists and is a directory."
        else:
            result = f"{file_path} does not exist."
        tk.messagebox.showinfo("File Existence", result)

# Create the Tkinter window
root = tk.Tk()
app = GUIApp(root)
root.mainloop()




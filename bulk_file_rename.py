# import os

# def bulk_rename_files(directory_path, old_word, new_word, add_numbering=False):
#     # 1. Check karein ke folder exist karta hai ya nahi
#     if not os.path.exists(directory_path):
#         print("Error: Folder path sahi nahi hai!")
#         return

#     # 2. Folder ki tamam files ki list nikalain
#     files = os.listdir(directory_path)
#     count = 1

#     print("\n--- Renaming Started ---")
#     for filename in files:
#         # Full path banayein
#         old_file_path = os.path.join(directory_path, filename)

#         # Sirf files ko rename karein (folders ko nahi)
#         if os.path.isfile(old_file_path):
#             # File name aur Extension ko alag karein (e.g., 'image' aur '.jpg')
#             name, extension = os.path.splitext(filename)

#             # File name mein word replace karein
#             new_name = name.replace(old_word, new_word)

#             # Agar numbering (1, 2, 3) add karni ho
#             if add_numbering:
#                 new_filename = f"{new_name}_{count}{extension}"
#             else:
#                 new_filename = f"{new_name}{extension}"

#             new_file_path = os.path.join(directory_path, new_filename)

#             # 3. File rename karne ki main command
#             os.rename(old_file_path, new_file_path)
#             print(f"Renamed: '{filename}' -> '{new_filename}'")
#             count += 1

#     print("--- Renaming Finished Successfully! ---")

# # --- EXECUTION ---
# # Apne folder ka path aur terms enter karein:
# folder_path = r"C:\Users\YourName\Desktop\TestFolder"
# word_to_find = "IMG"
# word_to_replace = "Vacation"

# # Call Function
# bulk_rename_files(folder_path, word_to_find, word_to_replace, add_numbering=True)

# Second Code
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder)

def start_renaming():
    folder = folder_entry.get()
    prefix = prefix_entry.get()
    
    if not folder or not os.path.exists(folder):
        messagebox.showerror("Error", "Bhai, sahi folder select karo!")
        return

    files = os.listdir(folder)
    count = 1
    
    for filename in files:
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            new_filename = f"{prefix}_{count}{ext}" if prefix else f"File_{count}{ext}"
            new_path = os.path.join(folder, new_filename)
            
            os.rename(old_path, new_path)
            count += 1

    messagebox.showinfo("Success", f"{count - 1} Files successfully rename ho gayin!")

# --- GUI Window Setup ---
app = tk.Tk()
app.title("Bulk File Renamer")
app.geometry("400x250")

# Folder Selection UI
tk.Label(app, text="Select Folder:").pack(pady=5)
folder_entry = tk.Entry(app, width=40)
folder_entry.pack()
tk.Button(app, text="Browse Folder", command=select_folder).pack(pady=5)

# New Name Prefix UI
tk.Label(app, text="New File Name / Prefix:").pack(pady=5)
prefix_entry = tk.Entry(app, width=30)
prefix_entry.pack()

# Rename Button
tk.Button(app, text="Rename All Files", bg="green", fg="white", command=start_renaming).pack(pady=20)

app.mainloop()
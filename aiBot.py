import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import zipfile
import os
import json

class AIbotApp:
    def __init__(self, root):
        self.root = root
        root.title('AI Bot - Drag and Drop Event Logs')
        
        self.label = tk.Label(root, text="Drag and drop a zip file here", width=60, height=4)
        self.label.pack(padx=10, pady=10)

        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.process_zip_file)

    def process_zip_file(self, event):
        file_path = event.data
        if file_path.endswith('.zip'):
            self.label.config(text=f"Processing {os.path.basename(file_path)}...")
            self.extract_and_process_zip(file_path)
            self.label.config(text="Drag and drop a zip file here")
        else:
            self.label.config(text="Please drop a zip file.")

    def extract_and_process_zip(self, zip_path):
        # Extract zip file and process contents
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            extract_path = os.path.splitext(zip_path)[0]
            zip_ref.extractall(extract_path)

            # Process extracted files
            for foldername, subfolders, filenames in os.walk(extract_path):
                for filename in filenames:
                    if filename.endswith('.evtx') or filename.endswith('.json'):
                        file_path = os.path.join(foldername, filename)
                        # Add your logic here to process each file
                        print(f"Processing {file_path}...")

                        # Example: Load JSON data
                        if filename.endswith('.json'):
                            with open(file_path, 'r') as json_file:
                                data = json.load(json_file)
                                # Process JSON data
                                print(data)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = AIbotApp(root)
    root.mainloop()

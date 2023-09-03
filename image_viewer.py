import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def _init_(self, root):
        self.root = root
        self.root.title("Image Viewer")
        
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.button_open = tk.Button(root, text="Open Image", command=self.open_image)
        self.button_open.pack()
        
        self.image = None
        self.image_tk = None
    
    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_path:
            self.load_image(file_path)
    
    def load_image(self, file_path):
        image = Image.open(file_path)
        self.image = image
        self.image_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
    
if __name_ == "_main_":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
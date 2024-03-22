from helpers import apply_ace_filter
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessorGUIPart1:
    def __init__(self, root):
        self.root = root
        self.root.title("Part 1")

        self.image_path = "cat_picture.jpeg"
        self.image = Image.open(self.image_path)
        self.processed_image = None
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.display_image(self.image)

        self.k1_label = tk.Label(root, text="Enter k1:")
        self.k1_label.pack()
        self.k1_entry = tk.Entry(root)
        self.k1_entry.pack()

        self.k2_label = tk.Label(root, text="Enter k2:")
        self.k2_label.pack()
        self.k2_entry = tk.Entry(root)
        self.k2_entry.pack()

        self.window_size_label = tk.Label(root, text="Enter window size:")
        self.window_size_label.pack()
        self.window_size_entry = tk.Entry(root)
        self.window_size_entry.pack()

        tk.Button(root, text="Apply Ace Filter", command=self.apply_ace).pack()

    def apply_ace(self):
        k1 = float(self.k1_entry.get())
        k2 = float(self.k2_entry.get())
        window_size = int(self.window_size_entry.get())
        self.processed_image = apply_ace_filter(self.image, window_size, k1, k2)
        self.display_image(self.processed_image)

    def display_image(self, img):
        img_thumbnail = img.copy()
        img_thumbnail.thumbnail((250, 250))
        imgtk = ImageTk.PhotoImage(image=img_thumbnail)
        self.image_label.configure(image=imgtk)
        self.image_label.image = imgtk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorGUIPart1(root)
    root.mainloop()

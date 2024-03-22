import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from main import apply_histogram_specification

class ImageProcessorGUIPart2:
    def __init__(self, root):
        self.root = root
        self.root.title("Part 2")

        self.image_path_ref = "reference_image.jpeg"
        self.image_path_tar = "target_image.png"

        self.image_ref = Image.open(self.image_path_ref)
        self.image_tar = Image.open(self.image_path_tar)

        self.processed_image = None

        self.ref_label = tk.Label(root)
        self.ref_label.pack()
        self.display_image(self.image_ref, self.ref_label)

        self.tar_label = tk.Label(root)
        self.tar_label.pack()
        self.display_image(self.image_tar, self.tar_label)

        tk.Button(root, text="Apply Histogram Specification", command=self.apply_histogram).pack()

    def apply_histogram(self):
        self.processed_image = apply_histogram_specification(self.image_ref, self.image_tar)
        self.display_image(self.processed_image, self.tar_label)

    def display_image(self, img, label):
        img_thumbnail = img.copy()
        img_thumbnail.thumbnail((250, 250))
        imgtk = ImageTk.PhotoImage(image=img_thumbnail)
        label.configure(image=imgtk)
        label.image = imgtk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorGUIPart2(root)
    root.mainloop()

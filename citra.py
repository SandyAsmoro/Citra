import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageFilter
import numpy as np
from skimage import exposure

class ImageEnhancementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Enhancement")
        self.root.geometry("1100x700")

        self.input_image = None
        self.output_image = None

        self.brightness_scale = None
        self.blur_scale = None

        self.create_widgets()

    def create_widgets(self):
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.TOP, padx=20, pady=20)

        input_label = tk.Label(input_frame, text="Input Image Path:")
        input_label.pack()

        self.input_entry = tk.Entry(input_frame, width=50)
        self.input_entry.pack()

        browse_button = tk.Button(input_frame, text="Browse", command=self.choose_file)
        browse_button.pack(pady=5)

        # Input image frame
        input_image_frame = tk.Frame(self.root)
        input_image_frame.pack(side=tk.LEFT, padx=20, pady=10)

        self.input_box = tk.Label(input_image_frame, relief=tk.SOLID, width=400, height=400)
        self.input_box.pack(side=tk.LEFT, padx=20)
        
        # Enhancement buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(side=tk.LEFT, padx=20)

        self.brightness_label = tk.Label(buttons_frame, text="Brightness")
        self.brightness_label.pack()
        
        self.brightness_scale = tk.Scale(buttons_frame, from_=0, to=2, resolution=0.1, orient=tk.HORIZONTAL, length=200)
        self.brightness_scale.set(1.0)
        self.brightness_scale.pack(pady=5)

        self.brightness_button = tk.Button(buttons_frame, text="Apply Brightness", command=self.apply_brightness)
        self.brightness_button.pack(pady=5)

        self.blur_label = tk.Label(buttons_frame, text="Blur")
        self.blur_label.pack()
        
        self.blur_scale = tk.Scale(buttons_frame, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL, length=200)
        self.blur_scale.set(0)
        self.blur_scale.pack(pady=5)

        self.blur_button = tk.Button(buttons_frame, text="Apply Blur", command=self.apply_blur)
        self.blur_button.pack(pady=5)
        
        self.negative_button = tk.Button(buttons_frame, text="Negative", command=self.apply_negative)
        self.negative_button.pack(pady=5)

        self.equalize_button = tk.Button(buttons_frame, text="Equalize", command=self.apply_equalize)
        self.equalize_button.pack(pady=5)

        self.histogram_button = tk.Button(buttons_frame, text="Matching", command=self.apply_histogram)
        self.histogram_button.pack(pady=5)

        self.reset_button = tk.Button(buttons_frame, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

        # Output frame
        output_frame = tk.Frame(self.root)
        output_frame.pack(side=tk.LEFT, padx=20, pady=0)

        self.output_box = tk.Label(output_frame, relief=tk.SOLID, width=400, height=400)
        self.output_box.pack(side=tk.LEFT, padx=20)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, file_path)
        self.load_input_image()

    def load_input_image(self):
        input_image_path = self.input_entry.get()
        if input_image_path:
            self.input_image = Image.open(input_image_path)
            self.output_image = self.input_image.copy()
            self.display_input_image()

    def display_input_image(self):
        input_image_resized = self.input_image.resize((400, 400))
        input_photo = ImageTk.PhotoImage(input_image_resized)
        self.input_box.configure(image=input_photo)
        self.input_box.image = input_photo

    def display_output_image(self):
        output_image_resized = self.output_image.resize((400, 400))
        output_photo = ImageTk.PhotoImage(output_image_resized)
        self.output_box.configure(image=output_photo)
        self.output_box.image = output_photo

    def apply_brightness(self):
        if self.input_image is None:
            return

        if self.output_image != self.input_image:
            self.output_image = self.input_image.copy()

        brightness_factor = self.brightness_scale.get()
        enhancer = ImageEnhance.Brightness(self.output_image)
        self.output_image = enhancer.enhance(brightness_factor)
        self.display_output_image()

    def apply_negative(self):
        if self.input_image is None:
            return

        if self.output_image != self.input_image:
            self.output_image = self.input_image.copy()

        self.output_image = ImageOps.invert(self.output_image)
        self.display_output_image()

    def apply_blur(self):
        if self.input_image is None:
            return

        if self.output_image != self.input_image:
            self.output_image = self.input_image.copy()

        radius = self.blur_scale.get()
        self.output_image = self.output_image.filter(ImageFilter.GaussianBlur(radius))
        self.display_output_image()

    def apply_equalize(self):
        if self.input_image is None:
            return

        if self.output_image != self.input_image:
            self.output_image = self.input_image.copy()

        self.output_image = ImageOps.equalize(self.output_image)
        self.display_output_image()

    def apply_histogram(self):
        if self.input_image is None:
            return

        if self.output_image != self.input_image:
            self.output_image = self.input_image.copy()

        reference_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if not reference_image_path:
            return

        reference_image = Image.open(reference_image_path).convert("RGB")
        reference_array = np.array(reference_image)
        output_array = np.array(self.input_image.convert("RGB"))

        matched_array = exposure.match_histograms(output_array, reference_array)

        self.output_image = Image.fromarray(matched_array.astype('uint8'))
        self.display_output_image()

    def reset(self):
        if self.input_image is None:
            return

        self.output_image = self.input_image.copy()
        self.display_output_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEnhancementGUI(root)
    root.mainloop()

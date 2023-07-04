import cv2  # Import library OpenCV untuk pengolahan gambar
import numpy as np  # Import library NumPy untuk operasi numerik# Import library NumPy untuk operasi numerik
import matplotlib.pyplot as plt  # Import library Matplotlib untuk plot grafik
import tkinter as tk  # Import library Tkinter untuk GUI
from PIL import Image, ImageTk  # Import library PIL untuk manipulasi gambar
from tkinter import filedialog, messagebox  # Import fungsi filedialog dan messagebox dari Tkinter


class ImageProcessor:

    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing")
        self.image = None
        self.displayed_image = None
        self.processed_images = [
        ]  # List untuk menyimpan gambar-gambar yang telah diproses

        # Label gambar
        self.image_label = tk.Label(root)
        self.image_label.pack(side="left")

        # Frame tombol
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="left", padx=60)

        # Tombol-tombol
        self.open_button = tk.Button(self.button_frame,
                                     text="Select image to process",
                                     command=self.open_image,
                                     bg="blue",
                                     fg="white",
                                     width=19, 
                                     height=2)
        self.open_button.pack(pady=10)

        self.grayscale_button = tk.Button(self.button_frame,
                                          text="Grayscale",
                                          command=self.apply_grayscale,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.grayscale_button.pack(pady=10)

        self.contrast_button = tk.Button(self.button_frame,
                                         text="Penambahan Kontras",
                                         command=self.apply_contrast,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.contrast_button.pack(pady=10)

        self.smooth_button = tk.Button(
            self.button_frame,
            text="Smoothing",
            command=self.apply_smooth,
                                         bg="green",
                                         fg="white",
                                         width=19,
                                         height=2)
        self.smooth_button.pack(pady=10)

        self.pertajam_button = tk.Button(
            self.button_frame,
            text="Pertajam",
            command=self.apply_pertajam,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.pertajam_button.pack(pady=10)

        self.edge_detection_button = tk.Button(
            self.button_frame,
            text="Negasi",
            command=self.apply_negation,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.edge_detection_button.pack(pady=10)
        
        self.edge_detection_button = tk.Button(
            self.button_frame,
            text="Negasi",
            command=self.apply_negation,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.edge_detection_button.pack(pady=10)
        self.histogram_button = tk.Button(self.button_frame,
                                          text="Histogram",
                                          command=self.show_histogram,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.histogram_button.pack(pady=10)

        self.histogram_matching_button = tk.Button(
            self.button_frame,
            text="Histogram Matching",
            command=self.histogram_matching,
                                          bg="green",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.histogram_matching_button.pack(pady=10)

        self.show_all_results_button = tk.Button(self.button_frame,
                                                 text="Tampilkan Semua Hasil",
                                                 command=self.show_all_results,
                                          bg="blue",
                                          fg="white",
                                          width=19,
                                          height=2)
        self.show_all_results_button.pack(pady=10)

        # Label hasil
        self.result_frame = tk.Frame(root)
        self.result_frame.pack(side="right", padx=20)

        self.result_label = tk.Label(self.result_frame)
        self.result_label.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("File Gambar", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = cv2.imread(file_path)
            if self.image is not None:
                self.display_image(self.image)

    def display_image(self, image):
        self.image_label.configure(image=None)
        displayed_image = Image.fromarray(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        displayed_image.thumbnail((400, 400))
        self.displayed_image = ImageTk.PhotoImage(displayed_image)
        self.image_label.configure(image=self.displayed_image)

    def display_processed_image(self, processed_image):
        self.result_label.configure(image=None)
        displayed_image = Image.fromarray(processed_image)
        displayed_image.thumbnail((400, 400))
        displayed_image = ImageTk.PhotoImage(displayed_image)
        self.result_label.configure(image=displayed_image)
        self.result_label.image = displayed_image

    def apply_grayscale(self):
        if self.image is not None:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.processed_images.append(gray_image)
            self.display_processed_image(gray_image)
        else:
            messagebox.showerror(
                "Error",
                "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
            )

    def show_histogram(self):
        if self.image is not None:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            plt.figure(figsize=(6, 4))
            plt.hist(gray_image.ravel(), bins=256, color='gray')
            plt.title("Histogram")
            plt.xlabel("Nilai Piksel")
            plt.ylabel("Frekuensi")
            plt.show()
        else:
            messagebox.showerror(
                "Error",
                "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
            )

    def apply_contrast(self):
        if self.image is not None:
            contrast_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            contrast_image = cv2.convertScaleAbs(contrast_image,
                                         alpha=1.5,
                                                 beta=0)
            self.processed_images.append(contrast_image)
            self.display_processed_image(contrast_image)
        else:
            messagebox.showerror
            ("Error",
             "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
             )
          
          
          
          
    def apply_negation(self):
        # Periksa apakah citra berhasil dibaca
        if self.image is not None:
            image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #library OpenCV
            negated_image = 255 - self.image #rumus
            self.processed_images.append(negated_image) #Proses gambar 
            self.display_processed_image(negated_image) #Proses menampilkan gambar
        
        else:
            messagebox.showerror
            ("Error",
             "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
             )
    def apply_pertajam(self):
        # Periksa apakah citra berhasil dibaca
        if self.image is not None:
            image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #library OpenCV
            kernel = np.array([ [-1,-1,-1],
                                [-1, 9,-1],
                                [-1,-1,-1]  ]) # Membuat kernel sharpening
            sharpened_image = cv2.filter2D(image, -1, kernel) #rumus
            self.processed_images.append(sharpened_image) #Proses gambar 
            self.display_processed_image(sharpened_image) #Proses menampilkan gambar
        
            
        else:
            messagebox.showerror
            ("Error",
             "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
             )
    def apply_smooth(self):
        # Periksa apakah citra berhasil dibaca
        if self.image is not None:
            image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #library OpenCV
            kernel_size = (5, 5) #ukuran kernel untuk bluring
            blurred_image = cv2.blur(self.image, kernel_size) #rumus
            self.processed_images.append(blurred_image) #Proses gambar 
            self.display_processed_image(blurred_image) #Proses menampilkan gambar
        
            
        else:
            messagebox.showerror
            ("Error",
             "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
             )






    def histogram_matching(self):
        if self.image is not None:
            reference_path = filedialog.askopenfilename(
                filetypes=[("File Gambar", "*.png;*.jpg;*.jpeg")])
            if reference_path:
                reference_image = cv2.imread(reference_path)
                if reference_image is not None:
                    gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
                    gray_reference = cv2.cvtColor(reference_image,
                                                  cv2.COLOR_BGR2GRAY)

                    # Melakukan histogram matching
                    matched_image = cv2.createCLAHE(clipLimit=2.0,
                                                    tileGridSize=(8, 8)).apply(
                                                        gray_image,
                                                        gray_reference)

                    # Menghitung nilai maksimum, minimum, dan rata-rata dari gambar yang sudah di-matched
                    max_val = np.max(matched_image)
                    min_val = np.min(matched_image)
                    mean_val = np.mean(matched_image)

                    self.processed_images.append(matched_image)
                    self.display_processed_image(matched_image)

                    # Menampilkan hasil histogram matching dan nilai-nilai
                    plt.figure(figsize=(12, 4))

                    plt.subplot(1, 2, 1)
                    plt.hist(gray_image.ravel(),
                             bins=256,
                             color='gray',
                             alpha=0.5,
                             label='Asli')
                    plt.hist(gray_reference.ravel(),
                             bins=256,
                             color='blue',
                             alpha=0.5,
                             label='Referensi')
                    plt.hist(matched_image.ravel(),
                             bins=256,
                             color='red',
                             alpha=0.5,
                             label='Matched')
                    plt.title("Histogram Matching")
                    plt.xlabel("Nilai Piksel")
                    plt.ylabel("Frekuensi")
                    plt.legend()

                    plt.subplot(1, 2, 2)
                    plt.text(
                        0.5,
                        0.5,
                        f"Maks: {max_val}\nMin: {min_val}\nRata-rata: {mean_val}",
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontsize=12)
                    plt.axis('off')

                    plt.tight_layout()
                    plt.show()
            else:
                messagebox.showerror(
                    "Error", "Tidak ada gambar referensi yang dipilih.")
        else:
            messagebox.showerror(
                "Error",
                "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
            )

    def apply_edge_detection(self):
        if self.image is not None:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_image, 100, 200)
            self.processed_images.append(edges)
            self.display_processed_image(edges)
        else:
            messagebox.showerror(
                "Error",
                "Tidak ada gambar yang dapat diproses. Harap buka gambar terlebih dahulu."
            )

    def show_all_results(self):
        if self.processed_images:
            n = len(self.processed_images)
            plt.figure(figsize=(4 * n, 4))
            for i in range(n):
                plt.subplot(1, n, i + 1)
                plt.imshow(self.processed_images[i], cmap='gray')
                plt.axis('off')
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showerror(
                "Error", "Tidak ada hasil pemrosesan yang ditampilkan.")


root = tk.Tk()
app = ImageProcessor(root)
root.mainloop()

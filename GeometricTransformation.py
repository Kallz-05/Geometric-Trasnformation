import streamlit as st
from PIL import Image
import cv2
import numpy as np



select=st.selectbox("pick",["camera","upload image"])
if select=="camera":
    cam=st.camera_input("capture a photo")
    if cam is not None:
        file_bytes = np.asarray(bytearray(cam.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image,channel="RGB")

else:
    uploaded_file = st.file_uploader("Choose a image file", type=["jpg","png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image1= cv2.imdecode(file_bytes, 1)
        st.image(opencv_image1,channels="BGR")

import cv2
import numpy as np
import os

# Path ke gambar
image_path = "FGO.jpg"  # Ganti dengan nama file gambar Anda
output_dir = "output_images"  # Direktori untuk menyimpan gambar hasil
os.makedirs(output_dir, exist_ok=True)  # Buat direktori jika belum ada

# Cek apakah file ada
if not os.path.exists(image_path):
    print(f"Error: File '{image_path}' tidak ditemukan. Periksa path-nya.")
else:
    # Buka file gambar
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Gambar tidak dapat dibuka. Pastikan file adalah format gambar yang valid.")
    else:
        # Dimensi gambar
        rows, cols = image.shape[:2]

        # Fungsi untuk mengecilkan ukuran gambar ke dimensi tetap
        def resize_to_fixed_size(img, width=300, height=300):
            new_size = (width, height)
            return cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

        # Ukuran gambar yang diinginkan
        target_width = 300
        target_height = 300

        # 1. Gambar Asli
        original_image_resized = resize_to_fixed_size(image, target_width, target_height)
        cv2.imwrite(os.path.join(output_dir, "original_image.jpg"), original_image_resized)
        cv2.imshow("Original Image", original_image_resized)

        # 2. Rotasi
        angle = 45  # Rotasi 45 derajat
        rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
        rotated_image_resized = resize_to_fixed_size(rotated_image, target_width, target_height)
        cv2.imwrite(os.path.join(output_dir, "rotated_image.jpg"), rotated_image_resized)
        cv2.imshow("Rotated Image", rotated_image_resized)

        # 3. Scaling
        scale_x, scale_y = 1.5, 1.5  # Skala 1.5x
        scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
        scaled_image_resized = resize_to_fixed_size(scaled_image, target_width, target_height)
        cv2.imwrite(os.path.join(output_dir, "scaled_image.jpg"), scaled_image_resized)
        cv2.imshow("Scaled Image", scaled_image_resized)

        # 4. Translasi
        tx, ty = 50, 100  # Geser 50 px ke kanan, 100 px ke bawah
        translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
        translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
        translated_image_resized = resize_to_fixed_size(translated_image, target_width, target_height)
        cv2.imwrite(os.path.join(output_dir, "translated_image.jpg"), translated_image_resized)
        cv2.imshow("Translated Image", translated_image_resized)

        # 5. Skewing
        skew_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])
        skewed_image = cv2.warpAffine(image, skew_matrix, (int(cols * 1.5), int(rows * 1.5)))
        skewed_image_resized = resize_to_fixed_size(skewed_image, target_width, target_height)
        cv2.imwrite(os.path.join(output_dir, "skewed_image.jpg"), skewed_image_resized)
        cv2.imshow("Skewed Image", skewed_image_resized)

        # Tunggu hingga tombol ditekan dan tutup semua jendela
        cv2.waitKey(0)
        cv2.destroyAllWindows()

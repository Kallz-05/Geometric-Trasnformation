import streamlit as st
import cv2
import numpy as np

# Fungsi untuk mengecilkan ukuran gambar ke dimensi tetap (opsional, jika tetap dibutuhkan)
def resize_to_fixed_size(img, width=300, height=300):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

# Menu pada Streamlit
menu = st.sidebar.selectbox("Menu", ["Nama Pengembang", "Aplikasi Manipulasi Gambar"])

if menu == "Nama Pengembang":
    st.title("Nama Pengembang")
    st.write("Muhammad Fikry Haikal")

elif menu == "Aplikasi Manipulasi Gambar":
    st.title("Aplikasi Manipulasi Gambar")

    # Upload file gambar
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if uploaded_file is not None:
        # Baca file gambar
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is not None:
            # Dimensi gambar asli
            rows, cols = image.shape[:2]

            # 1. Gambar Asli
            st.image(image, caption="Original Image", channels="BGR")

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

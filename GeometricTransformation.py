import cv2
import numpy as np

# Fungsi utama
def main():
    # Baca file gambar (ganti 'image.png' dengan path file gambar Anda)
    image_path = 'image.png'
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Gambar tidak dapat dibuka. Pastikan path gambar benar.")
        return

    # Dimensi gambar
    rows, cols = image.shape[:2]

    # 1. Rotasi
    angle = 45  # Sudut rotasi dalam derajat
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    cv2.imshow("Rotated Image", rotated_image)

    # 2. Skalasi
    scale_factor = 1.5  # Faktor skala
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Scaled Image", scaled_image)

    # 3. Translasi
    tx, ty = 50, 100  # Perpindahan dalam piksel
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    cv2.imshow("Translated Image", translated_image)

    # 4. Skewing
    skew_x, skew_y = 0.5, 0.5  # Koefisien skew
    skew_matrix = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])
    skewed_image = cv2.warpAffine(image, skew_matrix, (int(cols * 1.5), int(rows * 1.5)))
    cv2.imshow("Skewed Image", skewed_image)

    # Menampilkan gambar asli (opsional)
    cv2.imshow("Original Image", image)

    # Tunggu hingga user menekan tombol apa saja
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Panggil fungsi utama
if __name__ == "__main__":
    main()

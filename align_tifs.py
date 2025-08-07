from skimage import img_as_float, exposure
from skimage.io import imread, imsave
from skimage.transform import resize
from pystackreg import StackReg
import matplotlib.pyplot as plt
import numpy as np
import os

# === Parameters ===
input_folder = ''  # Folder with input images
reference_image_path = ''  # Path to reference image
output_folder = ''  # Where aligned images will be saved
channel_to_align = #Channel used for alignment

# === Create output folder if it doesn't exist ===
os.makedirs(output_folder, exist_ok=True)

# === Load reference image ===
image1 = imread(reference_image_path)
print(f"Reference image shape: {image1.shape}")

# === Preprocess reference channel ===
ref_channel = image1[:, :, channel_to_align]
ref_channel = exposure.rescale_intensity(ref_channel, in_range=(120, 200))
ref_channel = img_as_float(ref_channel)

# === Set up registration (affine or translation) ===
sr = StackReg(StackReg.AFFINE)

# === Process each image in the input folder ===
input_files = os.listdir(input_folder)
for input_file in input_files:
    if input_file.endswith('.tif'):
        input_path = os.path.join(input_folder, input_file)
        print(f"Input: {input_path}")
        file_size = os.path.getsize(input_path)

        if file_size >= 5 * 1024 * 1024:  # Only process files ≥ 5 MB
            image2 = imread(input_path)
            mov_channel = image2[:, :, channel_to_align]
            mov_channel = exposure.rescale_intensity(mov_channel, in_range=(120, 200))
            mov_channel = img_as_float(mov_channel)

            # Optional: visualize channels
            plt.imshow(ref_channel, cmap='gray')
            plt.title(f'Reference (channel {channel_to_align})')
            plt.show()

            plt.imshow(mov_channel, cmap='gray')
            plt.title(f'To align (channel {channel_to_align})')
            plt.show()

            # === Register and transform ===
            out_trans = sr.register(ref_channel, mov_channel)
            aligned_image2 = np.zeros_like(image2)
            for c in range(image2.shape[2]):
                aligned_image2[:, :, c] = sr.transform(image2[:, :, c], tmat=out_trans)

            # === Save aligned image ===
            output_file = f'aligned_{input_file}'
            output_path = os.path.join(output_folder, output_file)
            imsave(output_path, aligned_image2)

            print(f"Processed: {input_file} -> {output_file}")
        else:
            print(f"Skipped: {input_file} (File size < 5MB)")

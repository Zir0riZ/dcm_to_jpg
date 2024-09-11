import pydicom
from PIL import Image
import numpy as np
import os
import glob


def dcm_to_jpg(dcm_path, jpg_path):
    # Read DICOM file
    dicom = pydicom.dcmread(dcm_path)

    # Convert pixel data to numpy array
    img = dicom.pixel_array.astype(float)

    # Normalize the image
    img = (np.maximum(img, 0) / img.max()) * 255.0

    # Convert to uint8
    img = np.uint8(img)

    # Create PIL image
    image = Image.fromarray(img)

    # Save as JPG
    image.save(jpg_path)


# Path to folder containing DICOM files
input_folder = ""

# Path to folder for saving JPG files
output_folder = ""

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find all DICOM files in the input folder
dcm_files = glob.glob(os.path.join(input_folder, "*.dcm"))

# Convert each DICOM file to JPG
converted_count = 0
for dcm_file in dcm_files:
    try:
        # Create JPG filename
        jpg_file = os.path.join(output_folder, os.path.splitext(
            os.path.basename(dcm_file))[0] + ".jpg")

        # Convert file
        dcm_to_jpg(dcm_file, jpg_file)
        print(f"Converted: {dcm_file} to {jpg_file}")
        converted_count += 1
    except Exception as e:
        print(f"Error converting {dcm_file}: {str(e)}")
        continue

print(f"Conversion of {converted_count} out of {len(dcm_files)} DICOM files to JPG completed.")
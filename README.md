# DCM to JPG Converter

This Python script converts DICOM (.dcm) files to JPG images.

## Features

- Batch conversion of DICOM files to JPG
- Image normalization for improved quality
- Progress reporting and error handling

## Prerequisites

To run this script, you need:

- Python 3.x
- The following libraries:
  - pydicom
  - Pillow (PIL)
  - numpy

You can install the required libraries using:
pip install pydicom Pillow numpy

## Usage

1. Download the `dcm2jpg.py` file.
2. Open the file in a text editor.
3. Specify the path to the input folder containing DICOM files in the `input_folder` variable.
4. Specify the path to the output folder for saving JPG files in the `output_folder` variable.
5. Run the script:
python dcm2jpg.py


## Example

Path to folder containing DICOM files
input_folder = "C:/Users/YourName/DICOM_Files"
Path to folder for saving JPG files
output_folder = "C:/Users/YourName/JPG_Files"


## Contributing

Your suggestions and contributions to improve this project are welcome. Please feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

# Microscope Foci Counter

This repository contains a minimal pipeline for aligning microscope image data and counting foci in each field. It is designed to be easy to use and adaptable to different experimental setups.

## Overview
The pipeline performs three main tasks:

1. **Crop image**. Automatically crop all images to the same dimensions
2. **Image Alignment**: Automatically aligns microscopy images to correct for drift or movement during acquisition.
3. **Foci Detection and Counting**: Identifies and counts the number of foci (e.g., fluorescent spots) present in each aligned image.


## Requirements

- Python 3.8+
  - `numpy`
  - `scipy`
  - `opencv-python`
  - `scikit-image`
  - `matplotlib`
  - `pandas`
  - `od`

- Fiji
  - `BioFormats` (Only for .ims format)

 
## Workflow

1) **Convert ims to tiff** (Only if not in tif format)                
Run convert_ims_to_tif.ijm from Fiji (Plugins>Run or Paste into Plugins>Macros>Sartup Macros)
Parameter: 
-Input directory with all the microsope files

2) **Crop image**
Run crop_fiji_macro_from_tif.ijm from Fiji (Plugins>Run or Paste into Plugins>Macros>Sartup Macros)
Parameter: 
-Input directory with all the microsope files in tif format                
- Output directory
- x # Starting x-coordinate of the crop                
- y # Starting y-coordinate of the crop                                
- width # Width of the cropped region                
- height # Height of the cropped region                

3) **Image Alignment**                
Run align_tifs.py 
Parameter: 
- input_folder #Input directory containing all microscope files in TIFF format, with the same dimensions.
- reference_image_path # Which image to use a a reference
- output_folder # Where aligned images will be saved
- channel_to_align = #Channel used for alignment

4) **Foci Detection and Counting**
Run count_foci.ijm from Fiji (Plugins>Run or Paste into Plugins>Macros>Sartup Macros)
Parameter:
- inputDir # Define directories with all the tif files aligned
- outputDir # Output directory
- Defines the input parameters of processChannel(p1,p2 ,p3 ,p4) (lines 56, 57 and 58)
 p1: Channel to count foci 
 p2: Proeminence
 p3: Min LUT
 p4: Max LUT





                  
                
                
                



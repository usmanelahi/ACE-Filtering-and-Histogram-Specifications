# Image Processor GUI - Part 1

This Python script implements a GUI application using Tkinter for applying the ACE (Adaptive Contrast Enhancement) filter to an image.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Tkinter
- Pillow (Python Imaging Library)

You can install Pillow via pip:

```
pip install Pillow
```

## Usage

1. Clone or download the script `main.py`.
2. Ensure you have the `helpers.py` file in the same directory, containing the `apply_ace_filter()` function.
3. Place your image (`cat_picture.jpeg`) in the same directory as the script.
4. Run the script using Python:

```
python main.py
```

5. The GUI window will appear displaying the image.
6. Enter the desired values for `k1`, `k2`, and `window size` in their respective entry fields.
7. Click the "Apply Ace Filter" button to apply the ACE filter with the specified parameters.
8. The processed image will be displayed in the GUI.

## Description

- `main.py`: Contains the main script implementing the GUI using Tkinter.
- `helpers.py`: Contains the `apply_ace_filter()` function, which applies the ACE filter to the image.
- `ImageProcessorGUIPart1`: The main class responsible for initializing the GUI elements, loading the image, and handling the application of the ACE filter.
- `display_image()`: A helper method to display images on the Tkinter GUI.
- `cat_picture.jpeg`: The image to which the ACE filter will be applied.

## Note

This script assumes that the image file is provided and named as `cat_picture.jpeg` in the same directory as the script. Ensure your image is correctly named and located before running the script.

# Image Processor GUI - Part 2

This Python script implements a simple GUI application using Tkinter for image processing. Specifically, it applies histogram specification to a reference image based on a target image.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Tkinter
- Pillow (Python Imaging Library)

You can install Pillow via pip:

```
pip install Pillow
```

## Usage

1. Clone or download the script `main.py`.
2. Place your reference image (`reference_image.jpeg`) and target image (`target_image.png`) in the same directory as the script.
3. Run the script using Python:

```
python main.py
```

4. The GUI window will appear displaying both the reference and target images.
5. Click the "Apply Histogram Specification" button to apply histogram specification to the target image based on the reference image.
6. The processed image will be displayed in the GUI.

## Description

- `main.py`: Contains the main script implementing the GUI using Tkinter.
- `apply_histogram_specification()`: This function, located in a separate file (`main.py`), applies histogram specification to the target image based on the reference image.
- `ImageProcessorGUIPart2`: The main class responsible for initializing the GUI elements, loading images, and handling the application of histogram specification.
- `display_image()`: A helper method to display images on the Tkinter GUI.
- `reference_image.jpeg`: The reference image used for histogram specification.
- `target_image.png`: The target image to which histogram specification will be applied.

## Note

This script assumes that the reference and target images are provided and named as `reference_image.jpeg` and `target_image.png`, respectively, in the same directory as the script. Ensure your images are correctly named and located before running the script.

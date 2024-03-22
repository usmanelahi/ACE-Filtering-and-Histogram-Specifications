from PIL import Image, ImageOps
import numpy as np
import math

def calculate_mean(img_array):
    total_sum = 0
    mean = 0
    count = 0
    for row in img_array:
        for col in row:
            total_sum += col
            count += 1
    mean = total_sum / count
    return mean

def calculate_std_dev(img_array):
    total_sum = 0
    deviation = 0
    size = len(img_array) * len(img_array[0])
    mean = calculate_mean(img_array)
    for row in img_array:
        for col in row:
            total_sum += ((col - mean) ** 2) / ((size ** 2) - 1)
    deviation = total_sum ** 0.5
    return deviation

def apply_ace_filter(image, window_size, k1, k2):
    img_array = np.asarray(image, dtype=np.float32)
    output_array = np.zeros(img_array.shape, dtype=np.float32)
    rows, cols = img_array.shape[:2]
    half_win = window_size // 2

    mean = calculate_mean(img_array)
    for r in range(rows):
        for c in range(cols):
            r_min = max(r - half_win, 0)
            r_max = min(r + half_win + 1, rows)
            c_min = max(c - half_win, 0)
            c_max = min(c + half_win + 1, cols)
            window = img_array[r_min:r_max, c_min:c_max]
            std_dev = calculate_std_dev(window)
            output_array[r, c] = k1 * (mean / std_dev) * (window[window_size // 2, window_size // 2] - calculate_mean(window)) + (k2 * calculate_mean(window))

    output_image = Image.fromarray(np.uint8(output_array))
    return output_image

def equalize_histogram(image):
    image_hist, bins = np.histogram(image.flatten(), 256, density=True)
    cdf = image_hist.cumsum()  
    cdf_normalized = cdf * 255 / cdf[-1]  

    image_equalized = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    return image_equalized.reshape(image.shape)

def match_histograms(image, reference):
    oldshape = image.shape
    image = image.ravel()
    reference = reference.ravel()

    s_values, bin_idx, s_counts = np.unique(image, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(reference, return_counts=True)

    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    return interp_t_values[bin_idx].reshape(oldshape)

def apply_histogram_specification(ref_img, tar_img):
    ref_array = np.asarray(ref_img, dtype=np.uint8)
    tar_array = np.asarray(tar_img, dtype=np.uint8)
    ref_equalized_array = equalize_histogram(ref_array)
    matched_img_array = match_histograms(tar_array, ref_equalized_array)

    matched_img = Image.fromarray(matched_img_array.astype('uint8'))
    return matched_img

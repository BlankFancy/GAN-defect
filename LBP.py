from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# TODO: add lbp feature for defect detection
def get_lbp_features(image, radius=1, n_points=8):
    lbp = local_binary_pattern(image, n_points, radius)
    return lbp
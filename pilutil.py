import colorsys
import os
import time

import numpy as np
import psutil
from PIL import Image, ImageEnhance

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)


def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = (h + hout) % 1
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr


def multiprocess_colorize(image, hue, brightness, saturation, result_dict, key):
    # prevent cpu fan goes to 100% lol...
    time.sleep(0.5)
    new_img = colorize(image, hue, brightness, saturation)
    result_dict[key] = new_img
    return new_img


def colorize(image, hue, brightness, saturation):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(img)
    new_img = Image.fromarray(shift_hue(arr, hue / 360.).astype('uint8'), 'RGBA')
    """
    random brightness
    """
    new_img = ImageEnhance.Brightness(new_img).enhance(brightness)
    new_img = ImageEnhance.Color(new_img).enhance(saturation)
    return new_img

def limit_cpu():
    "is called at every process start"
    p = psutil.Process(os.getpid())
    # set to lowest priority, this is windows only, on Unix use ps.nice(19)
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)

"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------
此程式可以將多張背景相同,但路人在不同位置的照片,合成一張將人物都去除,只有背景的相片。
"""

import os
import sys
from simpleimage import SimpleImage
from math import sqrt


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_distance = sqrt((red-pixel.red)**2 + (green-pixel.green)**2
                          + (blue-pixel.blue)**2) # sqrt開根號
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_pixels_red = 0
    total_pixels_blue = 0
    total_pixel_green = 0
    for i in range(len(pixels)):  # pixels是list所以用for迴圈
        total_pixels_red += pixels[i].red
        total_pixels_blue += pixels[i].blue
        total_pixel_green += pixels[i].green
    return [total_pixels_red // len(pixels) ,total_pixel_green // len(pixels)   # return平均後的值
        ,total_pixels_blue // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    average_pixel = get_average(pixels)  # 得到所有平均後的red/blue/green
    min = float('inf')  # 設一個無限大的數
    best_pixel = None
    for i in range(len(pixels)):
        # 把(一個)pixel和平均後的red/green/blue丟入get_pixel_dist計算color_distance
        best_distance = get_pixel_dist(pixels[i],average_pixel[0],average_pixel[1],average_pixel[2])
        if best_distance < min:
            min = best_distance
            best_pixel = pixels[i]  # 當best_distance小於最小值,更新min和best_pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):  # 每個pixel的x/y座標
            pixel_list = []
            for img in images: # 跑每張照片images是一個list(沒有編號但還是會全部跑完的寫法)
                img_pixel = img.get_pixel(x,y)
                pixel_list.append(img_pixel) # 每張照片在位置(x,y)的pixel加到list裡面
            best_pixel = get_best_pixel(pixel_list)
            result_pixel = result.get_pixel(x,y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue =  best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)  # 加入新的Img
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])  # 跑所有Img
    solve(images)


if __name__ == '__main__':
    main()

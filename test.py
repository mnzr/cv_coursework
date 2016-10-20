"""
Task 1: Plot the histogram of a range of images.
Task 2: Plot also the histogram of the three components of a color image
        when represented as
           i)RGB
           ii)YIQ
           iii)HSI

Acquire some RGB images. Convert them to YIQ and HIS representations.
Subject them to various degree of noise and convert them back to RGB for
display.

Implement histogram smoothing; determine how much smoothing is necessary
to suppress turning pints in the histogram due to what you consider to
be noise, or small-scale image effects.
"""

# from PIL import Image

# # Image format: JPG
# # Image size: 100x100
# SIZE = 100
# # Image mode: RGB
# gorillaz = Image.open("Gorillaz.jpg") # JpegImageFile object
# # Load the image to access pixel values
# pixels = gorillaz.load()    # Iteratable


# # Loading the image
# img=mpimg.imread('Gorillaz.jpg')    # numpy array

# red = img[:,:,0]
# green = img[:,:,1]
# blue = img[:,:,2]
# bins = np.linspace(-10, 10, 100)


# # all = [red, green, blue]
# colors = ['red', 'green', 'blue']

# plt.hist(red, bins=bins)
# plt.hist(green, bins=bins)
# plt.hist(blue, bins=bins)

# plt.title("Histogram with 'auto' bins")
# plt.show()

# print(img[0][99][0])

# print(img[1][0][0])
# print(img[99][99][0])


# [110 146 234] [101 162 243] [ 99 140 220] ...,
# [ 81 150 255] [ 65 139 234] [ 61  89 163] ...,

# lum_img = img[:,:,0]
# imgplot = plt.imshow(lum_img)
# plt.imshow(lum_img)
# plt.colorbar()



# for x in range(SIZE):
#     for y in range(SIZE):
#         print(pixels[x, y], end=' ')
#     print()

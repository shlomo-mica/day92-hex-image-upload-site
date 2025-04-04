from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Open an image file
image1 = Image.open('zwift_race.jpg')
image2=Image.open('testrgb.png')


# Convert the image to RGB mode (if not already)
rgb_image = image1.convert('RGB')

# Convert the RGB image to a NumPy array
rgb_array = np.array(rgb_image)
#print(rgb_array)
#print(rgb_array[11, 2])  # This will display a NumPy array of shape (height, width, 3)
#print(rgb_image.size)
#print(rgb_image.show())  #zwift show


# Convert to hex
hex_array = np.array([
    ["#{:02X}{:02X}{:02X}".format(r, g, b) for r, g, b in row]
    for row in rgb_array])

df = pd.DataFrame(hex_array)
# Flatten DataFrame to a 1D array for counting
flattened_colors = df.values.flatten()
print(df)
# Count occurrences of each unique HEX color
color_counts = pd.Series(flattened_colors).value_counts().reset_index()
color_counts.columns = ["HEX Color", "Count"]

# Display duplicate color counts
print(color_counts.head(11))













# shape = hex_array.shape
# size = hex_array.size
#
# # Print results
# print("HEX Array:\n", hex_array)
# print("\nShape:", shape)  # (Rows, Columns)
# print("Size:", size)  # Total number of elements
#
# array = np.zeros([100, 200, 3], dtype=np.uint8)
#
# array[:, :222] = [255, 128, 0]  # Orange left side
# array[:, 100:] = [0, 0, 255]  # Blue right side
#
# img = Image.fromarray(array)
# img.save('testrgb.png')
# img.show()




# Define the array and ensure it's a NumPy array with dtype=uint8
# array22 = np.array([[132, 131, 111],
#                     [132, 131, 111],
#                     [134, 131, 114]], dtype=np.uint8)
#
# # Convert to a grayscale image
# img22 = Image.fromarray(array22, mode='L')
#
# # Save and show the image
# img22_resized = img22.resize((100, 100), Image.NEAREST)  # You can change NEAREST to other resampling methods
#
# # Save and show the resized image
# img22_resized.save('picture_resized.png')
# img22_resized.show()




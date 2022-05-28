# This code is used to tile together the four directions of the street view image from the street point
import os
from PIL import Image

# Control of image quality, value range 1 to 100
quality_value = 100
# Original image save path
original_path = r'E:\resource_code_data\Streetview_Download\save_images'
# joint image save path
joint_path = r'E:\resource_code_data\Streetview_Download\save_joint_images'

#  Get all image paths under a file
image_open = [Image.open(original_path+'\\'+fn) for fn in os.listdir(original_path)]

# Images converted to the same size
image_resize = []
for img in image_open:
    new_img = img.resize((256, 128), Image.ANTIALIAS)
    image_resize.append(new_img)

def joint_pic(img_list,number):
    img_list = img_list[0]
    # print(img_list)
    # Single image size
    width, height = img_list[0].size
    # Create a long blank image
    # white = Image.new(img_list[0].mode, (width, height * len(ims)))
    white = Image.new(img_list[0].mode, (width * len(img_list), height))
    # joint image
    for i, image in enumerate(img_list):
        # result.paste(image, box=(0, i * height))
        white.paste(image, box=(i * width, 0))
    # save the image
    white.save(os.path.join(joint_path,str(number)+'.jpg'),quality=quality_value)

# Grouping lists into groups of 4
for j,count in enumerate(range(0,len(image_resize),4)):
    j += 1
    # print(j,count)
    group = []
    group.append(image_resize[count:count+4])
    # print(image_resize)
    # print(group)
    joint_pic(group,j)
    print('process the ' + str(j) + ' iamge')
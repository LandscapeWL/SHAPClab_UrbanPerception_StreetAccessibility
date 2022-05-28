# The purpose of this code is to create the corresponding txt file of the training images and labels
import os

# image = os.listdir(r"E:\resource_code_data\ADE20K_Process\training\train_image")
image = os.listdir(r"E:\resource_code_data\ADE20K_Process\validation\val_image")
# with open("./train_data.txt","w") as f:
with open("./val_data.txt","w") as f:
    for name in image:
        # print(name
        label = name.split('.')[0] + '_seg.png'
        f.write(name+";"+label+"\n")
print('precess done')
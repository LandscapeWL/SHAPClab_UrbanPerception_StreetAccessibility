# This code is used to pre-process the Ade20k dataset, separating the training images from the labeled images
import os
from PIL import Image

# Access to training and validation data
# process = 'training'
process = 'validation'
# process2 = 'train'
process2 = 'val'

# These two folders are used to store pre-processed data
# savepath_iamge is for saving the training data
# savepath_label is for saving the label data
savepath_image = r'E:\resource_code_data\ADE20K_Process\{}\{}_image'.format(process,process2)
savepath_label = r'E:\resource_code_data\ADE20K_Process\{}\{}_label'.format(process,process2)

# This path is for ADE20k files that need to be processed
# Please replace the alphabetical categories that need to be processed (e.g. a,b,c,d,e.......)
path = r'E:\resource_code_data\ADE20K\{}\a'.format(process)
read_path = os.listdir(path)
n=0
for i in read_path:
    image_path = os.listdir(r'E:\resource_code_data\ADE20K\{}\a\\'.format(process) + i)
    for j in image_path:
        if j.endswith('jpg'):
            jpg = Image.open(path+'/'+i+'/'+j)
            jpg.save(savepath_image+'/'+j)
        if j.endswith('seg.png'):
            png = Image.open(path+'/'+i+'/'+j)
            png.save(savepath_label+'/'+j)
        n+=1
        print('process_'+ str(n) +'_image')
print('process done')



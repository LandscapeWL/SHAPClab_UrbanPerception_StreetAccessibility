# You can deploy this code on a cloud server to collect perception scores for street view images
import os
import cv2
import csv
import codecs
import os

# street view save path
read_path = r'image/'
# perception result file name
fileName = 'Score.csv'
# perception result file save path
save_path = r'score_save'

num = 0
imagelist = os.listdir(read_path)

print('Please observe the street view image for 5 seconds\nAnd enter a number between 1 and 100 for the score')
for imgname in imagelist:
    print('Remaining ', len(imagelist)-num, ' images.', end='')
    image = cv2.imread(read_path + imgname)
    cv2.imshow(imgname, image)
    # k = cv2.waitKey(0)
    cv2.waitKey(3000)
    cv2.destroyWindow(imgname)
    print(' The ',num,' image ',end='')
    num += 1
    score = input("perception score is:")

    if int(score) < 101:
        # writte result in csv file
        with codecs.open(fileName, 'a', 'utf-8') as csvfile:
            filednames = [imgname, score]
            writer = csv.DictWriter(csvfile, fieldnames=filednames)
            writer.writeheader()

        # Store the scoring results in the corresponding folder
        if not os.path.exists(save_path + '/' + score):
            os.makedirs(save_path + '/' + score)
        cv2.imwrite(save_path + '/' + score + '/' + imgname, image)
        os.remove(read_path + imgname)

    else:
        print("Please re-enter a number between 1 and 100!\n",end='')
        score = input("Again input perception score is:")

        # writte result in csv file
        with codecs.open(fileName, 'a', 'utf-8') as csvfile:
            filednames = [imgname, score]
            writer = csv.DictWriter(csvfile, fieldnames=filednames)
            writer.writeheader()

        # Store the scoring results in the corresponding folder
        if not os.path.exists(save_path + '/' + score):
            os.makedirs(save_path + '/' + score)
        cv2.imwrite(save_path + '/' + score + '/' + imgname, image)
        os.remove(read_path + imgname)


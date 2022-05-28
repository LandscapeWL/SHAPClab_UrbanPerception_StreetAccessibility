# Download Urban Street View Images
# -*- coding:utf-8 -*-
import csv
import urllib.request
import time
import random

def pic_download(pic_path,f_pic):
    web = urllib.request.urlopen(pic_path)
    itdata = web.read()
    f_tup = open(f_pic, "wb")
    f_tup.write(itdata)
    f_tup.close()

def read_line(f):
    temp_list=[]
    with open(f, encoding='utf-8', mode='r')as file_object:
        for line in file_object:
            temp = line.replace('\n', '').encode('utf-8').decode('utf-8-sig')
            temp_list.append(temp)
    return temp_list

def write_txt(path,content):
    f = open(path,'a',encoding='utf-8')
    f.write(content)
    f.close()

if __name__ == '__main__':
    # Set the file path to store the longitude and latitude coordinates of the street view point
    f = r"E:\resource_code_data\Streetview_Download\point_data\streetview_point.txt"
    # Set the street view image storage path
    f_pic = r"E:\resource_code_data\Streetview_Download\save_images"
    # Set the download street view message path
    f_path = r"E:\resource_code_data\Streetview_Download\save_message\streetview_download_message.txt"
    # Set the path to store API Key
    f_key = r"E:\resource_code_data\Streetview_Download\key.csv"

    # Import Key form 'key.csv' file
    with open(f_key) as f_k:
        reader = csv.reader(f_k)
        key_lists = list(reader)
        # print(reader)

    # Use keys in order. Every 99 street view image downloaded switch to the next key.
    k = 0
    j = 0
    # key_lists = read_line(f_key)
    key = key_lists[j][1]
    write_txt(f_path,"Id,lon,lat,pic_name"+"\n")
    lists = read_line(f)
    for list in lists:
        temp_result = list.replace(" ","").split(",")
        print("Spatial location message："+temp_result[0]+" "+temp_result[1]+" "+temp_result[2])
        print("That Key download ",k," images")

        if k>99:
            j = j+1
            key = key_lists[j][1]
            k = 0

        # print(key)
        for i in range(0,4):
            url = "http://api.map.baidu.com/panorama/v2?ak="+str(key)+"&width=1024&height=512&location="+str(temp_result[1])+","+str(temp_result[2])+"&pitch=20&fov=90&heading="+str(i*90)
            print(url)
            time.sleep(3)
            pic_download(url,f_pic+"\\"+str(temp_result[0])+'_'+ str(i) +'.jpg')
            content = temp_result[0]+','+temp_result[1]+','+temp_result[2]+','+str(temp_result[0])+'.jpg'+"\n"
            write_txt(f_path,content)
            k = k+1
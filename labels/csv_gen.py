import os
import csv
import random

dir_path = "/content/drive/My Drive/dataset/video/"
class_name = os.listdir(dir_path)
print(os.listdir(dir_path+class_name[0]))	
data_train = []
data_val=[]
for cls in class_name:
        videos = os.listdir(dir_path+cls)
        train_count=int(len(videos)*0.8)
        val_count=int(len(videos)*0.2)
        print(train_count,val_count)
        for i in range(train_count):
                video=videos[i]
                name,ext = video.split('.')
                data_train.append((name, "train"))
        for i in range(val_count):
                video=videos[len(videos)-1-i]
                name,ext = video.split('.')
                data_val.append((name, "val"))
                
                        
data_train.sort()
print(data_train,len(data_train))
data_val.sort()
print(data_val,len(data_val))
with open('/content/drive/My Drive/samsung/labels/CVAE_val.csv','w') as outval:
    csv_out=csv.writer(outval)
    csv_out.writerow(['label','split'])
    for row in data_val:
        csv_out.writerow(row)

with open('/content/drive/My Drive/samsung/labels/CVAE_train.csv','w') as outtrain:
    csv_out=csv.writer(outtrain)
    csv_out.writerow(['label','split'])
    for row in data_train:
        csv_out.writerow(row)
		


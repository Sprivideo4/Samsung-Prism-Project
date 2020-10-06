import os
import csv

dir_path = "/content/drive/My Drive/dataset/test/"
class_name = os.listdir(dir_path)	
data = []
for cls in class_name:
	videos = os.listdir(dir_path+cls)
	for video in videos:
		name,ext = video.split('.')
		data.append((name, "test"))
data.sort()
with open('/content/drive/My Drive/samsung/labels/CVAE_test.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['label','split'])
    for row in data:
        csv_out.writerow(row)
		


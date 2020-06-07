#!/usr/bin/python3

import os
import uuid
import glob
import hashlib
import requests
from hashlib import md5
from multiprocessing import Pool

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(2 ** 20), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def duplicate_finder(fname):
	for i in range(0, len(fname)):
		for j in range(i + 1, len(fname)):
			if(md5(fname[i]) == md5(fname[j])):
				print(fname[i])
				print(fname[j])
				print("are Duplicate")
				print("------------")
			

def download_file(url, file_name = None):
	r = requests.get(url, allow_redirects = True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)


 
urlArr = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg", "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]
	 
child = os.fork()

# child greater than 0  means parent process 
if child == 0:
	 
	print("Child process and id is : ", os.getpid())
	newarray = ["1.jpeg",".png","1.jpg","2.jpeg","2.jpg"]
	for i in range(len(urlArr)):
		download_file(urlArr[i], "foto" + newarray[i]) 
	os._exit(0)
if child > 0:
	#parent
	#print("Parent process and id is : ", os.getpid())
	os.wait()


filenames = glob.glob("/home/ulkem/finalv1/*")
file_jpeg = glob.glob("/home/ulkem/finalv1/*.jpeg")
file_jpg = glob.glob("/home/ulkem/finalv1/*.jpg")
file_png = glob.glob("/home/ulkem/finalv1/*.png")

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        print(filename, hashlib.md5(data).hexdigest())
print("---------")

with Pool(3) as p:
	print(p.map(duplicate_finder, [file_jpeg, file_jpg, file_png]))	
	


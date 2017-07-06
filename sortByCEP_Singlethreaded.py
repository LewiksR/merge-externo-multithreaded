#! /usr/bin/python3

import sys
import os
import struct
import time
from operator import itemgetter

#globals
path = "/home/gpca/Lewiks/CEP/cep.dat"
pathDir = "/home/gpca/Lewiks/CEP/Result/"
#path = "C:\\Users\\Lewiks\\Dropbox\\ARQ\\CEP\\cep.dat"
#pathDir = "C:\\Users\\Lewiks\\Dropbox\\ARQ\\CEP\\"
s = struct.Struct("72s72s72s72s2s8s2s")
maxPerFile = 10000

nextFile = list()
f = open(path, "rb")
counter = 0
fileCounter = 0

t1 = time.time()

#split the files
l = f.read(s.size)
while (len(l) != 0):
	read = s.unpack(l)
	nextFile.append(read)
	l = f.read(s.size)
	counter += 1
	
	if counter >= maxPerFile or len(l) == 0:
		counter = 0
		f_s = open(pathDir + "cep_split_" + str(fileCounter), "ab")
		print("Writing file " + pathDir + "cep_split_" + str(fileCounter))
		nextFile.sort(key=itemgetter(5))

		for i in range(len(nextFile)):
			#print("Wrote entry #" + str(i) + " to file #" + str(fileCounter))
			f_s.write(s.pack(nextFile[i][0], nextFile[i][1], nextFile[i][2], nextFile[i][3], nextFile[i][4], nextFile[i][5], nextFile[i][6]))

		f_s.close()
		nextFile = list()
		fileCounter += 1

print ("Time to split: " + str(time.time() - t1))
t2 = time.time()

#merge sort
counter = 0
while (os.path.isfile(pathDir + "cep_split_" + str(counter + 1)) or counter != 0):
	if os.path.isfile(pathDir + "cep_split_" + str(counter)) and os.path.isfile(pathDir + "cep_split_" + str(counter + 1)):
		f1 = open(pathDir + "cep_split_" + str(counter), "rb")
		f2 = open(pathDir + "cep_split_" + str(counter + 1), "rb")

		f3 = open(pathDir + "not_a_placeholder", "ab")
		l1 = f1.read(s.size)
		l2 = f2.read(s.size)

		while (len(l1) > 0 and len(l2) > 0):
			r1 = s.unpack(l1)
			r2 = s.unpack(l2)
			if r1[5] < r2[5]:
				f3.write(s.pack(r1[0], r1[1], r1[2], r1[3], r1[4], r1[5], r1[6]))
				l1 = f1.read(s.size)
			else:
				f3.write(s.pack(r2[0], r2[1], r2[2], r2[3], r2[4], r2[5], r2[6]))
				l2 = f2.read(s.size)

		while (len(l1) > 0):
			f3.write(s.pack(r1[0], r1[1], r1[2], r1[3], r1[4], r1[5], r1[6]))
			l1 = f1.read(s.size)

		while (len(l2) > 0):
			f3.write(s.pack(r2[0], r2[1], r2[2], r2[3], r2[4], r2[5], r2[6]))
			l2 = f2.read(s.size)
		
		f1.close()
		f2.close()
		f3.close()
		
		os.remove(pathDir + "cep_split_" + str(counter))
		os.remove(pathDir + "cep_split_" + str(counter + 1)	)
		os.rename(pathDir + "not_a_placeholder", pathDir + "cep_split_" + str((counter + 1)//2))
		counter += 2
	elif os.path.isfile(pathDir + "cep_split_" + str(counter)):
		os.rename(pathDir + "cep_split_" + str(counter), pathDir + "cep_split_" + str((counter + 1)//2))
		counter = 0
	else:
		counter = 0

os.rename(pathDir + "cep_split_0", pathDir + "cep_ordered.dat")

print ("\n\n")
print ("Time to merge: " + str(time.time() - t2))
print ("Total time: " + str(time.time() - t1))

f = open(pathDir + "cep_ordered.dat", "rb")
l1 = f.read(s.size)
l2 = f.read(s.size)

flag = 0
while (len(l1) > 0 and len(l2) > 0):
	r1 = s.unpack(l1)
	r2 = s.unpack(l2)
	if r1[5] > r2[5]:
		print("Something went wrong, file is not ordered")
		l1 = ""
		flag = 1
	else:
		l1 = l2
		l2 = f.read(s.size)

f.close()

if flag == 0:
	print("File successfully ordered")









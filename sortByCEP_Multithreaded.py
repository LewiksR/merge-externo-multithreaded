#! /usr/bin/python3

import math
import os
import queue
import queue as Queue
import struct
import sys
import time
import threading
from operator import itemgetter

print ("\n\n\n\n\n\n\n\n\n\n\n")

# --------------------------------
# DECLARING ALL VARIABLES --------

#globals
path = "/home/gpca/Lewiks/CEP/cep.dat"
pathDir = "/home/gpca/Lewiks/CEP/Result/"
#path = "C:\\Users\\Lewiks\\Dropbox\\ARQ\\CEP\\cep.dat"
#pathDir = "C:\\Users\\Lewiks\\Dropbox\\ARQ\\CEP\\Result\\"
s = struct.Struct("72s72s72s72s2s8s2s")
maxPerFile = 10000

f = open(path, "rb")
fileCounter = 0

#we need to count until when to iterate and make new threads and stuff
f.seek(0,2)
splitCount = math.ceil(f.tell() / maxPerFile / s.size)
f.seek(0,0)

lastWrittenSplit = 0
t1 = time.time()

class thread_merge (threading.Thread):
	def __init__(self, file1, file2):
		threading.Thread.__init__(self)
		self.file1 = min(file1, file2)
		self.file2 = max(file1, file2)
	def run(self):
		#print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[THREAD " + str(self.file1) + " WAS STARTED]--")
		doMerge(self.file1, self.file1, self.file2)
		
		#activeCount() does count the MAIN THREAD
		while (threading.activeCount() > 2):
			try:
				q.put_nowait(self.file1)
				#print ("[Thread " + str(self.file1) + "] Just <PUT> file " + str(self.file1) + " in the queue.")
				break;
			except queue.Full:
				try:
					nextFile = q.get(False)
					#print ("[Thread " + str(self.file1) + "] Just <TOOK> file " + str(nextFile) + " from the queue.")
					doMerge(self.file1, self.file1,nextFile)#min(self.file1, nextFile), max(self.file2, nextFile))
				except queue.Empty:
					pass
		#!!!!!!!!!uncomment this in case a split is left without merging
		#print ("Threads left: " + str(threading.activeCount()))
		if threading.activeCount() <= 2:
			#print ("[Thread " + str(self.file1) + "] Doing last split")
			try:
				nextFile = q.get(False)
				#print ("[Thread " + str(self.file1) + "] Just <TOOK> file " + str(nextFile) + " from the queue.")
				doMerge(self.file1, self.file1,nextFile)#min(self.file1, nextFile), max(self.file2, nextFile))
			except queue.Empty:
				pass
		#print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[THREAD " + str(self.file1) + " JUST FINISHED]!!")

def doMerge(ownerThread, file1, file2):
	f3Name = pathDir + "cep_split_" + str(file1) + "+" + str(file2)
	global lastWrittenSplit
	
	if os.path.isfile(pathDir + "cep_split_" + str(file1)) and os.path.isfile(pathDir + "cep_split_" + str(file2)):
		f1 = open(pathDir + "cep_split_" + str(file1), "rb")
		f2 = open(pathDir + "cep_split_" + str(file2), "rb")
		
		f3 = open(f3Name, "ab")
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
		
		os.remove(pathDir + "cep_split_" + str(file1))
		os.remove(pathDir + "cep_split_" + str(file2))
		os.rename(f3Name, pathDir + "cep_split_" + str(file1))
		lastWrittenSplit = file1
#		print ("lastWrittenSplit: " + str(lastWrittenSplit))
	elif os.path.isfile(pathDir + "cep_split_" + str(file1)):
		lastWrittenSplit = file1
	
	#print ("[Thread " + str(ownerThread) + "] Merged files " + str(file1) + " and " + str(file2))

#///////////////////////////////////////////////////////////////////// ///////////////////
#                                                                  // //                //
#   START FOR ALL THE PROCEDURES                                  // //                 //
#                                                                // //                  //
#   DECLARE METHODS, CLASSES AND SUCH ABOVE THIS COMMENT        // //                   //
#                                                              // //                    //
#/////////////////////////////////////////////////////////////// /////////////////////////

#split the files
counter = 0
threadCounter = 0
#
#
#SPLITTING ----------------------------------------------\
nextFile = list()
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
		
		#THIS IS COSTLY
		nextFile.sort(key=itemgetter(5))
		
		for i in range(len(nextFile)):
			f_s.write(s.pack(nextFile[i][0], nextFile[i][1], nextFile[i][2], nextFile[i][3], nextFile[i][4], nextFile[i][5], nextFile[i][6]))
		
		f_s.close()
		nextFile = list()
		fileCounter += 1
#FINISHED SPLITTING -------------------------------------/

print ("Time to split: " + str(time.time() - t1))
t2 = time.time()

q = queue.Queue(maxsize=1)

#starting threads job --------------------------------------\
threadList = list()

while (threadCounter < splitCount):
	t = thread_merge(threadCounter, threadCounter + 1)
	t.start()
	threadList.append(t)
	threadCounter += 2 # i use 1 thread per 2 splits

for t in threadList:
	t.join()
#all threads have finished by now --------------------------/




print ("\n\n")
print ("Time to merge: " + str(time.time() - t2))
print ("Total time: " + str(time.time() - t1))
print ("lastWrittenSplit: " + str(lastWrittenSplit))

os.rename(pathDir + "cep_split_" + str(lastWrittenSplit), pathDir + "cep_sorted.dat")


f = open(pathDir + "cep_sorted.dat", "rb")
l1 = f.read(s.size)
l2 = f.read(s.size)

#verifying if everything's sorted
flag = 0
while (len(l1) > 0 and len(l2) > 0):
	r1 = s.unpack(l1)
	r2 = s.unpack(l2)
	if r1[5] > r2[5]:
		print("Something went wrong, file is not sorted")
		l1 = ""
		flag = 1
	else:
		l1 = l2
		l2 = f.read(s.size)

f.close()

if flag == 0:
	print("File successfully sorted")









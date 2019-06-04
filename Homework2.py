import datetime
import string
import random
import csv
import os

def gen_code_file(secretword:str, freq:int, maxlength:int):
	letters = string.ascii_letters
	datestamp = str(datetime.date.today())
	wordlocations = []
	f = open("random_letters_new.txt", 'w')
	for _ in range(freq):
		wordlocations.append(random.randint(0,maxlength))
	
	wordlocations.sort()
	writefifo =''
	j=0
	for i in range(maxlength):
		if (len(wordlocations) ==0) | ((j+1)>len(wordlocations)):
			writefifo+=random.choice(letters)
		elif i == wordlocations[j]:
			writefifo+=secretword
			if j==0:
				writefifo+=datestamp
			j+=1
		else:
			writefifo+=random.choice(letters)
	for i in range(len(writefifo)):
		if (i % 200) ==0:
			writefifo= writefifo[:i] + "\n" + writefifo[i:]
	f.write(writefifo)
	f.close()

def findWord(filename:str, word:str):
	returnarray=[]
	try:
		f = open(filename, 'r')
		filedata = f.read()
	except FileNotFoundError:
		print("Input file doesn't exist")
		return -1
	for i in range(len(filedata)):
		if filedata[i:i+len(word)] == word:
			returnarray.append(i)
	return returnarray

def dataSorter(filename:str):
	outputdict = {}
	keylist=[]
	longest=0
	with open(filename, newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row['Category'] in outputdict:
				if row['Value'] not in outputdict[row['Category']]:
					outputdict[row['Category']].append(row['Value'])
			else:
				outputdict[row['Category']] = [row['Value']] 
		for key in outputdict:
			keylist.append(key)
			outputdict[key].sort()
			if len(outputdict[key]) > longest:
				longest = len(outputdict[key])
		keylist.sort()
	csvfile.close()
	with open('sorted_data.csv', 'w', newline='') as newcsvfile:
		writer = csv.DictWriter(newcsvfile, keylist)
		writer.writeheader()
		for i in range(longest):
			out = {}
			for key in outputdict:
				if len(outputdict[key])> i:
					out[key]= outputdict[key][i]
			writer.writerow(out)
	newcsvfile.close()

def dataRecorder(filename:str, record:dict):
	exists = os.path.isfile(filename)
	with open(filename, 'a', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, ["Name", "Weight", "Height"])
		if not exists:
			writer.writeheader()
		writer.writerow(record)
		
	csvfile.close()

		

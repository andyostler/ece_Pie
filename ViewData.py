import os
import sys
import re
import socket
import matplotlib.pyplot as plot

def main(host, option, filename='*'):
	distance=[]
	d_timestamp=[]
	percent = []
	p_timestamp=[]
	try:
		command = 'scp pi@host:/home/pi/Documents/'+ filename+' '+filename
		os.system(command)
		if path.exists(filename):
            with open(filename,'r') as rfile:
                reader = csv.DictReader(rfile,['Timestamp','Data Type','Data'],delimiter=',')
                next(reader)
                for row in reader:
					if row['Data Type'] == 'Percent':
						percent.append(row['Data'])
						p_timestamp.append(row['Timestamp'])
					else:
						distance.append(row['Data'])
						d_timestamp.append(row['Timestamp'])
		
		if option:
			if percent!=[]:
				plt.subplot(2,1,1)
				plt.plot(d_timestamp, distance,'o-')
				plt.xlabel("Timestamps")
				plt.ylabel("Distance in cm")
				plt.title("Distance From Sensor Over Time")
				
				plt.subplot(2,1,2)
				plt.plot(p_timestamp, percent,'o-')
				plt.xlabel("Timestamps")
				plt.ylabel("Percent of Potentiometer")
				plt.title("Percent of Potemtionmeter Used Over Time")
				plt.show()
			else:
				plt.plot(d_timestamp, distance,'o-')
				plt.xlabel("Timestamps")
				plt.ylabel("Distance in cm")
				plt.title("Distance From Sensor Over Time")
				
				
	except:
		print("file or computer not available")
	
	
if __name__== "__main__":
	try:
		if((re.match('\d{3}.\d{1,3}.\d{1,3}.\d{1,3}',sys.argv[1])!= None) & (re.match('\d',sys.argv[2])!= None)):
			main(sys.argv[1],sys.argv[2],sys.argv[3])
		else:
			print("Incorrect arguments")
	except:
		print("No arguments given")
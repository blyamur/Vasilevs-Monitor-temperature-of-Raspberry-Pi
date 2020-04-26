import os
import time

def measure_temp():
		#temp = os.popen("vcgencmd measure_temp").readline()
		temp = "56.9'C"
		#show =  float("%.2f" % temp)
		temp.replace("temp=","")
		return(temp.replace("'C",""))
		

while True:
		#print(measure_temp())
		
		print(round(measure_temp()))
		time.sleep(1)

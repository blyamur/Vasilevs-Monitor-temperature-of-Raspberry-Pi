import os
import time

FAN_ON_MODE = 65  # (In celsius) The upper temperature threshold at which cooling is turned on.
FAN_OFF_MODE = 55  # (In celsius) Lower temperature threshold at which cooling is turned off
SLEEP_INTERVAL = 5  # (In seconds) Temperature Check Interval
GPIO_PIN = 17  # GPIO pin used for cooling control

def measure_temp():
		temp = os.popen("vcgencmd measure_temp").readline()
		#show =  float("%.2f" % temp)
		temp.replace("temp=","")
		return(temp.replace("'C",""))
		

while True:
		#print(measure_temp())
		fan = OutputDevice(GPIO_PIN)
		print(round(measure_temp()))
		if temp > FAN_ON_MODE:
                        fan.on()
                elif fan.value and temp < FAN_OFF_MODE:
                         fan.off()
		time.sleep(SLEEP_INTERVAL)

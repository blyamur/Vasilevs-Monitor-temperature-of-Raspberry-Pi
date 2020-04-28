import os
import time
import RPi.GPIO as GPIO

FAN_ON_MODE = 65  # (In celsius) The upper temperature threshold at which cooling is turned on.
FAN_OFF_MODE = 55  # (In celsius) Lower temperature threshold at which cooling is turned off
SLEEP_INTERVAL = 5  # (In seconds) Temperature Check Interval
SLEEP_INTERVAL_FAN = 5  # (In seconds) Temperature Check Interval

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


def measure_temp():
       temp = os.popen("vcgencmd measure_temp").readline()
       #show =  float("%.2f" % temp)
       temp.replace("temp=","")
       return(temp.replace("'C",""))
	#return float(m.group(1))	

while True:
       #print(measure_temp()
       print(round(measure_temp()))
       if temp > FAN_ON_MODE:
                GPIO.output(4, True)
                time.sleep(SLEEP_INTERVAL_FAN)
       elif fan.value and temp < FAN_OFF_MODE:
                GPIO.output(4, False)
       time.sleep(SLEEP_INTERVAL)

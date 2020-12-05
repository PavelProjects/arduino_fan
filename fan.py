import time
import subprocess
import os 
import signal
import sys

def signal_handler(sig, frame):
    os.system(tunrOff)
    sys.exit(0)

device  = "/dev/ttyUSB0"
max_temp = int(input('Max temperature : '))
sleep_time = int(input('Sleep time : '))

if max_temp == 0:
    max_temp = 60
if sleep_time == 0:
    sleep_time = 2

tunrOn = "echo  \'1\' > " + device
tunrOff = "echo  \'0\' > " + device
prev_temp = max_temp
flag = True

signal.signal(signal.SIGINT, signal_handler)

while flag and flag == 1:
    core_temp = subprocess.Popen(['sensors', '-u'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = core_temp.communicate()
    temp = int(repr(out).split('\\n').pop(3).split(' ').pop(3).split('.').pop(0))
    print(temp)
    if temp > max_temp and prev_temp > max_temp:
        os.system(tunrOn)
    else:
        os.system(tunrOff)
    prev_temp = temp
    time.sleep(sleep_time)
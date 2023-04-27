import serial #Serial imported for Serial communication
import time #Required to use delay functions
import subprocess

ArduinoSerial = serial.Serial(port='/dev/ttyACM0',baudrate=9600)
time.sleep(2) #wait for 2 seconds for the communication to get established

playpause = "playerctl --player=spotify play-pause"
check_vol = "playerctl --player=spotify volume"

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
    current_vol = float(subprocess.check_output(check_vol, shell=True))
    vol_up = f"playerctl --player=spotify volume {current_vol+0.05} +"
    vol_down = f"playerctl --player=spotify volume {current_vol-0.05} -"
    
    if 'Play/Pause' in incoming:
        subprocess.run(playpause, shell=True)

    if 'Volume Up' in incoming:
        subprocess.run(vol_up, shell=True)
        
    if 'Volume Down' in incoming:
        subprocess.run(vol_down, shell=True)

    incoming = ""

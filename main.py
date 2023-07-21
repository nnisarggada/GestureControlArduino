import serial #Serial imported for Serial communication
import time #Required to use delay functions
import subprocess

ArduinoSerial = serial.Serial(port='/dev/ttyACM0',baudrate=9600)
time.sleep(2) #wait for 2 seconds for the communication to get established

playpause = "playerctl play-pause"

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
    vol_up = "pactl set-sink-volume @DEFAULT_SINK@ +10%"
    vol_down = "pactl set-sink-volume @DEFAULT_SINK@ -10%"
    
    if 'Play/Pause' in incoming:
        subprocess.run(playpause, shell=True)

    if 'Volume Up' in incoming:
        subprocess.run(vol_up, shell=True)
        
    if 'Volume Down' in incoming:
        subprocess.run(vol_down, shell=True)

    incoming = ""

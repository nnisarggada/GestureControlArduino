import serial #Serial imported for Serial communication
import time #Required to use delay functions
import subprocess

ArduinoSerial = serial.Serial(port='/dev/ttyACM0',baudrate=9600)
time.sleep(2) #wait for 2 seconds for the communication to get established

playpause = "playerctl play-pause"
vup = "pactl -- set-sink-volume 0 +10%"
vdown = "pactl -- set-sink-volume 0 -10%"

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)
    
    if 'Play/Pause' in incoming:
        subprocess.run(playpause, shell=True)

    if 'Volume Up' in incoming:
        subprocess.call(['sh','./increase-spotify-volume.sh'])
        
    if 'Volume Down' in incoming:
        subprocess.call(['sh','./decrease-spotify-volume.sh'])

    incoming = ""

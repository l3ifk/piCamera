# Pi Camera
A simple project to turn a RaspberryPi and a camera module to a camera :)
![image](https://github.com/l3ifk/piCamera/assets/100339546/53b89d04-5eb0-4cd8-9ffb-e1b39f3be265)

I run it with a RaspberryPi Zero 2W
Camera module is the HQ Camera module by Raspberry Pi
and a PiSugar 2 to power everything

Here are some sample pictures to let you see the quality of it:

![image](https://github.com/l3ifk/piCamera/assets/100339546/b1638949-2588-4b98-88f8-a68cbbfb83f7) ![image](https://github.com/l3ifk/piCamera/assets/100339546/05c9af21-cf99-4a5e-995f-1b665bc83564) ![image](https://github.com/l3ifk/piCamera/assets/100339546/e35e6ec5-bedb-41b6-a7b4-ccd76e8d32cc) ![image](https://github.com/l3ifk/piCamera/assets/100339546/ae9fba9e-867e-41eb-9348-38d6c093e82d) ![image](https://github.com/l3ifk/piCamera/assets/100339546/aa064e5f-e08c-4c2d-9c15-243ec2720a01)


# Functionality

The script I wrote uses the input of 2 buttons, one to take a picture and one for recording videos.
Press the Video button once to start a video and once again to end the recording.
Note that you need a display with HDMI input! 
If the display gets its picture through the GPIO pins, then it won't be able to display the current video the camera is seeing...

# Installation

I flashed Rapsberry Pi Os Lite 64-Bit to my Pi Zero 2W and used ssh to set everything up.

A Pi Zero 1W would in theory work but give you lower framerates and longer waiting time to take high resolution pictures.

In the camera.py script, you'll see that I already restricted the resolution of the camera module, because it would take me up to 5 seconds to take a full resolution image...

So a stronger Pi would be an advantage to reduce this timing.

**Note** You have to create two folders in your home directory for the script to work:

- Pictures
- Videos

Check the Spelling and pay attention that the first letter is capitalized!
That's because in the python script want's to save pictures under /home/pi/Pictures and videos under /home/pi/Videos.

# Ecexute at start-up

I used systemd to start the script upon system start. 
I added the **start_camera.sh** script too.

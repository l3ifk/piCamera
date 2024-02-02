from datetime import datetime
from gpiozero import Button
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time
from libcamera import Transform
import libcamera

picb=Button(20)
vidb=Button(21)
picam=Picamera2()
preview_config = picam.create_preview_configuration(transform=Transform(hflip=True, vflip=True))
video_config=picam.create_video_configuration(transform=Transform(hflip=True, vflip=True))
capture_config=picam.create_still_configuration({"size": (2565, 1923)}, transform=Transform(hflip=True, vflip=True))
picam.options["compress_level"]=1
picam.configure(preview_config)
picam.set_controls({"AwbEnable": True, "AwbMode": libcamera.controls.AwbModeEnum.Auto})
encoder = H264Encoder()
running=True
recording=False
timestamp=datetime.now()
print(str(timestamp))

def high_res_picture():
	if recording:
		time.sleep(1)
	else:
		timestamp=datetime.now()
		picam.switch_mode_and_capture_file(capture_config, "/home/pi/Pictures/"+str(timestamp)+".jpg")
		print('took picture')
high_res_picture

def video(): 
	global recording
	timestamp=datetime.now()
	if recording:
		recording=False
		picam.stop_encoder()
		picam.switch_mode(preview_config)
		time.sleep(2)
	else:
		picam.switch_mode(video_config)
		picam.start_encoder(encoder, "/home/pi/Videos/"+str(timestamp)+".h264")
		recording=True
video

def picture():
	timestamp=datetime.now()
	picam.capture_file("/home/pi/Pictures/lowRes/"+str(timestamp)+".jpg")
#	print('picture taken')
picture

def button_push():
	print("button pushed!")
button_push

picam.start_preview(Preview.DRM, width=1280, height=850, transform=Transform(hflip=1, vflip=1))
picam.start()
vidb.when_pressed=video
try:
	while running:
#		print('Active')
		if picb.is_pressed:
			high_res_picture()
			time.sleep(0.2)
		else:
			time.sleep(0.2)

except KeyboardInterrupt:
	picam.stop_preview()
	running=False

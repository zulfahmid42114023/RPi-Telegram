import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO_PIR = 12
GPIO_LED = 16
GPIO.setup(GPIO_PIR,GPIO.IN)
GPIO.setup(GPIO_LED,GPIO.OUT)
Current_State  = 0
Previous_State = 0

try:

	while GPIO.input(GPIO_PIR)==1:
		Current_State  = 0
 	print "Sensor Siap!!!"

	while True:
		Current_State = GPIO.input(GPIO_PIR)
		if Current_State==1 and Previous_State==0:
			print "Terdeteksi!!"
			GPIO.output(GPIO_LED, GPIO.HIGH)
			time.sleep(2)

			os.system('fswebcam -r 640x360 /home/zulfahmi/Foto/photo.jpg')
			os.system('/home/zulfahmi/tg/bin/telegram-cli -k server.pub -WR -e  "send_photo Zeef /home/zulfahmi/Foto/photo.jpg"')
			Previous_State=1
			Previous_State=1
			GPIO.output(16, GPIO.LOW)

		elif Current_State==0 and Previous_State==1:
			print "Sensor Siap!!!"
			Previous_State=0
			time.sleep(0.1)
 
except KeyboardInterrupt:
	print "  Quit"
	GPIO.cleanup()

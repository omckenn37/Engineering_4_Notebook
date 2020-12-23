import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()

#draw.ellipse((x, top, x + shape_width, bottom), outline=255, fill=0)

#disp.image(image)
#disp.display()



while True:
	accel, mag = accelerometer.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag

	draw.text((x, top), "Accel x ={0}".format(accel_x), font=font, fill=255)
	disp.image(image)
	disp.display()
	

import time

from rpi_ws281x import PixelStrip, Color

#Setup the neopixel strip
LEDCOUNT = 8  
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = False 
BRIGHTNESS = 200    #255 max

#Initialise he strip
strip = PixelStrip(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS)

strip.begin()

for x in range(LEDCOUNT):
    strip.setPixelColor(x, Color(255,170,150)) #I wanted a warm-ish white
strip.show()

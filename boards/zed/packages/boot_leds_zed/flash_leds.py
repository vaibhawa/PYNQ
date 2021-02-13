#! /usr/bin/env python3.6

from pynq import Overlay
from time import sleep
from pynq.lib import AxiGPIO

ol = Overlay('base.bit')
leds = AxiGPIO(ol.ip_dict['axi_gpio_1']).channel1

for i in range(8):
	leds[0:4].on()
	sleep(.2)
	leds[0:4].off()
	sleep(.2)



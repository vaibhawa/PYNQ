#! /usr/bin/env python3.6

from pynq.overlays.base import BaseOverlay
from time import sleep
from pynq.lib import AxiGPIO

ol = BaseOverlay('base.bit')

for i in range(8):
	ol.leds[0:4].on()
	sleep(.2)
	ol.leds[0:4].off()
	sleep(.2)



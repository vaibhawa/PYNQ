import pynq
import pynq.lib
import time

__author__ = "Vaibhawa"
__email__ = ""

    """ The Base Overlay for the Zedboard
	This overlay is designed to interact with some of the on board peripherals
    and external interfaces of the Zedboard. It exposes the following
    attributes

    leds : AxiGPIO
         8-bit output GPIO for interacting with the red LEDs LD0-7
    buttons : AxiGPIO
         5-bit input GPIO for interacting with the buttons BTN0-4
    switches : AxiGPIO
         8-bit input GPIO for interacting with the switches SW0-7

    """
class BaseOverlay(pynq.Overlay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_loaded():
            self.leds = AxiGPIO(self.ip_dict['axi_gpio_1']).channel1
            self.buttons = AxiGPIO(self.ip_dict['axi_gpio_0']).channel1
            self.switches = AxiGPIO(self.ip_dict['axi_gpio_0']).channel2
            self.leds.setdirection("out")
            self.leds.setlength(4)
            self.buttons.setdirection("in")
            self.buttons.setlength(4)
            self.switches.setdirection("in")
            self.switches.setlength(4)
    def download(self):
        super().download()

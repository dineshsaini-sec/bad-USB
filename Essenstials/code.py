import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(1)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(0.3)

layout.write("chrome https://www.whitescreen.online/blue-screen-of-death-windows-10/")
time.sleep(0.2)

kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(3)

layout.write("f")
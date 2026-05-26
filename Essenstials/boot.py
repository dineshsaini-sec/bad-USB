import usb_hid
import storage

storage.disable_usb_drive()
usb_hid.enable(usb_hid.Device.KEYBOARD)
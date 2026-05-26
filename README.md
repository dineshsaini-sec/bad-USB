# bad-USB

A collection of payloads, scripts, and essential files leveraging the RP2040 microcontroller (such as the Waveshare RP2040-One) for automated Keystroke Injection attacks.

---

## Features

* Hardware Compatibility: Optimized for RP2040-based development boards.
* CircuitPython Powered: Built using CircuitPython for easy payload modification and fast deployment.
* Automated Execution: Emulates a standard USB HID keyboard to inject keystrokes into target machines at blazing speeds.

---

## Repository Structure

* Essenstials/ - Core libraries, dependency files, and foundational setups.
* bsod.html - A sample asset/payload designed to trigger a mock Blue Screen of Death for demonstration purposes.
* adafruit-circuitpython-waveshare_rp2040_one-en_GB-10.2.1.uf2 - The required CircuitPython firmware for the Waveshare RP2040-One board.
* adafruit-circuitpython-bundle-10.x-mpy-20260520.zip - The official library bundle containing necessary HID drivers.
* flash_nuke.uf2 - A utility firmware file used to completely wipe the RP2040 flash memory when resetting the board.

---

## Quick Start Guide

### 1. Flash CircuitPython
1. Hold down the BOOT/BOOTSEL button on your RP2040 board.
2. Connect the board to your computer via USB.
3. Drag and drop the adafruit-circuitpython-waveshare_rp2040_one-en_GB-10.2.1.uf2 file onto the mounted RPI-RP2 drive.
4. The board will reboot and mount as a new drive named CIRCUITPY.

### 2. Install Libraries
1. Extract the adafruit-circuitpython-bundle-10.x-mpy-20260520.zip archive.
2. Locate the adafruit_hid folder inside the bundle.
3. Copy the adafruit_hid folder into the lib/ directory on your CIRCUITPY drive.

### 3. Deploy Payloads
1. Copy your primary execution script into the root of the CIRCUITPY drive.
2. Rename your main script to code.py to ensure it executes automatically whenever the device is plugged into a target machine.

---

## Disclaimer

This repository is created strictly for educational, testing, and authorized security auditing purposes. Standard rules of engagement apply. The developer assumes no liability for any misuse, damage, or illegal activities conducted with these tools.

# Toolchain Setup & Flash Instructions

## 1) Python Virtual Environment
Always activate the evironment before doing anything using esptool or mpremote

```bash
#To create the venv
python3 -m venv -/embedded_venv

# To Activate
source ~/embedded_venv/bin/activate

## 2) Flashing MicroPython

# Locate the serial bus
ls /dev/ttyUSB* /dev/ttyACM*

# Erase existing flash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

# Write new firmware offset 0x1000
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud460800 write_flash -z 0x1000 EXP32_GENERIC-*.bin




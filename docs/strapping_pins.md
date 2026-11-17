# ESP32 Strapping Pins

The strapping pins (GPIO 0, 2, 5, 12, 15) determine the boot mode of the ESP32 when it receives power. 
If external hardware (like a button) holds these pins in the wrong state during boot, the ESP32 will fail to run the firmware or may enter programming mode instead. 

**Rule of thumb:** Never use GPIO 0, 2, 5, 12, or 15 for input buttons or sensors. Use safe pins like GPIO4, 13, 14, 16, 17, etc.

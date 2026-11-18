# Week 1: GPIO, Blink & Breadboard Fundamentals

This repository contains my Week 1 progress for the 52-week Embedded Systems curriculum. 

## Contents
- `blink.py`: MicroPython script to blink the onboard LED (GPIO2).
- `notes/`: Handwritten formulas and breadboard logic.
- `docs/`: Toolchain setup notes and ESP32 strapping pin research.

## Status
- [x] Toolchain (esptool, mpremote) installed and verified.
- [x] Blind code written and tested in simulator.
- [ ] Hardware verified (ESP32 arriving tomorrow).

## Hardware Verification (Nov 18)

Today I successfully flashed MicroPython to the ESP32 and verified the hardware using a multimeter.

### Measurements
| Measurement | Theoretical | Measured | % Error |
| :--- | :--- | :--- | :--- |
| 3V3 Rail | 3.30 V | [Your 3V3 reading] V | [Calculate] % |
| Divider Midpoint (10k/10k) | 1.65 V | [Your divider reading] V | [Calculate] % |
| Voltage across 220 Ω | ~1.3 V | 1.15 V | ~11.5 % |
| LED Current | 5.9 mA | 5.23 mA | 11.3 % |

### Gallery
![Breadboard Setup](notes/day1b_led_breadboard.jpg)

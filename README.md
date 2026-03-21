# Autonomous GPS Quadcopter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-in%20progress-yellow)]()
[![ArduPilot](https://img.shields.io/badge/ArduPilot-4.6.3-blue)]()

A 1.85kg autonomous quadcopter platform designed for GPS waypoint missions and Raspberry Pi MAVLink control.

![Quadcopter Overview](images/quad-main.jpg)

## 🎯 Project Overview

This project documents the complete build of an autonomous quadcopter capable of executing GPS waypoint missions, position hold, and return-to-launch functionality, all controlled via a Raspberry Pi companion computer using MAVLink protocol.

### Key Features

- ✅ **GPS Waypoint Navigation** - Execute complex flight paths autonomously
- ✅ **MAVLink Control** - Raspberry Pi integration via DroneKit-Python
- ✅ **Position Hold** - GPS-based hovering and loiter modes
- ✅ **Return to Launch** - Automatic return on low battery or signal loss
- ✅ **Long Flight Time** - 12-15 minutes on 3000mAh 4S battery
- ✅ **High Performance** - 1.89:1 thrust-to-weight ratio
- 🔲 **Computer Vision Ready** - Expandable for CV applications

### Project Status

🟡 **In Development - 75% Complete**

**Completed:**
- ✅ ArduCopter firmware flashed (V4.6.3)
- ✅ ESC and motor configuration
- ✅ GPS module connected and tested
- ✅ Frame design finalized

**In Progress:**
- 🔄 Sensor calibrations
- 🔄 Frame assembly
- 🔄 Raspberry Pi MAVLink setup

**Upcoming:**
- 🔲 First test flight
- 🔲 Autonomous mission testing
- 🔲 Computer vision integration

---

## 📊 Technical Specifications

### Flight Performance
| Specification | Value |
|--------------|-------|
| **Total Weight** | 1.85 kg (all-up) |
| **Thrust-to-Weight** | 1.89:1 |
| **Flight Time (Hover)** | 12-15 minutes |
| **Flight Time (Aggressive)** | 8-10 minutes |
| **Max Thrust** | 3500g (875g per motor) |
| **Frame Size** | 450mm diagonal |
| **Propeller Size** | 11×7 inches |

### Power System
| Component | Specification |
|-----------|--------------|
| **Battery** | 3000mAh 4S LiPo (14.8V, 60C) |
| **Motors** | D2830-12 Brushless (×4) |
| **ESC** | Diatone Mamba F40 4-in-1 (40A) |
| **Protocol** | Dshot600 |

### Flight Controller
| Component | Specification |
|-----------|--------------|
| **FC** | Matek F405-Wing V2 |
| **Processor** | STM32 F405 (168MHz) |
| **IMU** | ICM-42688-P |
| **Barometer** | DPS310 |
| **Firmware** | ArduCopter V4.6.3 |

### Autonomous System
| Component | Specification |
|-----------|--------------|
| **GPS** | Beitian BN-880 (Ublox M8N) |
| **Companion Computer** | Raspberry Pi 4 (2-4GB) |
| **Communication** | MAVLink (921600 baud) |
| **Software** | DroneKit-Python, MAVProxy |

---

## 🛠️ Hardware

### Bill of Materials

See [hardware/bill-of-materials.md](hardware/bill-of-materials.md) for complete parts list.

**Core Components:**
- Matek F405-Wing V2 Flight Controller
- Diatone Mamba F40 4-in-1 ESC (40A)
- D2830-12 Brushless Motors (×4)
- 11×7 Propellers (2× CW, 2× CCW)
- 3000mAh 4S 60C LiPo Battery
- Beitian BN-880 GPS Module
- Raspberry Pi 4 (2GB or 4GB)
- 10× 18mm Carbon Fiber Rods (300mm length)
- XT60 Connectors, Bullet Connectors
- Wiring, Heat Shrink, Solder

**Total Cost:** ~$250-$400 USD

### Frame Design

**Updated Frame Configuration:**
- **Material:** Carbon fiber rods (18mm diameter)
- **Configuration:** 10× rods at 300mm length each
- **Motor spacing:** 450mm diagonal (motor-to-motor)
- **Center plate:** Custom mounting for FC stack

See [hardware/frame/frame-assembly.md](hardware/frame/frame-assembly.md) for assembly instructions.

---

## 📚 Documentation

### Setup Guides
- [Build Guide](docs/build-guide.md) - Complete step-by-step assembly
- [Hardware Specifications](docs/hardware-specs.md) - Detailed component specs
- [Flight Controller Setup](docs/flight-controller-setup.md) - ArduCopter configuration
- [MAVLink Setup](docs/mavlink-setup.md) - Raspberry Pi integration
- [Calibration Guide](docs/calibration-guide.md) - Sensor calibration procedures

### Reference
- [Wiring Diagrams](hardware/wiring-diagrams/) - Complete wiring schematics
- [Troubleshooting](docs/troubleshooting.md) - Common issues and solutions
- [Safety Guidelines](docs/safety.md) - Safe operation procedures

---

## 💻 Software

### Raspberry Pi Setup

**Requirements:**
```bash

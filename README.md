# Autonomous GPS Quadcopter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-in%20progress-yellow)]()
[![ArduPilot](https://img.shields.io/badge/ArduPilot-4.6.3-blue)]()

A 1.85kg autonomous quadcopter platform built for GPS waypoint navigation, position hold, return-to-launch, and Raspberry Pi MAVLink control.

## Project Overview

This repo contains everything needed to build and program an autonomous quadcopter from scratch -- hardware specs, wiring guides, ArduCopter configuration, and Python flight control software.

### Capabilities

- GPS waypoint navigation via DroneKit-Python
- MAVLink control from Raspberry Pi 4 companion computer
- GPS position hold and altitude hold
- Automatic return-to-launch on low battery or signal loss
- 12-15 minute hover flight time on 3000mAh 4S LiPo
- 1.89:1 thrust-to-weight ratio
- Computer vision ready (future expansion)

### Project Status

**In Development**

Completed:
- ArduCopter V4.6.3 firmware flashed
- ESC and motor configuration
- GPS module connected and tested
- Frame design finalized

In Progress:
- Sensor calibrations
- Frame assembly
- Raspberry Pi MAVLink integration

Upcoming:
- First test flight
- Autonomous mission testing
- Computer vision integration

---

## Technical Specifications

### Flight Performance

| Spec | Value |
|------|-------|
| Total Weight | 1.85 kg (all-up) |
| Thrust-to-Weight | 1.89:1 |
| Flight Time (Hover) | 12-15 minutes |
| Flight Time (Aggressive) | 8-10 minutes |
| Max Thrust | 3500g (875g per motor) |
| Frame Size | 450mm diagonal |
| Propeller Size | 11x7 inches |
| GPS Accuracy | +/- 2-3 meters |
| Wind Resistance | Stable in 5-10 mph |

### Core Components

| Component | Model |
|-----------|-------|
| Flight Controller | Matek F405-Wing V2 (STM32 F405, 168MHz) |
| ESC | Diatone Mamba F40 4-in-1 (40A, Dshot600) |
| Motors | D2830-12 Brushless x4 (850 KV) |
| Battery | 3000mAh 4S LiPo (14.8V, 60C) |
| GPS | Beitian BN-880 (Ublox M8N + compass) |
| Companion Computer | Raspberry Pi 4 (2-4GB) |
| Frame | Custom carbon fiber rod (450mm, 10x 18mm rods) |
| Firmware | ArduCopter V4.6.3 |

**Total Cost:** ~$250-$400 USD

---

## Repository Structure

```
Autonomous-Drone/
├── README.md
├── LICENSE
├── config/
│   └── arducopter-params.param    # Flight controller parameters
├── docs/
│   ├── build-guide.md             # Step-by-step assembly
│   ├── hardware-specs.md          # Detailed component specs
│   ├── flight-controller-setup.md # ArduCopter configuration
│   ├── mavlink-setup.md           # Raspberry Pi integration
│   ├── calibration-guide.md       # Sensor calibration procedures
│   ├── troubleshooting.md         # Common issues and fixes
│   └── safety.md                  # Safety protocols
├── hardware/
│   ├── bill-of-materials.md       # Full parts list with costs
│   ├── frame/
│   │   └── frame-assembly.md      # Frame build instructions
│   └── wiring-diagrams/
│       └── wiring-guide.md        # Complete wiring reference
└── software/
    ├── requirements.txt
    ├── setup.sh                   # Raspberry Pi setup script
    ├── drone_controller.py        # Core DroneKit controller class
    ├── waypoint_mission.py        # Autonomous waypoint missions
    └── monitoring_dashboard.py    # Real-time telemetry display
```

---

## Quick Start

### 1. Hardware Assembly

See the [Build Guide](docs/build-guide.md) for full step-by-step instructions. The [Bill of Materials](hardware/bill-of-materials.md) has the complete parts list.

### 2. Flash and Configure Flight Controller

Connect the Matek F405-Wing V2 via USB and flash ArduCopter V4.6.3 using QGroundControl or Mission Planner. Then load the parameter file:

```
config/arducopter-params.param
```

See [Flight Controller Setup](docs/flight-controller-setup.md) for details.

### 3. Calibrate Sensors

Follow the [Calibration Guide](docs/calibration-guide.md):
- Accelerometer (6-position)
- Compass (outdoor, all orientations)
- ESC throttle range

### 4. Set Up Raspberry Pi

```bash
# Clone this repo on the Pi
git clone https://github.com/rishith-c/Autonomous-Drone.git
cd Autonomous-Drone

# Run the setup script
chmod +x software/setup.sh
./software/setup.sh

# Or install manually
pip3 install -r software/requirements.txt
```

See [MAVLink Setup](docs/mavlink-setup.md) for UART wiring and configuration.

### 5. Test Connection

```python
from dronekit import connect

vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)
print(f"GPS: {vehicle.gps_0}")
print(f"Battery: {vehicle.battery}")
print(f"Mode: {vehicle.mode.name}")
vehicle.close()
```

### 6. Fly a Mission

```python
from software.drone_controller import DroneController

drone = DroneController()
drone.arm()
drone.takeoff(5)
drone.goto(37.12345, -121.12345, 10)
drone.rtl()
drone.close()
```

---

## System Architecture

### Power Distribution

```
[3000mAh 4S LiPo 14.8V]
         |
    [XT60 Connector]
         |
    [Mamba F40 ESC]
    /    |    |    \
   M1   M2   M3   M4
   |
   [VBAT/GND to FC]
   |
[Matek F405-Wing V2]
   |
   [5V BEC to peripherals]
   ├── GPS Module (5V)
   ├── Raspberry Pi (separate 5V BEC or USB power bank)
   └── Other peripherals
```

### Signal Flow

```
[Matek FC - ArduCopter]
   ├── ESC (Dshot600) --> Motors
   ├── GPS Module (UART3, 115200 baud)
   ├── Compass (I2C, integrated with GPS)
   ├── Raspberry Pi (UART2, MAVLink, 921600 baud)
   └── RC Receiver (optional, UART/SBUS)
```

### Control Architecture

```
User / Mission Planner
        |
Raspberry Pi (Python / DroneKit)
        | MAVLink commands
Flight Controller (ArduCopter)
        | Sensor fusion: GPS, IMU, Baro
ESC (motor speed commands)
        |
4x Brushless Motors
```

### Motor Layout (Quad X)

```
        FRONT
    M3 CCW    M1 CW
        \    /
         [FC]
        /    \
    M2 CW    M4 CCW

M1: Front Right (CW)
M2: Rear Left  (CW)
M3: Front Left  (CCW)
M4: Rear Right  (CCW)
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [Build Guide](docs/build-guide.md) | Complete assembly from start to finish |
| [Hardware Specs](docs/hardware-specs.md) | Detailed specs for every component |
| [Bill of Materials](hardware/bill-of-materials.md) | Full parts list with costs |
| [Wiring Guide](hardware/wiring-diagrams/wiring-guide.md) | All wiring connections |
| [Frame Assembly](hardware/frame/frame-assembly.md) | Frame construction |
| [Flight Controller Setup](docs/flight-controller-setup.md) | ArduCopter parameters |
| [MAVLink Setup](docs/mavlink-setup.md) | Raspberry Pi integration |
| [Calibration Guide](docs/calibration-guide.md) | Sensor calibration |
| [Troubleshooting](docs/troubleshooting.md) | Common problems and solutions |
| [Safety](docs/safety.md) | Safety protocols and checklists |

---

## Future Enhancements

**Short Term (1-3 months)**
- FPV camera for first-person view
- RC receiver for manual backup
- Obstacle avoidance sensors
- Telemetry radio for longer range

**Medium Term (3-6 months)**
- Computer vision with OpenCV
- Object tracking and following
- Precision landing using visual markers
- Advanced path planning

**Long Term (6+ months)**
- Machine learning integration
- Autonomous inspection missions
- Multi-drone swarm coordination
- Indoor flight with alternative positioning
- Payload delivery system

---

## Resources

- [ArduPilot Documentation](https://ardupilot.org/copter/)
- [DroneKit-Python Docs](https://dronekit-python.readthedocs.io/)
- [MAVLink Protocol](https://mavlink.io/en/)
- [Matek F405-Wing V2 Docs](http://www.mateksys.com/?portfolio=f405-wing-v2)
- [QGroundControl](http://qgroundcontrol.com/)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

# MAVLink Setup

Raspberry Pi 4 integration with the flight controller via MAVLink protocol.

---

## Hardware Connection

### UART Wiring

| Raspberry Pi | FC Pin | Wire |
|--------------|--------|------|
| GPIO 14 (pin 8) - TX | RX2 (UART2 RX) | 24-26 AWG |
| GPIO 15 (pin 10) - RX | TX2 (UART2 TX) | 24-26 AWG |
| Pin 6 - GND | GND | 24-26 AWG |

TX crosses to RX on both ends. Common ground is required.

### Power

Power the RPi separately from the FC. Options:
- USB power bank (5V 3A) connected to USB-C
- Dedicated 5V BEC from the battery, connected to GPIO pins 2 (+5V) and 6 (GND)

Do not power the RPi from the FC's 5V output -- it cannot supply enough current.

---

## Raspberry Pi Software Setup

### Option 1: Run the Setup Script

```bash
git clone https://github.com/rishith-c/Autonomous-Drone.git
cd Autonomous-Drone
chmod +x software/setup.sh
./software/setup.sh
```

### Option 2: Manual Install

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
sudo apt install python3-pip python3-dev -y

# Install MAVProxy (ground station / message router)
sudo pip3 install mavproxy

# Install DroneKit (Python API for MAVLink)
sudo pip3 install dronekit dronekit-sitl

# Install pymavlink (low-level MAVLink library)
sudo pip3 install pymavlink numpy
```

### Enable UART on the Pi

```bash
# Add to /boot/config.txt:
enable_uart=1

# Disable the serial console (it conflicts with UART):
sudo raspi-config
# Navigate: Interface Options -> Serial Port
# Login shell over serial: No
# Serial port hardware enabled: Yes

# Reboot
sudo reboot
```

After reboot, the UART is available at `/dev/ttyAMA0`.

---

## Flight Controller Parameters

These must be set on the FC (via ground station or param file):

```
SERIAL2_PROTOCOL = 2    (MAVLink2)
SERIAL2_BAUD     = 921  (921600 baud)
```

Match the baud rate between the FC parameter and the Python connection string.

---

## Testing the Connection

### Basic Connection Test

```python
from dronekit import connect

vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)

print(f"GPS: {vehicle.gps_0}")
print(f"Battery: {vehicle.battery}")
print(f"Mode: {vehicle.mode.name}")
print(f"Armed: {vehicle.armed}")

vehicle.close()
```

If this works, MAVLink is functioning.

### Connection Troubleshooting

| Problem | Fix |
|---------|-----|
| "Connection timed out" | Check TX/RX crossover wiring |
| "No heartbeat" | Verify common ground between RPi and FC |
| "Permission denied on /dev/ttyAMA0" | Run `sudo chmod 666 /dev/ttyAMA0` or add user to dialout group |
| "Port not found" | Ensure UART is enabled in raspi-config and /boot/config.txt |
| Garbled data | Baud rate mismatch -- check both FC and Python use same value |

### Using MAVProxy

MAVProxy can act as a message router, forwarding MAVLink to multiple endpoints:

```bash
# Forward FC connection to UDP for ground station access over WiFi
mavproxy.py --master=/dev/ttyAMA0 --baudrate=921600 --out=udp:0.0.0.0:14550
```

Then connect QGroundControl on your laptop to `udp:<pi-ip>:14550`.

---

## Using the DroneController Class

The `software/drone_controller.py` module provides a clean interface:

```python
from drone_controller import DroneController

drone = DroneController('/dev/ttyAMA0', baud=921600)

# Read telemetry
telemetry = drone.get_telemetry()
print(telemetry)

# Arm and takeoff
drone.arm()
drone.takeoff(5)

# Fly to a waypoint
drone.goto(37.12345, -121.12345, 10)

# Return to launch
drone.rtl()

drone.close()
```

See `software/waypoint_mission.py` for multi-waypoint autonomous missions and `software/monitoring_dashboard.py` for a real-time telemetry display.

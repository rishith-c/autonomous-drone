"""
Autonomous waypoint mission using DroneKit.

Uploads a list of GPS waypoints to the flight controller and
executes them in AUTO mode. Includes a takeoff command at the
start and an RTL command at the end.

Usage:
    python3 waypoint_mission.py

Edit the WAYPOINTS list below to define your mission.
"""

import sys
import time

from dronekit import VehicleMode, Command, connect
from pymavlink import mavutil


DEFAULT_PORT = '/dev/ttyAMA0'
DEFAULT_BAUD = 921600

# Define your waypoints here: (latitude, longitude, altitude_meters)
WAYPOINTS = [
    (37.12345, -121.12345, 10),
    (37.12355, -121.12355, 15),
    (37.12365, -121.12335, 10),
]


def upload_mission(vehicle, waypoints):
    """
    Clear existing commands and upload a new mission.

    The mission consists of:
      1. Takeoff to the altitude of the first waypoint
      2. Navigate through each waypoint in order
      3. Return to launch
    """
    cmds = vehicle.commands
    cmds.clear()

    # Takeoff command
    cmds.add(Command(
        0, 0, 0,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0, 0,
        0, 0, 0, 0,
        0, 0, waypoints[0][2],
    ))

    # Waypoint commands
    for lat, lon, alt in waypoints:
        cmds.add(Command(
            0, 0, 0,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            0, 0,
            0, 0, 0, 0,
            lat, lon, alt,
        ))

    # Return to launch
    cmds.add(Command(
        0, 0, 0,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
        mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
        0, 0,
        0, 0, 0, 0,
        0, 0, 0,
    ))

    cmds.upload()
    print(f"Uploaded mission with {len(waypoints)} waypoints.")


def run_mission(vehicle):
    """Arm, switch to AUTO, and monitor until mission completes."""
    print("Setting AUTO mode...")
    vehicle.mode = VehicleMode("AUTO")

    print("Arming...")
    vehicle.armed = True
    while not vehicle.armed:
        print("  Waiting for arm...")
        time.sleep(0.5)

    print("Mission running.")
    while vehicle.mode.name == "AUTO":
        next_wp = vehicle.commands.next
        alt = vehicle.location.global_relative_frame.alt
        spd = vehicle.groundspeed
        bat = vehicle.battery.voltage
        print(f"  WP {next_wp} | Alt {alt:.1f}m | Speed {spd:.1f}m/s | Bat {bat:.1f}V")
        time.sleep(1)

    print(f"Mission ended. Mode: {vehicle.mode.name}")


def main():
    port = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORT
    baud = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_BAUD

    print(f"Connecting on {port} at {baud}...")
    vehicle = connect(port, wait_ready=True, baud=baud)
    print("Connected.")

    upload_mission(vehicle, WAYPOINTS)
    run_mission(vehicle)

    vehicle.close()
    print("Done.")


if __name__ == '__main__':
    main()

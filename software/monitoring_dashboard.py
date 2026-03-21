"""
Real-time telemetry monitoring dashboard.

Connects to the flight controller via MAVLink and prints
a live-updating telemetry display to the terminal.

Usage:
    python3 monitoring_dashboard.py
    python3 monitoring_dashboard.py /dev/ttyAMA0 921600

Press Ctrl+C to exit.
"""

import sys
import time

from dronekit import connect


DEFAULT_PORT = '/dev/ttyAMA0'
DEFAULT_BAUD = 921600
REFRESH_INTERVAL = 1  # seconds


def print_dashboard(vehicle):
    """Print a single frame of telemetry data."""
    v = vehicle
    loc = v.location

    print("\033[2J\033[H", end="")  # clear terminal
    print("=" * 50)
    print("  AUTONOMOUS DRONE - TELEMETRY")
    print("=" * 50)
    print(f"  Mode:         {v.mode.name}")
    print(f"  Armed:        {v.armed}")
    print(f"  System:       {v.system_status.state}")
    print("-" * 50)
    print(f"  GPS Sats:     {v.gps_0.satellites_visible}")
    print(f"  GPS Fix:      {v.gps_0.fix_type}")
    print(f"  Latitude:     {loc.global_frame.lat:.6f}")
    print(f"  Longitude:    {loc.global_frame.lon:.6f}")
    print(f"  Altitude:     {loc.global_relative_frame.alt:.2f} m")
    print("-" * 50)
    print(f"  Heading:      {v.heading} deg")
    print(f"  Groundspeed:  {v.groundspeed:.2f} m/s")
    print(f"  Airspeed:     {v.airspeed:.2f} m/s")
    print("-" * 50)
    print(f"  Battery:      {v.battery.voltage:.2f} V")
    print(f"  Current:      {v.battery.current:.2f} A")

    if v.battery.level is not None:
        print(f"  Remaining:    {v.battery.level}%")

    print("=" * 50)
    print("  Press Ctrl+C to exit")


def main():
    port = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORT
    baud = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_BAUD

    print(f"Connecting on {port} at {baud}...")
    vehicle = connect(port, wait_ready=True, baud=baud)
    print("Connected. Starting dashboard...\n")

    try:
        while True:
            print_dashboard(vehicle)
            time.sleep(REFRESH_INTERVAL)
    except KeyboardInterrupt:
        print("\nShutting down.")
    finally:
        vehicle.close()


if __name__ == '__main__':
    main()

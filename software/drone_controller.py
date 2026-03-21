"""
Core drone controller using DroneKit and MAVLink.

Provides a clean interface for arming, takeoff, waypoint navigation,
and landing via the Matek F405-Wing V2 flight controller.

Usage:
    from drone_controller import DroneController

    drone = DroneController('/dev/ttyAMA0', baud=921600)
    drone.arm()
    drone.takeoff(5)
    drone.goto(37.12345, -121.12345, 10)
    drone.rtl()
    drone.close()
"""

import sys
import time

from dronekit import VehicleMode, LocationGlobalRelative, connect


DEFAULT_PORT = '/dev/ttyAMA0'
DEFAULT_BAUD = 921600
TAKEOFF_COMPLETE_FRACTION = 0.95
POLL_INTERVAL = 0.5


class DroneController:
    """High-level controller for an ArduCopter-based quadcopter."""

    def __init__(self, connection_string=DEFAULT_PORT, baud=DEFAULT_BAUD):
        print(f"Connecting to vehicle on {connection_string} at {baud} baud...")
        self.vehicle = connect(connection_string, wait_ready=True, baud=baud)
        print("Connected.")

    def get_telemetry(self):
        """Return a dictionary of current vehicle state."""
        v = self.vehicle
        return {
            'mode': v.mode.name,
            'armed': v.armed,
            'gps_satellites': v.gps_0.satellites_visible,
            'gps_fix': v.gps_0.fix_type,
            'latitude': v.location.global_frame.lat,
            'longitude': v.location.global_frame.lon,
            'altitude_rel': v.location.global_relative_frame.alt,
            'heading': v.heading,
            'groundspeed': v.groundspeed,
            'airspeed': v.airspeed,
            'battery_voltage': v.battery.voltage,
            'battery_current': v.battery.current,
            'battery_level': v.battery.level,
        }

    def arm(self):
        """Switch to GUIDED mode and arm the motors."""
        print("Setting GUIDED mode...")
        self.vehicle.mode = VehicleMode("GUIDED")

        while self.vehicle.mode.name != "GUIDED":
            time.sleep(POLL_INTERVAL)

        print("Arming motors...")
        self.vehicle.armed = True

        while not self.vehicle.armed:
            print("  Waiting for arm...")
            time.sleep(POLL_INTERVAL)

        print("Armed.")

    def takeoff(self, target_altitude):
        """
        Take off to the given altitude in meters.
        Blocks until the target altitude is reached (within 95%).
        """
        if not self.vehicle.armed:
            print("Vehicle is not armed. Call arm() first.")
            return

        print(f"Taking off to {target_altitude}m...")
        self.vehicle.simple_takeoff(target_altitude)

        while True:
            alt = self.vehicle.location.global_relative_frame.alt
            print(f"  Altitude: {alt:.1f}m")
            if alt >= target_altitude * TAKEOFF_COMPLETE_FRACTION:
                print(f"Reached target altitude: {alt:.1f}m")
                break
            time.sleep(POLL_INTERVAL)

    def goto(self, lat, lon, alt):
        """
        Fly to the given GPS coordinate.
        Non-blocking -- returns immediately after sending the command.
        """
        point = LocationGlobalRelative(lat, lon, alt)
        print(f"Flying to ({lat}, {lon}) at {alt}m...")
        self.vehicle.simple_goto(point)

    def rtl(self):
        """Switch to Return to Launch mode."""
        print("Returning to launch...")
        self.vehicle.mode = VehicleMode("RTL")

    def land(self):
        """Switch to Land mode (land at current position)."""
        print("Landing...")
        self.vehicle.mode = VehicleMode("LAND")

    def set_mode(self, mode_name):
        """Switch to an arbitrary flight mode by name."""
        print(f"Setting mode: {mode_name}")
        self.vehicle.mode = VehicleMode(mode_name)

    def close(self):
        """Close the MAVLink connection."""
        print("Closing connection.")
        self.vehicle.close()


def main():
    """Quick connection test -- prints telemetry and exits."""
    port = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORT
    baud = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_BAUD

    drone = DroneController(port, baud)

    telemetry = drone.get_telemetry()
    for key, value in telemetry.items():
        print(f"  {key}: {value}")

    drone.close()


if __name__ == '__main__':
    main()

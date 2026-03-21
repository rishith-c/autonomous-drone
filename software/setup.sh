#!/bin/bash
# Raspberry Pi setup script for the Autonomous Drone project.
# Run this on a fresh Raspberry Pi OS Lite installation.
#
# Usage:
#   chmod +x setup.sh
#   ./setup.sh

set -e

echo "=== Autonomous Drone - Raspberry Pi Setup ==="
echo ""

# --- System update ---
echo "[1/5] Updating system packages..."
sudo apt update && sudo apt upgrade -y

# --- Python dependencies ---
echo "[2/5] Installing Python and build tools..."
sudo apt install -y python3-pip python3-dev build-essential

# --- Python packages ---
echo "[3/5] Installing Python packages (DroneKit, MAVProxy, pymavlink)..."
pip3 install --break-system-packages dronekit dronekit-sitl mavproxy pymavlink numpy

# --- Enable UART ---
echo "[4/5] Enabling UART..."

# Add enable_uart=1 to /boot/config.txt if not already present
if ! grep -q "^enable_uart=1" /boot/config.txt 2>/dev/null; then
    echo "enable_uart=1" | sudo tee -a /boot/config.txt > /dev/null
    echo "  Added enable_uart=1 to /boot/config.txt"
else
    echo "  UART already enabled in /boot/config.txt"
fi

# Disable serial console on ttyAMA0 (conflicts with UART use)
sudo systemctl stop serial-getty@ttyAMA0.service 2>/dev/null || true
sudo systemctl disable serial-getty@ttyAMA0.service 2>/dev/null || true

echo "[5/5] Setup complete."
echo ""
echo "IMPORTANT: You still need to disable the serial login shell via raspi-config:"
echo "  sudo raspi-config"
echo "  -> Interface Options -> Serial Port"
echo "  -> Login shell over serial: No"
echo "  -> Serial port hardware enabled: Yes"
echo ""
echo "Then reboot:"
echo "  sudo reboot"
echo ""
echo "After reboot, test the connection:"
echo "  python3 software/drone_controller.py"

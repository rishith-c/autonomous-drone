# Troubleshooting

Common problems, their causes, and how to fix them.

---

## FC Not Connecting to Computer

**Symptoms:** No communication via USB, device not detected.

**Causes:** Bad cable, driver issues, wrong COM port.

**Fixes:**
- Try a different USB cable (must be a data cable, not charge-only)
- Install or update USB drivers (STM32 VCP driver)
- Try a different USB port
- Check device manager (Windows) or `ls /dev/tty*` (Mac/Linux)
- Hold the BOOT button while plugging in USB to enter bootloader mode

---

## Motors Not Spinning

**Symptoms:** Quad arms successfully but motors do not spin.

**Causes:** ESC protocol mismatch, wiring issue, ESC not calibrated.

**Fixes:**
- Verify `MOT_PWM_TYPE = 6` (Dshot600) matches your ESC capability
- Check motor signal wires are connected to the correct FC motor output pads
- Test each motor individually using the ground station motor test
- Confirm the ESC is receiving battery power (check with multimeter)
- If using PWM instead of Dshot, run ESC calibration

---

## GPS No Fix

**Symptoms:** GPS status stuck on "No Fix" or "No GPS".

**Causes:** Indoors, blocked sky view, wiring error, wrong parameters.

**Fixes:**
- Go outside with clear sky view (first lock takes up to 3 minutes)
- Check GPS wiring: White (TX) must go to FC RX3, Green (RX) to FC TX3
- Verify parameters: `GPS_TYPE = 1`, `SERIAL3_PROTOCOL = 5`, `SERIAL3_BAUD = 115`
- Check GPS LED -- should blink when powered, solid when locked
- Ensure GPS has 5V power (red wire to 5V pad)

---

## Compass Not Healthy

**Symptoms:** "Compass not healthy" pre-arm error.

**Causes:** Not calibrated, magnetic interference, wrong configuration.

**Fixes:**
- Run compass calibration outdoors, away from metal
- Move GPS module further from power wires (use 10cm mast)
- Check `COMPASS_EXTERNAL = 1` if using the GPS-integrated compass
- Verify SDA and SCL wires are connected to the FC I2C pads
- Check for magnetic interference sources (motors, battery, metal frame parts)
- Compass offsets should be under 600 after calibration

---

## Quad Flips on Takeoff

**Symptoms:** Flips immediately when throttle is raised.

**Causes:** Wrong motor rotation, wrong motor order, wrong prop direction.

**Fixes:**
- Verify motor layout matches Quad X configuration:
  - M1 (front right): CW
  - M2 (rear left): CW
  - M3 (front left): CCW
  - M4 (rear right): CCW
- Test each motor individually (props off) and verify direction
- Swap any 2 of a motor's 3 phase wires to reverse its direction
- Verify CW props are on CW motors and CCW props are on CCW motors
- Confirm `FRAME_CLASS = 1` and `FRAME_TYPE = 1`

---

## Quad Drifts in GPS Mode

**Symptoms:** Does not hold position, drifts away in Loiter mode.

**Causes:** Poor GPS accuracy, bad compass calibration, high HDOP.

**Fixes:**
- Wait for more satellites (need 8+ for good hold)
- Check HDOP is below 2.0
- Recalibrate compass outdoors
- Verify GPS is mounted with arrow forward, on a mast above electronics
- Check for magnetic interference
- Make sure the quad has been sitting still for a few minutes after GPS lock before switching to Loiter

---

## MAVLink Not Connecting from Raspberry Pi

**Symptoms:** Python script times out or cannot connect to FC.

**Causes:** Wrong baud rate, wrong port, no common ground, UART not enabled.

**Fixes:**
- Check wiring: RPi TX (GPIO 14) to FC RX2, RPi RX (GPIO 15) to FC TX2
- Confirm common ground wire between RPi and FC
- Match baud rates: `SERIAL2_BAUD = 921` on FC and `baud=921600` in Python
- Verify `/dev/ttyAMA0` exists: `ls -la /dev/ttyAMA0`
- Ensure UART is enabled: `enable_uart=1` in `/boot/config.txt`
- Ensure serial console is disabled via `raspi-config`
- Check `SERIAL2_PROTOCOL = 2` (MAVLink2) on the FC
- Try lower baud rate (57600) if 921600 is unreliable

---

## Battery Voltage Warning with Full Battery

**Symptoms:** Low voltage alarm even when battery is fully charged.

**Causes:** Battery monitoring not configured or misconfigured.

**Fixes:**
- Set `BATT_CAPACITY = 3000`
- Set `BATT_MONITOR = 4` (Analog Voltage and Current)
- Set `BATT_VOLT_PIN = 10` and `BATT_CURR_PIN = 11` (Matek F405-Wing V2 specific)
- Adjust `BATT_VOLT_MULT` until the ground station voltage matches a multimeter reading on the battery
- Set `BATT_AMP_PERVLT = 66.7` (per Matek spec)
- Verify battery is actually fully charged: 16.8V for 4S

---

## High Vibrations in Flight Logs

**Symptoms:** Accelerometer readings show values above 30 in logs, unstable flight.

**Causes:** Poor FC mounting, unbalanced props, loose components.

**Fixes:**
- Mount FC on anti-vibration dampeners (soft foam or silicone grommets)
- Balance propellers (use a prop balancer or check for visible damage)
- Tighten all motor mounting screws
- Ensure nothing is resting against the FC that could transmit vibration
- Check that props are not warped or cracked

---

## Quad Won't Arm

**Symptoms:** Arming command is rejected, pre-arm check fails.

**Causes:** One or more safety checks not passing.

**Fixes:**
- Read the specific pre-arm failure message in the ground station
- Common failures and fixes:

| Message | Fix |
|---------|-----|
| "Compass not calibrated" | Calibrate compass outdoors |
| "Accelerometer not calibrated" | Run 6-position accel cal |
| "GPS no fix" | Go outside, wait for lock |
| "Battery failsafe" | Check voltage and BATT params |
| "RC not calibrated" | Calibrate RC or adjust ARMING_CHECK |
| "Gyro cal failed" | Keep quad still during startup |
| "Barometer not healthy" | Check for airflow over baro sensor, reboot FC |

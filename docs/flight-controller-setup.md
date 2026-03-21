# Flight Controller Setup

Configuration guide for the Matek F405-Wing V2 running ArduCopter V4.6.3.

---

## Flashing Firmware

1. Download [QGroundControl](http://qgroundcontrol.com/) (Mac/Linux) or [Mission Planner](https://ardupilot.org/planner/) (Windows)
2. Connect the FC via USB
3. Select board: **MatekF405-Wing**
4. Select firmware: **ArduCopter V4.6.3** (latest stable)
5. Flash and wait for reboot
6. If the FC is not detected, hold the BOOT button while plugging in USB

---

## Parameter Configuration

All parameters can be loaded at once from `config/arducopter-params.param`, or set individually below.

### Frame Type

```
FRAME_CLASS = 1    (MultiCopter)
FRAME_TYPE  = 1    (Quad X)
```

### ESC Protocol

```
MOT_PWM_TYPE = 6   (Dshot600)
```

### GPS

```
GPS_TYPE        = 1     (AUTO detect, or 2 for explicit uBlox)
SERIAL3_PROTOCOL = 5    (GPS)
SERIAL3_BAUD    = 115   (115200 baud)
```

### Compass

```
COMPASS_ENABLE    = 1
COMPASS_EXTERNAL  = 1   (using GPS-integrated compass)
COMPASS_AUTO_ROT  = 1   (auto-detect compass orientation)
```

### MAVLink (Raspberry Pi on UART2)

```
SERIAL2_PROTOCOL = 2    (MAVLink2)
SERIAL2_BAUD     = 921  (921600 baud)
```

If 921600 causes issues, try 57600:
```
SERIAL2_BAUD = 57       (57600 baud)
```

### Battery Monitoring

```
BATT_MONITOR    = 4      (Analog Voltage and Current)
BATT_VOLT_PIN   = 10
BATT_CURR_PIN   = 11
BATT_VOLT_MULT  = (check Matek F405-Wing V2 docs for exact value)
BATT_AMP_PERVLT = 66.7   (per Matek F405-Wing V2 spec)
BATT_CAPACITY   = 3000   (mAh)
```

### Failsafes

```
BATT_LOW_VOLT    = 14.0   (3.5V per cell -- triggers low battery action)
BATT_CRT_VOLT    = 13.2   (3.3V per cell -- triggers critical action)
BATT_FS_LOW_ACT  = 2      (RTL on low battery)
BATT_FS_CRT_ACT  = 1      (Land immediately on critical battery)
FS_THR_ENABLE    = 1      (RC failsafe enabled)
```

---

## Sensor Health Check

After setting parameters, reboot the FC and verify in the ground station:

- **Accelerometer:** Should show "Healthy"
- **Gyroscope:** Should show "Healthy"
- **Barometer:** Should show "Healthy" with reasonable altitude reading
- **Compass:** Should show "Healthy" (may need calibration first)
- **GPS:** Will show "No Fix" indoors -- take outside to verify

If any sensor shows unhealthy, check wiring and re-flash firmware.

---

## Arming Checks

ArduCopter will refuse to arm if safety checks fail. Common pre-arm failures:

| Error | Fix |
|-------|-----|
| "Compass not calibrated" | Run compass calibration outdoors |
| "Accelerometer not calibrated" | Run 6-position accel calibration |
| "GPS not detected" | Check GPS wiring (TX/RX crossover) |
| "Battery failsafe" | Check battery voltage and BATT parameters |
| "RC not calibrated" | Calibrate RC or disable RC checks if using RPi only |

If flying without an RC transmitter (RPi only), you may need to adjust arming checks:
```
ARMING_CHECK = 1    (all checks enabled -- recommended)
```

Only disable specific checks if you understand the implications.

---

## PID Tuning

Default PID values usually work for a first flight. If you notice issues:

| Symptom | Adjustment |
|---------|------------|
| Oscillations / wobble | Reduce P gain |
| Slow or sluggish response | Increase P gain |
| Drifts after stopping | Increase I gain |
| Overshoots on fast moves | Increase D gain |

Start with the defaults and only tune after analyzing flight logs. ArduCopter's autotune mode can also help -- switch to AUTOTUNE mode during a calm flight and let it optimize.

---

## Verifying Motor Output

Before first flight, use the ground station motor test:

1. Remove all propellers
2. Connect battery
3. In ground station, go to Motor Test
4. Spin each motor individually at 5-10% throttle
5. Verify:
   - M1 (front right) spins CW
   - M2 (rear left) spins CW
   - M3 (front left) spins CCW
   - M4 (rear right) spins CCW
6. If wrong direction: swap 2 of the 3 motor phase wires

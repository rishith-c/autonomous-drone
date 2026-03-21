# Calibration Guide

Sensor calibration procedures for the Matek F405-Wing V2 flight controller.

All calibrations are done through a ground station (QGroundControl or Mission Planner) with the FC connected via USB.

---

## 1. Accelerometer Calibration

The accelerometer measures the quad's orientation relative to gravity. This calibration is required before first flight.

### Procedure

1. Connect FC to ground station via USB
2. Navigate to sensor calibration section
3. Place the FC (or fully assembled quad) in 6 orientations, holding steady for each:
   - **Level** (right-side up, flat on table)
   - **Left side down**
   - **Right side down**
   - **Nose down**
   - **Nose up**
   - **Upside down**
4. Hold each position steady until the ground station confirms that orientation
5. Wait for "Calibration Complete" message

### Tips

- Do this with the FC mounted on the frame in its final position
- The surface must be flat and level
- Hold still for at least 5 seconds per orientation
- If calibration fails, retry on a more level surface

---

## 2. Compass Calibration

The compass (magnetometer) determines heading. It is very sensitive to magnetic interference.

### Procedure

1. Take the quad **outside**, away from:
   - Buildings with rebar
   - Cars
   - Metal fences
   - Power lines
   - Any large metal objects
2. Start compass calibration in the ground station
3. Rotate the quad slowly in all orientations:
   - Rotate 360 degrees while level
   - Rotate 360 degrees while nose-down
   - Rotate 360 degrees while on its side
   - Basically, cover as many orientations as possible -- figure-8 patterns work well
4. Continue until progress bars fill and calibration completes
5. The ground station will report compass offsets -- these should be under 600

### Tips

- Must be done outdoors
- Remove any magnets or metal near the GPS/compass module
- GPS should be on a 10cm mast above the electronics
- If calibration keeps failing, there may be too much magnetic interference from the ESC or power wires
- Recalibrate if you change GPS mounting position

### Relevant Parameters

```
COMPASS_ENABLE   = 1
COMPASS_EXTERNAL = 1    (GPS-integrated compass)
COMPASS_AUTO_ROT = 1    (auto-detect orientation)
```

---

## 3. ESC Calibration

Sets the throttle range so all motors respond identically to the same throttle input.

**With Dshot600, traditional ESC calibration is usually not needed** -- Dshot is a digital protocol with no analog drift. However, if using PWM instead, follow this procedure:

### PWM ESC Calibration Procedure

1. **Remove all propellers**
2. Power off the quad
3. In the ground station, navigate to ESC calibration
4. Follow the on-screen instructions (typically: set throttle high, power on, wait for tones, set throttle low, wait for confirmation tones)
5. Test each motor individually at low throttle to verify uniform response

### Dshot Verification

If using Dshot600 (recommended), just verify:
```
MOT_PWM_TYPE = 6    (Dshot600)
```

Then use the motor test in the ground station to confirm all 4 motors spin at the same speed for the same commanded value.

---

## 4. Radio Calibration (if using RC transmitter)

If you have an RC transmitter/receiver for manual backup control:

1. Connect RC receiver to FC (SBUS or PPM on appropriate UART)
2. Turn on the transmitter
3. In the ground station, go to radio calibration
4. Move all sticks to their full extremes (up, down, left, right)
5. Move all switches through their positions
6. The ground station records min/max values for each channel
7. Save calibration
8. Set failsafe: when the transmitter is off, the receiver should output a specific low throttle value that triggers the FC failsafe

---

## 5. Level Calibration (Board Level Horizon)

If the artificial horizon in the ground station doesn't show level when the quad is sitting flat:

1. Place the quad on a known-level surface
2. In ground station, run "Calibrate Level" or "Level Horizon"
3. This sets the current orientation as "level"

---

## Post-Calibration Verification

After all calibrations, check in the ground station:

| Sensor | Expected Status |
|--------|----------------|
| Accelerometer | Healthy, level reads ~0 degrees pitch/roll |
| Gyroscope | Healthy, reads ~0 when stationary |
| Barometer | Healthy, shows reasonable altitude |
| Compass | Healthy, heading matches real-world direction |
| GPS | No Fix indoors (take outside to verify lock) |
| Battery | Shows correct voltage when connected |

If any sensor still shows unhealthy after calibration, check wiring and redo the calibration.

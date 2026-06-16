# Hardware Specifications

Detailed specifications for every component in the build.

---

## Flight Controller: Matek F405-Wing V2

| Spec | Value |
|------|-------|
| Processor | STM32 F405 (32-bit ARM Cortex-M4, 168MHz) |
| IMU | ICM-42688-P (6-axis gyroscope/accelerometer) |
| Barometer | DPS310 (altitude sensing) |
| Flash | 16MB onboard (flight logging) |
| UART Ports | 6x serial ports |
| I2C Buses | 2x |
| PWM Outputs | 10 (using 4 for quadcopter) |
| Voltage Input | 2-6S (7.4V - 25.2V) |
| Weight | ~10g |
| Firmware | ArduCopter V4.6.3 |
| Mounting | 30x30mm hole pattern |
| Cost | $35-45 |

Key features: built-in voltage/current sensor, microSD slot for logging, multiple UART ports for GPS and companion computer.

---

## ESC: Diatone Mamba F40 4-in-1

| Spec | Value |
|------|-------|
| Continuous Rating | 40A per motor |
| Burst Rating | 50A per motor |
| Total Continuous | 160A |
| Voltage Range | 3-6S |
| Protocol | Dshot600 |
| Firmware | BLHeli_32 or BLHeli_S |
| Mounting | 30x30mm |
| Weight | ~40g |
| Cost | $35-45 |

Dshot600 is a digital protocol -- no PWM calibration drift, no analog noise.

---

## Motors: D2830-12 Brushless Outrunner (x4)

| Spec | Value |
|------|-------|
| KV Rating | ~1000-1200 |
| Max Thrust | 875g per motor |
| Total Thrust (4x) | 3500g |
| Max Power | 187W per motor |
| Voltage | 3-4S compatible |
| Shaft Diameter | 5mm |
| Mount Pattern | Standard X-pattern |
| Weight | ~60g each |
| Recommended Props | 10-12 inch |
| Cost | $10-15 each |

At 1850g all-up weight with 3500g max thrust, the thrust-to-weight ratio is 1.89:1.

---

## Battery: 4S LiPo

| Spec | Value |
|------|-------|
| Chemistry | Lithium Polymer (LiPo) |
| Configuration | 4S1P (4 cells in series) |
| Capacity | 3000mAh |
| Nominal Voltage | 14.8V |
| Full Charge | 16.8V (4.2V per cell) |
| Low Voltage Cutoff | 14.0V (3.5V per cell) |
| Critical Voltage | 13.2V (3.3V per cell) |
| Discharge Rate | 60C (180A continuous max) |
| Connector | XT60 |
| Weight | ~350g |
| Dimensions | ~105 x 35 x 28mm |
| Cost | $25-35 |

Storage voltage: 3.8V per cell (15.2V total). Never discharge below 3.0V per cell.

---

## Propellers: 11x7

| Spec | Value |
|------|-------|
| Diameter | 11 inches |
| Pitch | 7 inches |
| Material | Reinforced plastic |
| Configuration | 2x CW + 2x CCW per set |
| Shaft Adapter | 5mm |
| Weight | ~18g each |
| Cost | $10-15 for 2 sets (8 props) |

Always buy spare props. Replace after any crash or visible damage.

---

## GPS Module: Beitian BN-880

| Spec | Value |
|------|-------|
| GPS Chip | Ublox M8N |
| Satellite Systems | GPS + GLONASS (dual constellation) |
| Update Rate | 5Hz |
| Accuracy | 2.5m CEP |
| Cold Start | ~26 seconds |
| Hot Start | ~1 second |
| Compass | HMC5883L or QMC5883L (3-axis magnetometer) |
| Antenna | External ceramic patch (on cable) |
| LED | GPS lock status indicator |
| Connection | 6-wire (VCC, GND, TX, RX, SDA, SCL) |
| Voltage | 3.3-5V |
| Weight | ~12g |
| Cost | $15-25 |

Mount on a mast 10cm above electronics. Arrow points forward.

---

## Companion Computer: Raspberry Pi 4 Model B

| Spec | Value |
|------|-------|
| Processor | Quad-core ARM Cortex-A72 @ 1.5GHz |
| RAM | 2GB or 4GB (4GB recommended) |
| Connectivity | WiFi, Bluetooth, Ethernet, USB |
| GPIO | 40-pin header (UART on GPIO 14/15) |
| Storage | 32GB microSD (Class 10) |
| Power | 5V 3A via USB-C or GPIO |
| OS | Raspberry Pi OS Lite (headless) |
| Weight | ~46g (without case) |
| Cost | $35-55 |

Powered separately from the FC -- use a USB power bank or dedicated 5V BEC. Shares common ground with FC for UART communication.

---

## Frame

| Spec | Value |
|------|-------|
| Type | Custom carbon fiber rod |
| Rod Material | Carbon fiber tubes (18mm diameter) |
| Rod Count | 10x at 300mm length |
| Motor Spacing | 450mm diagonal |
| Center Plate | Acrylic or carbon fiber (200x200mm) |
| Motor Mounts | 18mm rod clamps or 3D-printed adapters |
| GPS Mast | 10cm standoff |
| Frame Weight | ~200-250g |
| Cost | $40-90 |

See [Frame Assembly](../hardware/frame/frame-assembly.md) for build instructions.

![Four carbon-fiber arms with yellow 3D-printed motor mounts and brushless motors installed.](assets/build-progress/arm-motor-assemblies.jpg)

**Current motor-mount build:** yellow 3D-printed adapters clamp the motors to the 18mm carbon-fiber arms. Verify screw tightness and motor shaft clearance before installing propellers.

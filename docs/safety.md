# Safety Guidelines

Quadcopters with spinning propellers are dangerous. Follow these protocols at all times.

---

## Pre-Flight Safety Checklist

Run through this before every flight:

- [ ] Props installed correctly (CW/CCW matched to motors)
- [ ] All screws tight (motors, FC, frame)
- [ ] Battery fully charged (16.8V for 4S)
- [ ] Battery securely mounted (velcro strap tight)
- [ ] No loose wires anywhere
- [ ] No wires near propeller paths
- [ ] GPS has 3D fix with 8+ satellites
- [ ] All sensors show healthy in ground station
- [ ] Compass calibrated recently
- [ ] Failsafes configured and tested
- [ ] Flight area clear of people and obstacles (30m minimum)
- [ ] Weather acceptable (no rain, wind under 10 mph)
- [ ] Emergency procedures reviewed

---

## During Flight

- Always maintain line of sight with the quad
- Have an RC transmitter as backup control if possible
- Monitor battery voltage constantly -- land when it hits 14.0V (3.5V/cell)
- Land with at least 20% battery remaining
- If anything seems wrong, land immediately
- Never fly over people or someone else's property
- Respect no-fly zones and local regulations
- Stay below 120m / 400ft altitude (FAA limit in the US)

---

## Emergency Procedures

### Loss of GPS

- Switch to Stabilize mode (manual control)
- Land immediately at current position
- Do not attempt GPS-dependent modes (Loiter, Auto, RTL) without GPS

### Low Battery

- If failsafe is configured, RTL will activate automatically at 14.0V
- If in manual control, land immediately where you are
- Do not try to fly back if battery is critical (13.2V)
- A crash landing nearby is better than a dead-battery crash far away

### Loss of Control

- If using RC: attempt to switch to a stable flight mode (Stabilize, Loiter)
- If using RPi: send RTL command or kill switch
- Last resort: cut power (will crash, but prevents a flyaway)
- A controlled crash is always better than an uncontrolled flyaway

### Flyaway

- Immediately attempt RTL command
- If no response, cut power
- Note the last known GPS position for recovery
- Report the incident and investigate root cause before flying again

---

## Battery Safety

LiPo batteries are a fire risk if mishandled.

- **Never leave a LiPo charging unattended**
- Always use a LiPo-compatible balance charger
- Charge on a fireproof surface inside a LiPo charging bag
- Store batteries at 3.8V per cell (15.2V for 4S) -- not full and not empty
- Never discharge below 3.0V per cell
- Never puncture, crush, or short-circuit a LiPo
- If a battery is puffed (swollen), stop using it immediately
- Dispose of damaged batteries at a battery recycling center -- do not throw in trash
- Keep a fire extinguisher (Class D or sand) nearby when charging

---

## Workspace Safety

When soldering and assembling:

- Wear safety glasses
- Work in a ventilated area (solder fumes)
- Use a temperature-controlled soldering iron
- Carbon fiber dust is harmful -- wear a mask when cutting or sanding CF rods
- Keep the work area clean and organized

---

## Legal Considerations

Depending on your location, you may need to:

- Register the drone with aviation authorities (FAA in the US if over 250g)
- Obtain a Remote Pilot Certificate for commercial use
- Follow local airspace restrictions
- Maintain visual line of sight
- Not fly over people or moving vehicles
- Stay below altitude limits

Check your local regulations before flying. This quad at 1.85kg is above the 250g registration threshold in most jurisdictions.

---

## Maintenance for Safety

| Frequency | Check |
|-----------|-------|
| Every flight | Props for cracks, screws tight, wires secure |
| Weekly | Motor bearings spin freely, frame integrity |
| Monthly | Compass recalibration, deep clean, connector inspection |
| Quarterly | Replace props, check motor condition, battery health |

Replace any component that shows wear, damage, or degraded performance. A $10 prop is not worth a crash.

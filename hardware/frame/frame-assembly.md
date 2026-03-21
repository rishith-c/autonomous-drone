# Frame Assembly

## Overview

Custom carbon fiber rod frame with 450mm diagonal motor spacing. Uses 10x 18mm diameter carbon fiber rods at 300mm length each, joined at a center plate.

## Materials

- 10x carbon fiber rods (18mm diameter, 300mm length)
- 1x center plate (acrylic or carbon fiber, 200x200mm)
- Motor clamps or 3D-printed adapters for 18mm rods
- M3 screws and nuts for FC/ESC mounting
- Landing gear legs (carbon fiber rods or 3D-printed)

## Frame Layout (Top View)

```
        FRONT
         |
    Rod  Rod
      \  |  /
   Rod--[Plate]--Rod
      /  |  \
    Rod  Rod
         |
        REAR

4 arms extending from center plate at 90-degree intervals
Plus vertical rods or landing gear underneath
```

## Assembly Steps

### Step 1: Prepare Carbon Fiber Rods

1. Cut all 10 rods to exactly 300mm (or buy pre-cut)
2. Sand both ends smooth -- carbon fiber splinters are dangerous, wear gloves and a mask
3. Inspect each rod for cracks or delamination
4. Wipe clean with isopropyl alcohol

### Step 2: Prepare Center Plate

1. Cut center plate to 200x200mm
2. Drill FC mounting holes in 30x30mm pattern (center of plate)
3. Drill rod mounting holes at 45-degree angles from center, matching arm positions
4. Sand all edges smooth
5. Test-fit the FC stack (FC + ESC) on the mounting holes

### Step 3: Assemble Arms

1. Insert 4 rods through center plate holes at 90-degree intervals
2. Each arm extends equally on both sides of center plate
3. Secure rods with epoxy or compression clamps at the center plate
4. Verify 450mm diagonal distance (motor mount to motor mount)
5. Check all arms are level and symmetrical

### Step 4: Mount Motors

1. Attach motor clamps or 3D-printed adapters to the end of each arm
2. Bolt each motor to its mount with the included screws
3. Motors should be perpendicular to the arms (shaft pointing up)
4. Tighten all motor mounting screws -- these take a lot of vibration
5. Verify motor spacing is 450mm diagonal

Motor positions:
```
        FRONT
    M3 (CCW)    M1 (CW)
        \          /
         [CENTER]
        /          \
    M2 (CW)     M4 (CCW)
```

### Step 5: Install Landing Gear

1. Attach 4 landing legs to the bottom of the center plate or arm junctions
2. Legs should provide 5-8cm ground clearance under the center plate
3. Add rubber or foam padding to leg tips to absorb landing impact
4. Test stability on a flat surface -- quad should not tip over

### Step 6: Mount Electronics Stack

1. Place anti-vibration dampeners on the FC mounting holes
2. Mount the ESC first (bottom of stack) with standoffs
3. Mount the FC on top of the ESC using M3 screws through vibration dampeners
4. The FC arrow should point toward the front of the quad
5. Ensure nothing is touching the FC that could transmit vibrations

### Step 7: Mount GPS on Mast

1. Attach a 10cm standoff or mast to the top of the center plate
2. Mount the BN-880 GPS module on top of the mast
3. The GPS arrow must point forward (same direction as FC arrow)
4. Route GPS wires down the mast and along the frame, away from power wires
5. Secure with zip ties

### Step 8: Mount Raspberry Pi

1. Secure RPi to the frame using standoffs or velcro
2. Position away from propeller wash path if possible
3. Ensure USB-C power port is accessible
4. Route UART wires to the FC
5. Leave GPIO header accessible for future expansion

### Step 9: Battery Mounting

1. Velcro strap attachment point on the bottom or center of frame
2. Battery slides in and secures with velcro strap
3. Position battery so center of gravity is near geometric center of frame
4. Test balance by hanging frame from a string at center -- should be roughly level
5. Adjust battery position as needed

### Step 10: Cable Management

1. Route all motor wires along the arms, secured with zip ties every 5-8cm
2. Keep signal wires away from power wires where possible
3. Ensure no wires can contact propellers at any angle
4. Leave a small amount of slack in all wires for vibration absorption
5. Use heat shrink at any point where wires cross frame edges

## Balance Check

After full assembly:
1. Hang the completed quad from a string at the center point
2. It should hang roughly level in all directions
3. If it tilts, move the battery or other heavy components to compensate
4. The center of gravity should be as close to the geometric center as possible

## Weight Budget

| Component | Weight |
|-----------|--------|
| Frame (rods + plate + hardware) | ~200-250g |
| Motors (4x 60g) | ~240g |
| ESC | ~40g |
| Flight Controller | ~10g |
| GPS Module | ~12g |
| Raspberry Pi 4 | ~46g |
| Battery (3000mAh 4S) | ~350g |
| Props (4x 18g) | ~72g |
| Wiring, connectors, misc | ~80-100g |
| **Total** | **~1050-1120g (aim for under 1850g all-up)** |

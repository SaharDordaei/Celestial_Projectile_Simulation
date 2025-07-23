# celestial_projectile_simulation.py
# Author: Sahar Dordaei Joghan
# Date: April 2023
# Description:
#     Interactive simulation of projectile motion on different planets using VPython

# =================== MIT License ===================
# Copyright (c) 2023 Sahar Dordaei Joghan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to use, modify, distribute, and publish with attribution.
# ===================================================


# Web VPython 3.2

# =======================
# === INITIAL SCENE SETUP ===
# =======================

scene.width = 800                            # Width of 3D canvas
scene.height = 500                           # Height of 3D canvas
scene.background = color.black               # Black background
scene.forward = vector(-1, 0, 0)             # View from the side (negative x-axis)
scene.up = vector(0, 1, 0)                   # 'Up' direction is positive y-axis

# =======================
# === PLANET DEFINITIONS ===
# =======================

planet_names = ["Earth", "Moon", "Mercury", "Mars"]   # List of selectable planets

# Dictionary mapping each planet to its gravitational acceleration (in m/s²)
gravities = {
    "Earth": 9.8,
    "Moon": 1.62,
    "Mercury": 3.7,
    "Mars": 3.71
}

# Approximate surface colors to visually distinguish each planet's ground
planet_colors = {
    "Earth": color.green,
    "Moon": color.gray(0.5),
    "Mercury": color.gray(0.3),
    "Mars": vector(1, 0.4, 0.2)  # reddish
}

# =======================
# === USER INTERFACE TEXT OUTPUT ===
# =======================

info_label = wtext("")         # Label to show current gravity
distance_label = wtext("")     # Label to show final distance
scene.append_to_caption("\n\n")

# Dummy function for sliders that don't update live (only read on button click)
def dummy(s): pass

# =======================
# === SLIDERS AND MENU ===
# =======================

# Initial velocity slider
scene.append_to_caption("Initial Velocity (m/s):\n")
vel_slider = slider(min=5, max=50, value=24, step=1, length=300, bind=dummy)
scene.append_to_caption("\n\n")

# Mass slider
scene.append_to_caption("Mass (kg):\n")
mass_slider = slider(min=0.1, max=10, value=1, step=0.1, length=300, bind=dummy)
scene.append_to_caption("\n\n")

# Friction (energy loss on bounce) slider
scene.append_to_caption("Friction (0–0.2):\n")
friction_slider = slider(min=0, max=0.2, value=0.01, step=0.01, length=300, bind=dummy)
scene.append_to_caption("\n\n")

# Volume slider — affects ball size and mass indirectly
scene.append_to_caption("Volume (m³):\n")
volume_slider = slider(min=0.1, max=5, value=1, step=0.1, length=300, bind=dummy)
scene.append_to_caption("\n\n")

# Launch angle slider (in degrees)
scene.append_to_caption("Launch Angle (degrees):\n")
angle_slider = slider(min=10, max=80, value=45, step=1, length=300, bind=dummy)
scene.append_to_caption("\n\n")

# Planet selection menu
scene.append_to_caption("Choose Planet:\n")
def planet_changed(m):
    planet = planet_names[planet_menu.index]
    # Update gravity label when planet changes
    info_label.text = "<b>Gravity:</b> " + str(gravities[planet]) + " m/s²<br>"

planet_menu = menu(choices=planet_names, index=0, bind=planet_changed)
planet_changed(None)  # Initialize label
scene.append_to_caption("\n\n")

# =======================
# === SIMULATION FUNCTION ===
# =======================

def simulate():
    # Clear all objects from previous simulation
    for obj in scene.objects:
        obj.visible = False
    distance_label.text = ""

    # Get user inputs
    v0 = vel_slider.value
    m = mass_slider.value
    friction = friction_slider.value
    volume = volume_slider.value
    angle = angle_slider.value
    planet = planet_names[planet_menu.index]
    g = gravities[planet]

    # Convert launch angle to radians and compute velocity components
    theta = radians(angle)
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)

    # Compute ball radius from volume (assuming sphere): V = 4/3 π r³ → r = (3V / 4π)^(1/3)
    radius = (3 * volume / (4 * pi)) ** (1.0/3.0)

    # Estimate range to determine how long the ground should be
    est_range = (v0**2 * sin(2*theta)) / g
    ground_length = max(100, est_range * 1.5)

    # Create ground and ball objects
    ground = box(pos=vector(ground_length/2, -radius, 0), size=vector(ground_length, 0.5, 4), color=planet_colors[planet])
    ball = sphere(pos=vector(0, 0, 0), radius=radius, color=color.orange, make_trail=True)

    # Set camera position and angle (side view)
    scene.camera.pos = vector(0, 5, 50)
    scene.camera.axis = vector(0, -5, -50)
    scene.center = vector(ground_length / 4, 2, 0)

    # Initialize position and velocity variables
    x = 0
    y = 0
    vx_now = vx
    vy_now = vy
    dt = 0.01  # Time step

    # ===== SIMULATION LOOP =====
    while True:
        rate(100)  # Run 100 frames per second

        # Update positions based on velocity
        x += vx_now * dt
        y += vy_now * dt

        # If ball hits ground, stop vertical and horizontal motion
        if y <= 0 and vy_now < 0:
            y = 0
            vy_now = 0
            vx_now = 0
        else:
            vy_now -= g * dt  # Apply gravity

        # Update ball position
        ball.pos = vector(x, y, 0)

        # Move camera slightly to follow the ball
        scene.center = vector(ball.pos.x + 10, 2, 0)

        # Stop simulation when ball comes to rest
        if y <= 0.01 and abs(vx_now) < 0.05 and abs(vy_now) < 0.05:
            break

    # Output total horizontal distance traveled
    distance_label.text = "<b>Total Distance:</b> {:.2f} meters".format(x)

# =======================
# === BUTTON TO START SIMULATION ===
# =======================

def clicked_start():
    simulate()

# Button that runs the simulation
button(text="▶ Start Simulation", bind=clicked_start)

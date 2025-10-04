# Celestial Projectile Motion Simulator

A VPython simulation to visualize **projectile motion** on different planetary bodies. This project models how launch parameters and gravitational differences affect a projectile's range and trajectory, with interactive controls for physics variables.

---

## What It Does

- Simulates projectile motion under varying gravity (Earth, Moon, Mercury, Mars).
- Includes adjustable sliders for:
  - **Initial velocity**
  - **Mass**
  - **Volume**
  - **Friction**
  - **Launch angle**
- Planet selection via dropdown menu with **real gravitational values**.
- Animates motion in real time with trail, dynamic camera, and accurate physics.
- Calculates and displays **total horizontal distance** traveled.

---

## Files Included

| File                            | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| `projectile_simulation.py`      | Full simulation code written in GlowScript VPython             |
| `README.md`                     | Project description, features, and usage instructions          |
| `LICENSE`                       | MIT License                                                    |

---

## How to Run

1. **Via Trinket (Recommended)**  
   Paste the code into [https://trinket.io/glowscript](https://trinket.io/glowscript) and run directly in your browser.

2. **Using Web VPython Locally**  
   Install a local VPython environment (e.g. via `glowscript` or `vpython` packages) and run with a Web-compatible interface.

---

## Scientific Notes

- The **trajectory** is modeled using standard Newtonian mechanics with simplified air resistance (via an energy-loss **friction coefficient**).
- Volume is converted into radius assuming a **spherical projectile**, using the formula:  
  \[
  r = \left(\frac{3V}{4\pi}\right)^{1/3}
  \]
- Planetary gravities used:
  - Earth: 9.80 m/s²
  - Moon: 1.62 m/s²
  - Mercury: 3.70 m/s²
  - Mars: 3.71 m/s²
- On low-gravity planets like the Moon, the projectile travels significantly farther under identical launch conditions.

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with attribution.

---

## Author

**Sahar Dordaei Joghan**   
Created: April 2023  
Updated: July 2025 (for GitHub Portfolio)

---

## Acknowledgments

- [Trinket.io](https://trinket.io/) for providing an interactive VPython environment.
- VPython team and GlowScript developers for their educational visualization tools.


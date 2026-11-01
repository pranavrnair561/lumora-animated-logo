# Lumora 3D Logo Animation

A 3D version of the Lumora logo, animated as a 5-second video intro.
Lumora is a fictional rooftop solar and home battery startup.
Tagline: *Power that rises with you.*

**[▶ View the live 3D animation](https://pranavrnair561.github.io/lumora-animated-logo/)**

<!-- After you add a screenshot named lumora-3d-still.png to this repo, delete this line's comment markers:
![Lumora 3D logo](lumora-3d-still.png)
-->

## What it shows
- **Lighting:** warm key light, teal rim light, soft fill light and a glow from the sun, with metallic materials on a reflective floor.
- **Camera motion:** a slow orbit and push-in, with depth of field in Blender to keep focus on the logo.
- **Transitions:** the arc draws on, the sun pops in with a light flash, the base line wipes out from the centre, and the wordmark rises into place.

## Timeline (30 fps, 150 frames)
| Frames | Action |
|--------|--------|
| 1–45 | Arc draws on |
| 25–55 | Sun scales in with overshoot and flash |
| 45–70 | Base line wipes in |
| 70–105 | Wordmark reveal |
| 1–150 | Camera orbit and dolly |

## Files
- `lumora_logo_3d.py` – Blender script that builds the logo, lights, camera and animation
- `index.html` – browser version of the animation (three.js), opens by double-click or via GitHub Pages
- `lumora-logo-animated.svg` – animated 2D version of the logo

## How to render in Blender
1. Open Blender 4.x.
2. Go to the **Scripting** tab and click **Open**.
3. Choose `lumora_logo_3d.py` and click **Run Script**.
4. Press Space to preview, or **Render › Render Animation** (Ctrl+F12) to export an MP4.

## Brand colours
Night `#0E1B2C` · Sunrise `#FFB020` · Lagoon `#167373` · Dawn `#FFF7E8` · Mist `#E3EBF0`

## Tools
Blender 4.x, three.js, and Claude for design and code assistance.

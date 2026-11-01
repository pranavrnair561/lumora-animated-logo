# Lumora 3D Logo Animation

A 3D version of the Lumora logo, animated as a 5-second video intro.
Lumora is a fictional rooftop solar and home battery startup.
Tagline: *Power that rises with you.*

![Lumora 3D logo](lumora-3d-still.png)

## Video
[Watch the animation](YOUR-VIDEO-LINK)  
(Or open `lumora_intro.mp4` in this repo.)

## What it shows
- **Lighting:** warm key light, teal rim light, soft fill light, and a glow
  from the sun, with metallic materials on a reflective floor.
- **Camera motion:** a slow orbit and push-in, with depth of field to keep
  focus on the logo.
- **Transitions:** the arc draws on, the sun pops in with a light flash, the
  base line wipes out from the centre, and the wordmark rises into place.

## Timeline (30 fps, 150 frames)
| Frames | Action |
|--------|--------|
| 1–45 | Arc draws on |
| 25–55 | Sun scales in with overshoot and flash |
| 45–70 | Base line wipes in |
| 70–105 | Wordmark reveal |
| 1–150 | Camera orbit and dolly |

## How to use
1. Open Blender 4.x.
2. Go to the **Scripting** tab and click **Open**.
3. Choose `lumora_logo_3d.py` and click **Run Script**.
4. Press Space to preview, or **Render › Render Animation** to export an MP4.

## Files
- `lumora_logo_3d.py` – Blender script that builds the logo, lights, camera and animation
- `lumora_intro.mp4` – rendered animation
- `lumora-3d-still.png` – still frame

## Brand colours
Night `#0E1B2C` · Sunrise `#FFB020` · Lagoon `#167373` · Dawn `#FFF7E8` · Mist `#E3EBF0`

## Tools
Blender [version]. Built with the help of Claude.

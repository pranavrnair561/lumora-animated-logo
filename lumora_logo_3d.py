# Lumora 3D logo intro - Blender 4.x. Run: Scripting tab > Open > Run Script.
# Renders nothing automatically. Render: Render > Render Animation (Ctrl+F12).
import bpy, math
from math import pi, sin, cos

# ---------- clean scene ----------
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete()
sc = bpy.context.scene
sc.frame_start, sc.frame_end = 1, 150
sc.render.fps = 30
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
sc.render.filepath = "//lumora_intro.mp4"
sc.render.image_settings.file_format = 'FFMPEG'
sc.render.ffmpeg.format = 'MPEG4'; sc.render.ffmpeg.codec = 'H264'
for eng in ('BLENDER_EEVEE_NEXT', 'BLENDER_EEVEE'):
    try: sc.render.engine = eng; break
    except TypeError: pass
sc.world = bpy.data.worlds.new("W"); sc.world.use_nodes = True
bg = sc.world.node_tree.nodes["Background"]
bg.inputs[0].default_value = (0.02, 0.04, 0.07, 1); bg.inputs[1].default_value = 0.6

def mat(name, col, rough=0.25, metal=0.0, emit=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = col
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit:
        b.inputs["Emission Color"].default_value = col
        b.inputs["Emission Strength"].default_value = emit
    return m

SUN   = mat("Sunrise", (1.0, 0.45, 0.03, 1), 0.4, 0, 3.0)
CREAM = mat("Dawn",    (1.0, 0.90, 0.78, 1), 0.15, 0.9)
TEAL  = mat("Lagoon",  (0.02, 0.18, 0.18, 1), 0.2, 0.8)
FLOOR = mat("Floor",   (0.02, 0.04, 0.07, 1), 0.08, 0.6)

def key(obj, prop, frame, value, idx=None):
    if idx is None: setattr(obj, prop, value); obj.keyframe_insert(prop, frame=frame)
    else:
        v = list(getattr(obj, prop)); v[idx] = value; setattr(obj, prop, v)
        obj.keyframe_insert(prop, frame=frame)

# ---------- logo geometry (mark is built in the X/Z plane, facing the camera) ----------
# Arc: bevelled curve so it can "draw on" with bevel_factor_end
cu = bpy.data.curves.new("ArcCurve", 'CURVE'); cu.dimensions = '3D'
cu.bevel_depth = 0.25; cu.bevel_resolution = 10; cu.use_fill_caps = True
sp = cu.splines.new('POLY'); sp.points.add(40)
for i, p in enumerate(sp.points):
    a = pi - pi * i / 40
    p.co = (2.4 * cos(a), 0, 2.4 * sin(a), 1)
arc = bpy.data.objects.new("Arc", cu); sc.collection.objects.link(arc)
arc.data.materials.append(CREAM)

bpy.ops.mesh.primitive_uv_sphere_add(radius=1.4, location=(0, 0, 0.8), segments=64, ring_count=32)
sun = bpy.context.object; sun.name = "Sun"; sun.data.materials.append(SUN)
bpy.ops.object.shade_smooth()

bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -1.0))
base = bpy.context.object; base.name = "Base"; base.scale = (4, 0.5, 0.25)
bev = base.modifiers.new("Bevel", 'BEVEL'); bev.width = 0.1; bev.segments = 5
base.data.materials.append(TEAL)

bpy.ops.object.text_add(location=(0, 0, -2.7), rotation=(pi / 2, 0, 0))
txt = bpy.context.object; txt.name = "Wordmark"
txt.data.body = "Lumora"; txt.data.size = 1.2; txt.data.extrude = 0.1
txt.data.align_x = 'CENTER'; txt.data.materials.append(CREAM)

bpy.ops.mesh.primitive_plane_add(size=60, location=(0, 0, -3.6))
bpy.context.object.data.materials.append(FLOOR)

# ---------- lighting: key + rim + fill + glow from the sun ----------
pivot = bpy.data.objects.new("Pivot", None); sc.collection.objects.link(pivot)
pivot.location = (0, 0, -0.6)

def light(name, kind, loc, energy, color, size=4):
    d = bpy.data.lights.new(name, kind); d.energy = energy; d.color = color
    if kind == 'AREA': d.size = size
    o = bpy.data.objects.new(name, d); o.location = loc; sc.collection.objects.link(o)
    c = o.constraints.new('TRACK_TO'); c.target = pivot
    c.track_axis = 'TRACK_NEGATIVE_Z'; c.up_axis = 'UP_Y'
    return o, d

keyL, keyD = light("Key", 'AREA', (-6, -8, 6), 900, (1.0, 0.85, 0.7), 5)
light("Rim", 'AREA', (7, 5, 3), 700, (0.3, 0.9, 0.9), 4)
light("Fill", 'AREA', (6, -9, 1), 150, (0.8, 0.9, 1.0), 8)
glow = bpy.data.lights.new("SunGlow", 'POINT'); glow.energy = 0
glowO = bpy.data.objects.new("SunGlow", glow); glowO.location = (0, -1.5, 0.8)
sc.collection.objects.link(glowO)

# ---------- camera: orbit + dolly ----------
cam = bpy.data.objects.new("Cam", bpy.data.cameras.new("Cam")); sc.collection.objects.link(cam)
cam.data.lens = 50; cam.data.dof.use_dof = True
cam.data.dof.focus_object = pivot; cam.data.dof.aperture_fstop = 2.8
cam.parent = pivot; sc.camera = cam
c = cam.constraints.new('TRACK_TO'); c.target = pivot
c.track_axis = 'TRACK_NEGATIVE_Z'; c.up_axis = 'UP_Y'
cam.location = (0, -15, 0.5); cam.keyframe_insert("location", frame=1)
cam.location = (0, -10.5, 0.2); cam.keyframe_insert("location", frame=150)
pivot.rotation_euler = (0, 0, math.radians(-35)); pivot.keyframe_insert("rotation_euler", frame=1)
pivot.rotation_euler = (0, 0, math.radians(20));  pivot.keyframe_insert("rotation_euler", frame=150)

# ---------- animation timeline (30 fps) ----------
# Arc draws on: frames 1-45
cu.bevel_factor_end = 0.0; cu.keyframe_insert("bevel_factor_end", frame=1)
cu.bevel_factor_end = 1.0; cu.keyframe_insert("bevel_factor_end", frame=45)

# Sun pops in with overshoot: frames 25-55, plus a light flash (transition effect)
for f, s in ((25, 0.01), (45, 1.15), (55, 1.0)):
    sun.scale = (s, s, s); sun.keyframe_insert("scale", frame=f)
for f, e in ((25, 0), (45, 9000), (70, 1200), (150, 800)):
    glow.energy = e; glow.keyframe_insert("energy", frame=f)
for f, e in ((40, 900), (45, 2600), (60, 900)):
    keyD.energy = e; keyD.keyframe_insert("energy", frame=f)

# Base line wipes out from the centre: frames 45-70
for f, x in ((45, 0.001), (70, 4)):
    base.scale = (x, 0.5, 0.25); base.keyframe_insert("scale", frame=f)

# Wordmark rises and scales in: frames 70-105
for f, s, z in ((70, 0.01, -2.2), (105, 1.0, -2.7)):
    txt.scale = (s, s, s); txt.location.z = z
    txt.keyframe_insert("scale", frame=f); txt.keyframe_insert("location", frame=f)

print("Lumora 3D intro ready. Press Space to preview, Ctrl+F12 to render.")

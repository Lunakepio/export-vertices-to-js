# 📦 Blender to Three.js Export Add-on

This Blender add-on exports mesh vertices as an array of `THREE.Vector3(x, y, z)` for use in Three.js. It's ideal for converting curves or meshes into data that can be easily integrated into 3D web experiences.

---

## ✨ Features

- Converts vertex positions to `THREE.Vector3` format.
- Automatically swaps Y and Z axes to match Three.js coordinate system.
- Exports to a JavaScript module (`.js`) with ready-to-import `curve` and `closed` values.

---

## 🧰 Installation

1. Open **Blender**.
2. Go to **Edit > Preferences > Add-ons**.
3. Click **Install** and select the `.py` file for this add-on.
4. Enable the checkbox to activate the add-on.

---

## 📐 Preparing Your Curve or Object

To ensure correct export:

1. **Convert Curve to Mesh**  
   - Select the curve object.  
   - Press `Alt + C` or go to **Object > Convert > Mesh from Curve/Meta/Surf/Text**.

2. **Apply All Transforms**  
   - With the mesh selected, press `Ctrl + A`.  
   - Apply:
     - **Location**
     - **Rotation**
     - **Scale**

---

## 🚀 Exporting the Vertices

1. Select the mesh object(s) you want to export (optional).
2. Run the export function from the add-on:
   ```python
   export_vertices(filepath="/your/path/file.js", use_selection=True, closed=False)


## Example file 

```js import * as THREE from 'three'; export const curve = [ new THREE.Vector3(1.0, 0.0, 2.0), new THREE.Vector3(2.0, 0.0, 3.5), new THREE.Vector3(4.0, 0.0, 1.2) ]; export const closed = false; ```

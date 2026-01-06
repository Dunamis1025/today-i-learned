# GUI Utilities (01_gui_utils)

This folder contains small preparation scripts created  
before building the full Tkinter image merge GUI application.

Rather than jumping directly into a complex GUI,
each script here isolates and explains one core concept
that will later be reused inside the main project.

Together, these utilities form the foundation
for image generation, data handling, and layout logic.

---

## What this folder prepares

### 1. Generating sample image data

The script `01_auto_screenshot.py` is used to automatically
generate image files by capturing full-screen screenshots
at fixed time intervals.

This removes the need for external image assets
and allows quick, repeatable testing.

**Key ideas**
- Automated data generation
- Sequential file naming (`image1.png` ~ `image10.png`)
- Using Pillow (`ImageGrab`) for screen capture

---

### 2. Pairing and unpacking image metadata

The script `02_zip_and_unzip_image_metadata.py` demonstrates
how image-related data can be paired and unpacked
using Python’s `zip()` and unpacking syntax.

This mirrors how the image merge GUI later handles:
- File paths
- Image widths
- Image heights
- Layout positions

**Example concept**
```python
filenames = ["image1.png", "image2.png", "image3.png"]
heights = [300, 420, 280]

list(zip(filenames, heights))

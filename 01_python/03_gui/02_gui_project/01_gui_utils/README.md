# Auto Screenshot Generator

A small standalone Python utility that automatically captures
full-screen screenshots at fixed time intervals.

## What this script does
- Waits for a short preparation time
- Captures the entire screen every 2 seconds
- Saves screenshots as sequential image files
  (`image1.png` ~ `image10.png`)

## Why Pillow is used
This script uses **Pillow**, the modern fork of the Python Imaging Library (PIL).
Pillow provides the `ImageGrab` module, which allows screen capture
directly from Python.

## Installation
This project uses a virtual environment to isolate dependencies.

```bash
pip install pillow

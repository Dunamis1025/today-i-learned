import time
from PIL import ImageGrab

# --------------------------------------------------
# What is PIL?
# PIL stands for "Python Imaging Library".
# It is a library that allows Python to open, save,
# modify images, and capture the screen.
#
# Today, we use Pillow, which is the actively
# maintained fork of the original PIL project.
# Even though Pillow is installed, it is still
# imported using the name "PIL".
# --------------------------------------------------

# --------------------------------------------------
# What is ImageGrab?
# ImageGrab is a module included in Pillow.
# It captures the current screen and returns it
# as an image object.
#
# - ImageGrab.grab()
#   → Takes a screenshot of the entire screen
#   → Returns it as an Image object in memory
# --------------------------------------------------

# --------------------------------------------------
# time.sleep(5)
# A short delay before starting the capture.
# This gives the user time to prepare the screen:
# - Open the target window
# - Adjust window positions
# - Remove the mouse cursor if needed
# --------------------------------------------------
time.sleep(5)  # Wait 5 seconds before starting

# --------------------------------------------------
# Loop explanation
# range(1, 11) runs the loop 10 times (1 to 10).
#
# This loop:
# - Captures the screen every 2 seconds
# - Saves 10 screenshots in total
# - Names files from image1.png to image10.png
# --------------------------------------------------
for i in range(1, 11):

    # --------------------------------------------------
    # Capture the current screen
    # The result is an Image object stored in memory,
    # not a file yet.
    # --------------------------------------------------
    img = ImageGrab.grab()

    # --------------------------------------------------
    # Save the captured image as a file
    # format(i) automatically creates numbered filenames:
    # image1.png, image2.png, ..., image10.png
    # --------------------------------------------------
    img.save("image{}.png".format(i))

    # --------------------------------------------------
    # Wait 2 seconds before the next capture
    # This allows capturing changes over time
    # and generating test image sets automatically.
    # --------------------------------------------------
    time.sleep(2)

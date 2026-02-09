filenames = ["image1.png", "image2.png", "image3.png"]
heights = [300, 420, 280]

print(list(zip(filenames, heights)))

merged = [('image1.png', 300), ('image2.png', 420), ('image3.png', 280)]
print(list(zip(*merged)))

files, heights2 = zip(*merged)
print(files)
print(heights2)

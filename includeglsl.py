import os
for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".glsl"):
             print(os.path.join(root, file))




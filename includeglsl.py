import os
for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".glsl"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)




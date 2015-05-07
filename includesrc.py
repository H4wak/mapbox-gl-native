import os
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".cpp"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)

for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".pp"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)

for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".c"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)

for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".h"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)

for root, dirs, files in os.walk("include"):
    for file in files:
        if file.endswith(".hpp"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)

for root, dirs, files in os.walk("include"):
    for file in files:
        if file.endswith(".h"):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)

for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith("."):
             x=os.path.join(root, file)
             a="\\"
             b=a+a
             x=x.replace(a,b,50)
             print(x)



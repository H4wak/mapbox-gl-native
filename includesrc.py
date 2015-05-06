import os
for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".cpp"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".pp"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".c"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".h"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith(".cpp"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\include"):
    for file in files:
        if file.endswith(".hpp"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\include"):
    for file in files:
        if file.endswith(".h"):
             print(os.path.join(root, file))

for root, dirs, files in os.walk(".\src"):
    for file in files:
        if file.endswith("."):
             print(os.path.join(root, file))



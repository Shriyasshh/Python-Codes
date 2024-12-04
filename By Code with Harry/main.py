import os
if (not os.path.exists("data")):
    os.mkdir("data")

for x in range(0, 10):
    os.mkdir(f"data/Day{x+1}")


#Rename
for i in range(0, 10):
    os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")

    #os.rename(f"data/tutorial{i+1}",f"data/Tutorial {i+1}")

#List count /directories
folders=os.listdir("data")

print(folders)

for folder in folders:
    print(folder,end=" ")
    print(os.listdir(f"data/{folder}"))
    
print(os.getcwd())
import os

filepath = "/home/cody/Documents/Code/DriveSync/Python/DriveSync/test.txt"

print "Modification time: "
print os.path.getmtime(filepath)
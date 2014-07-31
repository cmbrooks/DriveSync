import os

filepath = "/home/cody/Documents/Code/DriveSync/Python/DriveSync/test.txt"

statbuf = os.stat(filepath)

print "Modification time: "
print os.path.getmtime(filepath)
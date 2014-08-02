import os
hdPath = "/home/cody/Documents/Sync/"
hdFileList = []

#Hard drive walk
for dirname, dirnames, filenames in os.walk(hdPath):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print "Subdirectory: " + os.path.join(dirname, subdirname)
    #print path to all filenames.
    for filename in filenames:
        print "Filename: " + os.path.join(dirname, filename)
        hdFileList.append(os.path.join(dirname, filename))

print "\nhdFileList is: "
print hdFileList
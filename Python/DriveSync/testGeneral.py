import os

hdPath = "/home/cody/Documents/Sync/"
hdPathLen = len(hdPath)
fdPath = "/var/run/media/cody/WARPDRIVE/"
fdPathLen = len(fdPath)

hdFileList = []
fdFileList = []

hdFilePathList = []
fdFilePathList = []

hdDate = os.path.getmtime(hdPath)
fdDate = os.path.getmtime(fdPath)

#Hard drive walk
print "Hard drive walk start"
print "Hard Drive Path: " + hdPath
for dirname, dirnames, filenames in os.walk(hdPath):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print "Subdirectory: " + os.path.join(dirname, subdirname)
    #print path to all filenames.
    for filename in filenames:
        filePath = os.path.join(dirname, filename)
        print "Original Filepath: " + filePath
        stripPath = filePath.lstrip(hdPath)
        print "Strip Path: " + stripPath
        hdFileList.append(filePath)
print "\nhdFileList is: "
print hdFileList
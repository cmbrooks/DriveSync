import os
import shutil

hdPath = "/home/cody/Documents/Sync/"
fdPath = "/var/run/media/cody/WARPDRIVE/"

hdFileList = []
fdFileList = []

hdFilePathList = []
fdFilePathList = []

hdDate = os.path.getmtime(hdPath)
fdDate = os.path.getmtime(fdPath)


###############################################################################


def copyFiles(hdFileDate, fdFileDate):
    if hdFileDate > fdFileDate:
        print "\nHard drive has latest copy of " + filename
        print "File coppied to " + os.path.join(fdPath, subdirname)
        #shutil.copy(filename, os.path.join(fdPath, subdirname))
        print "File has been coppied to the flash drive"
    elif hdFileDate == fdFileDate:
        print "Both HD and FD have latest copy"
    else:
        print "\nFlash drive has latest copy of " + filename
        print "File coppied to " + os.path.join(hdPath, subdirname)
        #shutil.copy(filename, os.path.join(hdPath, subdirname))
        print "File has been coppied to the hard drive"


###############################################################################


#Hard drive walk
print "\nHard drive walk start"
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


#Flash drive walk
print "\nFlash drive walk start"
for dirname, dirnames, filenames in os.walk(fdPath):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print "Subdirectory: " + os.path.join(dirname, subdirname)
    #print path to all filenames.
    for filename in filenames:
        print "Filename: " + os.path.join(dirname, filename)
        fdFileList.append(os.path.join(dirname, filename))
print "\nfdFileList is: "
print fdFileList


###############################################################################


#Date Comparison
if hdDate > fdDate:
    print "\nMod dates for listed files (HD)"
    for hdFileName in hdFileList:
        hdFileDate = os.path.getmtime(hdFileName)
        print hdFileName + " was last modified " + str(hdFileDate) + " (HD)"
        #compare to FD
        fdFileName = hdFileName.replace(hdPath, fdPath, 1)
        fdFileDate = os.path.getmtime(fdFileName)
        print hdFileName + " was last modified " + str(fdFileDate) + " (FD)"
        copyFiles(hdFileDate, fdFileDate)

else:
    print "\nMod dates for listed files (FD)"
    for fdFileName in fdFileList:
        fdFileDate = os.path.getmtime(hdFileName)
        print fdFileName + " was last modified " + str(fdFileDate) + " (FD)"
        #compare to HD
        hdFileName = hdFileName.replace(fdPath, hdPath, 1)
        hdFileDate = os.path.getmtime(hdFileName)
        print hdFileName + " was last modified " + str(hdFileDate) + " (HD)"
        copyFiles(hdFileDate, fdFileDate)


###############################################################################
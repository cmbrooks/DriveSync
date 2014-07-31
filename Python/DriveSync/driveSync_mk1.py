import os

flashdrivePath = "/var/run/media/cody/809D-3068/"
harddrivePath = "/home/cody/Documents/Sync"

flashdriveMod = os.path.getmtime(flashdrivePath)
harddriveMod = os.path.getmtime(harddrivePath)

if flashdriveMod > harddriveMod:
    print "Flash drive copy is newer"
else:
    print "Hard Drive copy is newer"
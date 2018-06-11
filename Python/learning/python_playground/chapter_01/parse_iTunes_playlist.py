import plistlib
from matplotlib import pyplot
import numpy as np
import random
def findDuplicates(fileName):
    print ("Finding Duplicate Tracks in playlist %s" % fileName)
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']

    trackNames = {}
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            if name in trackNames:
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
            else:
                trackNames[name] = (duration, 1)
        except:
            pass
    return trackNames

def plotStats(fileName):
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    ratings = []
    durations = []
    for trackId, track in tracks.items():
        try:
            ratings.append(random.randint(1, 5))
            durations.append(track['Total Time'])
        except:
            pass

    if len(ratings) > 0 and len(durations) > 0:
        x = np.array(durations, np.int32)
        # Convert durations to Minutes
        x = x/60000.0
        y = np.array(ratings, np.int32)
        pyplot.subplot(2, 1, 1)
        pyplot.plot(x, y, 'o')
        pyplot.axis([0, 1.05*np.max(x), -1, 6])
        pyplot.xlabel("Track Duration")
        pyplot.ylabel("Track Rating")

        pyplot.subplot(2, 1, 2)
        pyplot.hist(x, bins = 20)
        pyplot.xlabel("Track Duration")
        pyplot.ylabel("Count")

        pyplot.show()

plotStats("iTunes_playlist.xml")




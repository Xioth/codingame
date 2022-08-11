import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def distanceDefib(lon, lat, defibLon, defibLat):
    EARTH_RADIUS = 6371

    x = (lon - defibLon) * (math.cos((lat + defibLat) / 2))
    y = lat - defibLat
    d = math.sqrt((x**2 + y**2)) * EARTH_RADIUS

    return d

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())

# Initialize lists with n length.
defibId, name, address, phone, defibLon, defibLat = ([None] * n for _ in range(6))
distances = []

for i in range(n):
    defib = input()
    defibId[i], name[i], address[i], phone[i], defibLon[i], defibLat[i] = defib.replace(',', '.').split(";")
    defibLon[i], defibLat[i] = float(defibLon[i]), float(defibLat[i])

    distances.append(distanceDefib(lon, lat, defibLon[i], defibLat[i]))

closerDefibIndex = distances.index(min(distances))
print(name[closerDefibIndex])

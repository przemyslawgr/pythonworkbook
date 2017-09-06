import math
print("Program  display the distance between the points, following the surface of the earth, in kilometers.")
pointa_lat = int(input("Write point a latitude"))
pointa_long = int(input("Write point a longitude"))
pointb_lat = int(input("Write point b latitude"))
pointb_long = int(input("Write point b longitude"))
distance = 6371.01 * math.acos(math.sin(pointa_lat) * math.sin(pointb_lat) + math.cos(pointa_lat) * math.cos(pointb_lat)
                               * math.cos(pointa_long - pointb_long))
print(distance)

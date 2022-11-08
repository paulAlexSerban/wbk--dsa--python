# Modify this program to print the distance between the Sun and Mars (227.9 million km)
planet = "Mars"
distance_from_sun = 227.9 

if planet == "Mercury":
    distance_from_sun = 57.91
elif planet == "Venus":
    distance_from_sun = 108.2
elif planet == "Earth":
    distance_from_sun = 149.6

print(f"{planet} is {distance_from_sun} million km away from the Sun")
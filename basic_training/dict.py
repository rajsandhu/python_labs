from turtle import distance


distance_from_sun = {
    # KEY = VALUE
    "Mercury": {
        "moons": 0,
        "atmosphere": False
    },
    "Venus": {
        "moons": 0,
        "atmosphere": True
    },
    "Earth": {
        "moons": 1,
        "atmosphere": True
    },
    "Mars": 1.5
}

# print(distance_from_sun["Earth"]["atmosphere"])

# FOR LOOP

for planet in distance_from_sun:
    # print(planet)
    print(f"Planet {planet} --> moons {distance_from_sun[planet]['moons']}")

for planet, data in distance_from_sun:
    print(f"Planet {planet} --> moons {data['moons']}")    

for planet, data in distance_from_sun.items():
    print(f"Planet {planet} --> moons {data['moons']}")    
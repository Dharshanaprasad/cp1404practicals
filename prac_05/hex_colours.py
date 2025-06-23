"""Hex Colour Lookup
"""

COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2"
}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    print(COLOUR_TO_HEX.get(colour_name, "Invalid colour name"))
    colour_name = input("Enter colour name: ").lower()

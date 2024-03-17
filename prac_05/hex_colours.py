COLOR_TO_HEX = {"BRONZE": "#cd7f32", "PINK": "#fc83eac", "GRAY": "#bebebe", "IRIS": "#5a4fcf", "AQUA": "#00ffff",
                "AUREOLIN": "#fdee00", "BEIGE": "f5f5dc", "BISTRE": "#3d2b1f", "BONE": "#e3dac9", "BRASS": "#b5a642"}
print(COLOR_TO_HEX)

color = input("Enter color: ").upper()
while color != "":
    try:
        print(f"{color} is {COLOR_TO_HEX[color]}")
    except KeyError:
        print("Invalid color input")
    color = input("Enter color: ").upper()
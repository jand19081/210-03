def draw_trooper():
    trooper = {
            "row1": ["  ___  "],
            "row2": [" /___\ "],
            "row3": [" \   / "],
            "row4": ["  \ /  "],
            "row5": ["   0   "],
            "row6": ["  /|\  "],
            "row7": ["  / \  "]
            }

    keys = ["row1", "row2", "row3", "row4", "row5", "row6", "row7"]
    for key in keys:
        row = str(trooper[key][0])
        print(row)

draw_trooper()
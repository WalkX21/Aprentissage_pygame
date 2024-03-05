i = 0
colors_in_work = [[6,24,75],[3,44,189]]
colors = [[9,13,51], [0,137,171]]
distances = {}

def color_proche(colors, colors_in_work):

    for color in colors_in_work():

        for x in colors():
            
            distancex = color[0] - x[0]
            distancey = color[1] - x[1]
            distancez = color[2] - x[2]

            
            distance = (distancex ** 2 + distancey ** 2 + distancez ** 2) ** 0.5
            distances[distance] = color

    couleur_plus_proche = distances[min(distances.keys())]
    return couleur_plus_proche

couleur_plus_proche = color_proche(colors, colors_in_work)
print("La couleur la plus proche est :", couleur_plus_proche)
            




        




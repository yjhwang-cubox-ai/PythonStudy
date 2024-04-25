import colorgram

colors = colorgram.extract('18_Turtle/img.jpg',50)

color_list = []
for color in colors:
    color = color.rgb
    r = color[0]
    g = color[1]
    b = color[2]
    
    color_tuple = (r, g, b)
    color_list.append(color_tuple)

print(color_list)
    